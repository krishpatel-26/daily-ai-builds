import http from "node:http";
import {readFile} from "node:fs/promises";
import {extname,join,normalize} from "node:path";
import {fileURLToPath} from "node:url";
import {calculateSlo} from "./slo.js";
const root=fileURLToPath(new URL("../",import.meta.url));
const types={".html":"text/html; charset=utf-8",".css":"text/css; charset=utf-8",".js":"text/javascript; charset=utf-8"};
const server=http.createServer(async(req,res)=>{
 try{
  const url=new URL(req.url,"http://127.0.0.1");
  if(req.method==="POST"&&url.pathname==="/api/analyze"){
   let body="";for await(const chunk of req)body+=chunk;
   if(body.length>100000)throw new Error("Request too large");
   const result=calculateSlo(JSON.parse(body||"{}"));
   res.writeHead(200,{"content-type":"application/json"});return res.end(JSON.stringify(result));
  }
  if(req.method!=="GET")throw new Error("Method not allowed");
  const requested=url.pathname==="/"?"index.html":decodeURIComponent(url.pathname.slice(1));
  const path=normalize(join(root,requested));if(!path.startsWith(root))throw new Error("Invalid path");
  const data=await readFile(path);res.writeHead(200,{"content-type":types[extname(path)]||"application/octet-stream"});res.end(data);
 }catch(error){res.writeHead(error instanceof SyntaxError?400:400,{"content-type":"application/json"});res.end(JSON.stringify({error:error.message}));}
});
server.listen(4177,"127.0.0.1",()=>console.log("SLO Sentinel: http://127.0.0.1:4177"));
