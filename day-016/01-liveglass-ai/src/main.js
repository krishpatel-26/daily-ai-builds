const { app, BrowserWindow, desktopCapturer, screen, ipcMain, globalShortcut, Tray, Menu, nativeImage, safeStorage } = require('electron');
const path = require('node:path');
const fs = require('node:fs');
const { createWorker } = require('tesseract.js');
const { translateBatch } = require('./translator');

const DEFAULTS = { sourceLanguage: 'de', targetLanguage: 'en', intervalSeconds: 4, opacity: 92, apiFallback: false, apiEndpoint: 'https://libretranslate.com/translate', apiKey: '' };
const OCR_LANGUAGE = { auto: 'eng', en: 'eng', de: 'deu', fr: 'fra', es: 'spa', it: 'ita', pt: 'por', nl: 'nld', tr: 'tur', ru: 'rus', ja: 'jpn', zh: 'chi_sim' };
let dashboard = null, overlay = null, tray = null, worker = null, running = false, busy = false, timer = null, generation = 0;
let settings = { ...DEFAULTS };
let status = { mode: 'idle', message: 'Ready to translate', translatedLines: 0 };

const settingsPath = () => path.join(app.getPath('userData'), 'settings.json');
function cleanSettings(input = {}) {
  const s = { ...DEFAULTS, ...input };
  if (!Object.hasOwn(OCR_LANGUAGE, s.sourceLanguage)) s.sourceLanguage = 'de';
  s.targetLanguage = 'en';
  s.intervalSeconds = Math.min(12, Math.max(3, Number(s.intervalSeconds) || 4));
  s.opacity = Math.min(100, Math.max(50, Number(s.opacity) || 92));
  s.apiFallback = Boolean(s.apiFallback);
  s.apiEndpoint = String(s.apiEndpoint || DEFAULTS.apiEndpoint).trim();
  s.apiKey = String(s.apiKey || '');
  return s;
}
function loadSettings() {
  try {
    const disk = JSON.parse(fs.readFileSync(settingsPath(), 'utf8'));
    if (disk.apiKeyEncrypted && safeStorage.isEncryptionAvailable()) {
      try { disk.apiKey = safeStorage.decryptString(Buffer.from(disk.apiKeyEncrypted, 'base64')); } catch { disk.apiKey = ''; }
    }
    delete disk.apiKeyEncrypted;
    settings = cleanSettings(disk);
  } catch { settings = { ...DEFAULTS }; }
}
function saveSettings(patch = {}) {
  settings = cleanSettings({ ...settings, ...patch });
  const disk = { ...settings };
  delete disk.apiKey;
  if (settings.apiKey && safeStorage.isEncryptionAvailable()) disk.apiKeyEncrypted = safeStorage.encryptString(settings.apiKey).toString('base64');
  fs.mkdirSync(path.dirname(settingsPath()), { recursive: true });
  fs.writeFileSync(settingsPath(), JSON.stringify(disk, null, 2), { mode: 0o600 });
  return { ...settings, apiKey: settings.apiKey ? '••••••••' : '' };
}
function publishStatus(mode, message, extra = {}) {
  status = { ...status, mode, message, ...extra };
  if (dashboard && !dashboard.isDestroyed()) dashboard.webContents.send('app:status', status);
  if (tray) tray.setToolTip('LiveGlass AI — ' + message);
}
function createDashboard() {
  dashboard = new BrowserWindow({ width: 940, height: 740, minWidth: 760, minHeight: 650, title: 'LiveGlass AI', backgroundColor: '#081018', autoHideMenuBar: true, show: false,
    webPreferences: { preload: path.join(__dirname, 'preload.js'), contextIsolation: true, nodeIntegration: false, sandbox: true } });
  dashboard.loadFile(path.join(__dirname, 'dashboard.html'));
  dashboard.once('ready-to-show', () => { dashboard.show(); dashboard.webContents.send('app:status', status); });
  dashboard.on('close', event => { if (!app.isQuitting && tray) { event.preventDefault(); dashboard.hide(); } });
}
function createOverlay() {
  const d = screen.getPrimaryDisplay();
  overlay = new BrowserWindow({ x: d.bounds.x, y: d.bounds.y, width: d.bounds.width, height: d.bounds.height, frame: false, transparent: true, backgroundColor: '#00000000', show: false, resizable: false, movable: false, alwaysOnTop: true, skipTaskbar: true, hasShadow: false, focusable: false,
    webPreferences: { preload: path.join(__dirname, 'preload.js'), contextIsolation: true, nodeIntegration: false, sandbox: true } });
  overlay.setAlwaysOnTop(true, 'screen-saver');
  overlay.setIgnoreMouseEvents(true, { forward: true });
  try { overlay.setContentProtection(true); } catch {}
  overlay.loadFile(path.join(__dirname, 'overlay.html'));
  overlay.on('closed', () => { overlay = null; });
}
async function getWorker() {
  const lang = OCR_LANGUAGE[settings.sourceLanguage] || 'eng';
  if (worker && worker.__language === lang) return worker;
  if (worker) { try { await worker.terminate(); } catch {} }
  publishStatus(running ? 'running' : 'scanning', 'Loading local OCR model: ' + lang);
  const cachePath = path.join(app.getPath('userData'), 'ocr-cache');
  fs.mkdirSync(cachePath, { recursive: true });
  worker = await createWorker(lang, 1, { cachePath, logger: () => {} });
  worker.__language = lang;
  return worker;
}
async function scanOnce() {
  if (busy) return;
  busy = true;
  const scanId = ++generation;
  try {
    publishStatus(running ? 'running' : 'scanning', 'Capturing primary display…');
    const display = screen.getPrimaryDisplay();
    const sources = await desktopCapturer.getSources({ types: ['screen'], thumbnailSize: { width: Math.max(800, display.size.width), height: Math.max(600, display.size.height) }, fetchWindowIcons: false });
    const source = sources.find(item => item.display_id === String(display.id)) || sources[0];
    if (!source || source.thumbnail.isEmpty()) throw new Error('No screen image returned. Check Windows capture permissions.');
    const size = source.thumbnail.getSize();
    const result = await (await getWorker()).recognize(source.thumbnail.toPNG());
    if (scanId !== generation || !overlay || overlay.isDestroyed()) return;
    const lines = (result.data.lines || []).map(line => ({ text: String(line.text || '').trim(), bbox: line.bbox, confidence: Number(line.confidence || 0) })).filter(line => line.text.length >= 2 && line.confidence >= 30).slice(0, 180);
    publishStatus(running ? 'running' : 'scanning', 'Translating ' + lines.length + ' detected lines…');
    const translated = await translateBatch(lines.map(line => line.text), settings);
    if (scanId !== generation || !overlay || overlay.isDestroyed()) return;
    const items = lines.map((line, i) => ({ original: line.text, text: translated.translations[i] || line.text, confidence: line.confidence,
      x: line.bbox.x0 / size.width * display.bounds.width, y: line.bbox.y0 / size.height * display.bounds.height,
      width: (line.bbox.x1 - line.bbox.x0) / size.width * display.bounds.width, height: (line.bbox.y1 - line.bbox.y0) / size.height * display.bounds.height
    })).filter(item => item.width > 8 && item.height > 5);
    overlay.webContents.send('overlay:items', { items, opacity: settings.opacity / 100 });
    if (!overlay.isVisible()) overlay.showInactive();
    publishStatus(running ? 'running' : 'idle', 'Translated ' + items.length + ' lines via ' + translated.engine, { translatedLines: items.length, engine: translated.engine });
  } catch (error) { publishStatus('error', error.message || String(error)); }
  finally { busy = false; }
}
function stopLive() { running = false; generation++; if (timer) clearInterval(timer); timer = null; publishStatus('idle', 'Live translation paused'); }
function startLive() { if (running) return; running = true; if (overlay && !overlay.isDestroyed()) overlay.showInactive(); scanOnce(); timer = setInterval(scanOnce, settings.intervalSeconds * 1000); publishStatus('running', 'Live translation active'); }
function toggleLive() { running ? stopLive() : startLive(); return running; }
function clearOverlay() { generation++; if (overlay && !overlay.isDestroyed()) overlay.webContents.send('overlay:items', { items: [], opacity: settings.opacity / 100 }); publishStatus(running ? 'running' : 'idle', 'Overlay cleared'); }
function showDashboard() { if (dashboard && !dashboard.isDestroyed()) { dashboard.show(); dashboard.focus(); } }
function createTray() {
  tray = new Tray(nativeImage.createEmpty());
  tray.setToolTip('LiveGlass AI');
  tray.setContextMenu(Menu.buildFromTemplate([{ label: 'Show controls', click: showDashboard }, { label: 'Start / pause translation', click: toggleLive }, { label: 'Scan once', click: scanOnce }, { label: 'Clear overlay', click: clearOverlay }, { type: 'separator' }, { label: 'Quit', click: () => { app.isQuitting = true; app.quit(); } }]));
}
app.whenReady().then(() => {
  loadSettings(); createDashboard(); createOverlay(); createTray();
  globalShortcut.register('CommandOrControl+Shift+L', toggleLive);
  globalShortcut.register('CommandOrControl+Shift+O', showDashboard);
  globalShortcut.register('CommandOrControl+Shift+K', clearOverlay);
  ipcMain.handle('settings:get', () => ({ ...settings, apiKey: settings.apiKey ? '••••••••' : '' }));
  ipcMain.handle('settings:save', (_e, patch) => { const value = { ...patch }; if (value.apiKey === '••••••••') delete value.apiKey; const saved = saveSettings(value); if (running) { stopLive(); startLive(); } return saved; });
  ipcMain.handle('translation:toggle', () => toggleLive());
  ipcMain.handle('translation:scan', () => scanOnce());
  ipcMain.handle('translation:clear', () => clearOverlay());
  ipcMain.handle('app:status', () => status);
  app.on('activate', showDashboard);
});
app.on('will-quit', () => { globalShortcut.unregisterAll(); if (worker) worker.terminate().catch(() => {}); });
