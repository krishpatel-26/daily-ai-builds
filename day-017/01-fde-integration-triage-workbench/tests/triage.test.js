const test = require('node:test');
const assert = require('node:assert/strict');
const { spawn } = require('node:child_process');

test('local server serves dashboard and analyzer assets', async t => {
  const port = 4317 + Math.floor(Math.random() * 300);
  const child = spawn(process.execPath, ['scripts/serve.js'], {
    cwd: process.cwd(),
    env: { ...process.env, PORT: String(port) },
    stdio: ['ignore', 'pipe', 'pipe']
  });
  let output = '';
  child.stdout.on('data', chunk => { output += chunk.toString(); });
  t.after(() => { child.kill(); });
  let response;
  for (let i=0; i<40; i++) {
    try { response = await fetch('http://127.0.0.1:'+port+'/'); break; }
    catch { await new Promise(resolve => setTimeout(resolve, 75)); }
  }
  assert.ok(response, 'server should start; log: '+output);
  assert.equal(response.status, 200);
  const html = await response.text();
  assert.match(html, /FDE Integration Triage Workbench/);
  const app = await fetch('http://127.0.0.1:'+port+'/app.js');
  assert.equal(app.status, 200);
  assert.match(await app.text(), /AUTH-401/);
});

test('static server refuses traversal outside project root', async t => {
  const port = 4700 + Math.floor(Math.random() * 200);
  const child = spawn(process.execPath, ['scripts/serve.js'], {
    cwd: process.cwd(),
    env: { ...process.env, PORT: String(port) },
    stdio: ['ignore','ignore','ignore']
  });
  t.after(() => { child.kill(); });
  let response;
  for (let i=0; i<40; i++) {
    try { response=await fetch('http://127.0.0.1:'+port+'/'); break; }
    catch { await new Promise(resolve=>setTimeout(resolve,75)); }
  }
  assert.ok(response);
  const traversal = await fetch('http://127.0.0.1:'+port+'/%2e%2e/%2e%2e/etc/passwd');
  assert.notEqual(traversal.status, 200);
});