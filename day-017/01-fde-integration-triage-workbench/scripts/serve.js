const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const port = Number(process.env.PORT || 4173);
const types = {'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8','.json':'application/json; charset=utf-8','.md':'text/markdown; charset=utf-8','.txt':'text/plain; charset=utf-8'};
http.createServer((req,res)=>{
  const pathname = decodeURIComponent(new URL(req.url,'http://localhost').pathname);
  const requested = pathname === '/' ? '/index.html' : pathname;
  const target = path.resolve(root,'.'+requested);
  if(!target.startsWith(root+path.sep) && target!==root){res.writeHead(403);res.end('Forbidden');return;}
  fs.readFile(target,(err,data)=>{
    if(err){res.writeHead(err.code==='ENOENT'?404:500,{'Content-Type':'text/plain; charset=utf-8'});res.end(err.code==='ENOENT'?'Not found':'Server error');return;}
    res.writeHead(200,{'Content-Type':types[path.extname(target)]||'application/octet-stream','X-Content-Type-Options':'nosniff','Cache-Control':'no-store'});res.end(data);
  });
}).listen(port,'127.0.0.1',()=>console.log('FDE Integration Triage Workbench running at http://127.0.0.1:'+port));
