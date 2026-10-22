const el = id => document.getElementById(id);
const settingIds = ['sourceLanguage','intervalSeconds','opacity','apiFallback','apiEndpoint','apiKey'];
function renderStatus(value = {}) {
  el('statusMessage').textContent = value.message || 'Ready to translate.';
  el('mode').textContent = String(value.mode || 'idle').toUpperCase();
  el('statusDot').parentElement.classList.toggle('running', value.mode === 'running');
  el('lineCount').textContent = Number(value.translatedLines || 0).toLocaleString();
  el('engine').textContent = value.engine || 'Not run yet';
  el('toggleButton').textContent = value.mode === 'running' ? 'Pause live translation' : 'Start live translation';
}
function readSettings() {
  return { sourceLanguage: el('sourceLanguage').value, intervalSeconds: Number(el('intervalSeconds').value), opacity: Number(el('opacity').value), apiFallback: el('apiFallback').checked, apiEndpoint: el('apiEndpoint').value.trim(), apiKey: el('apiKey').value };
}
async function loadSettings() {
  const saved = await window.liveGlass.getSettings();
  for (const id of settingIds) {
    if (id === 'apiFallback') el(id).checked = Boolean(saved[id]);
    else if (saved[id] !== undefined) el(id).value = String(saved[id] || '');
  }
  el('opacityValue').textContent = el('opacity').value + '%';
}
el('toggleButton').addEventListener('click', async () => { await window.liveGlass.toggle(); renderStatus(await window.liveGlass.getStatus()); });
el('scanButton').addEventListener('click', async () => { el('statusMessage').textContent = 'Scanning…'; await window.liveGlass.scan(); });
el('clearButton').addEventListener('click', async () => { await window.liveGlass.clear(); renderStatus(await window.liveGlass.getStatus()); });
el('saveButton').addEventListener('click', async () => {
  try { const saved = await window.liveGlass.saveSettings(readSettings()); el('apiKey').value = saved.apiKey || ''; el('statusMessage').textContent = 'Settings saved on this device.'; }
  catch (error) { el('statusMessage').textContent = 'Could not save settings: ' + error.message; }
});
el('opacity').addEventListener('input', () => { el('opacityValue').textContent = el('opacity').value + '%'; });
window.liveGlass.onStatus(renderStatus);
loadSettings().then(() => window.liveGlass.getStatus().then(renderStatus)).catch(error => { el('statusMessage').textContent = error.message; });
