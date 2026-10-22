const { spawn } = require('node:child_process');
const path = require('node:path');
const fs = require('node:fs');
function localTranslate(texts, settings) {
  return new Promise(resolve => {
    const script = path.join(__dirname, '..', 'scripts', 'local_translate.py');
    if (!fs.existsSync(script)) return resolve({ ok: false, reason: 'Local translator helper was not found.' });
    const candidates = process.platform === 'win32' ? [{ cmd: 'python', args: [script] }, { cmd: 'py', args: ['-3', script] }] : [{ cmd: 'python3', args: [script] }, { cmd: 'python', args: [script] }];
    let idx = 0;
    const attempt = () => {
      if (idx >= candidates.length) return resolve({ ok: false, reason: 'Python or Argos Translate is not installed.' });
      const item = candidates[idx++]; let stdout = '', stderr = '', child, settled = false;
      try { child = spawn(item.cmd, item.args, { windowsHide: true, stdio: ['pipe','pipe','pipe'] }); } catch { return attempt(); }
      const timeout = setTimeout(() => { if (!settled) { settled = true; child.kill(); resolve({ ok:false, reason:'Local translation timed out.' }); } }, 12000);
      child.stdout.setEncoding('utf8'); child.stderr.setEncoding('utf8');
      child.stdout.on('data', c => stdout += c); child.stderr.on('data', c => stderr += c);
      child.on('error', () => { clearTimeout(timeout); if (!settled) { settled = true; attempt(); } });
      child.on('close', code => {
        clearTimeout(timeout); if (settled) return; settled = true;
        try { const out = JSON.parse(stdout.trim()); if (out.ok && Array.isArray(out.translations) && out.translations.length === texts.length) return resolve({ ok:true, translations:out.translations, engine:'Argos Translate (local)' }); resolve({ ok:false, reason:out.reason || stderr || 'Local translation failed.' }); }
        catch { if (code !== 0 && idx < candidates.length) return attempt(); resolve({ ok:false, reason:'No local Argos language pair is installed.' }); }
      });
      child.stdin.end(JSON.stringify({ texts, source:settings.sourceLanguage, target:'en' }));
    };
    attempt();
  });
}
async function apiTranslate(texts, settings) {
  if (!settings.apiFallback) throw new Error('No local translation model is installed. Install Argos or enable API fallback in settings.');
  const endpoint = String(settings.apiEndpoint || '').trim();
  if (!/^https:\/\//i.test(endpoint) && !/^http:\/\/(localhost|127\.0\.0\.1)(:\d+)?\//i.test(endpoint)) throw new Error('API endpoint must use HTTPS (HTTP is allowed only for localhost).');
  const body = { q:texts.join('\n'), source:settings.sourceLanguage === 'auto' ? 'auto' : settings.sourceLanguage, target:'en', format:'text' };
  if (settings.apiKey && settings.apiKey !== '••••••••') body.api_key = settings.apiKey;
  const response = await fetch(endpoint, { method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify(body), signal:AbortSignal.timeout(15000) });
  if (!response.ok) throw new Error('Translation endpoint returned HTTP ' + response.status + '.');
  const data = await response.json();
  const joined = String(data.translatedText || data.translation || '');
  if (!joined) throw new Error('Translation API did not return translatedText.');
  const parts = joined.split('\n');
  return texts.map((_, i) => parts[i] || joined);
}
async function translateBatch(texts, settings) {
  if (!texts.length) return { translations:[], engine:'No text detected' };
  const local = await localTranslate(texts, settings);
  if (local.ok) return { translations:local.translations, engine:local.engine };
  return { translations:await apiTranslate(texts, settings), engine:'Translation API fallback' };
}
module.exports = { translateBatch };
