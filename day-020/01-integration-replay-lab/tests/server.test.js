const test=require('node:test');
const assert=require('node:assert/strict');
const {spawn}=require('node:child_process');

async function launch(t){
 const port=4800+Math.floor(Math.random()*500);
 const child=spawn(process.execPath,['scripts/serve.js'],{cwd:process.cwd(),env:{...process.env,PORT:String(port)},stdio:['ignore','pipe','pipe']});
 let output='';child.stdout.on('data',c=>output+=c.toString());
 t.after(()=>child.kill());
 let response;
 for(let i=0;i<50;i++){
   try{response=await fetch('http://127.0.0.1:'+port+'/');break;}
   catch{await new Promise(r=>setTimeout(r,60));}
 }
 assert.ok(response,'server failed to start: '+output);
 return {port,first:response};
}

test('local server serves the dashboard and core asset with security headers',async t=>{
 const {port,first}=await launch(t);
 assert.equal(first.status,200);
 assert.match(first.headers.get('content-type'),/text\/html/);
 assert.match(first.headers.get('content-security-policy'),/default-src 'self'/);
 assert.match(await first.text(),/Integration Replay Lab/);
 const js=await fetch('http://127.0.0.1:'+port+'/src/core.js');
 assert.equal(js.status,200);
 assert.match(await js.text(),/runAll/);
});

test('server returns 404 for missing files and rejects path traversal',async t=>{
 const {port}=await launch(t);
 const missing=await fetch('http://127.0.0.1:'+port+'/does-not-exist');
 assert.equal(missing.status,404);
 const traversal=await fetch('http://127.0.0.1:'+port+'/%2e%2e/%2e%2e/etc/passwd');
 assert.notEqual(traversal.status,200);
});
