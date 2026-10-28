import {createServer} from "node:http";
import {readFile} from "node:fs/promises";
import {resolve,normalize} from "node:path";
import {parseLogInput,analyzeLogs,toMarkdownReport} from "./triage.js";
const root=resolve(".");
const server=createServer(async(req,res)=>{res.setHeader("X-Content-Type-Options","nosniff");res.setHeader("Cache-Control","no-store");
if(req.method==="GET"&&(req.url==="/"||req.url==="/index.html")){try{const html=await readFile(resolve(root,"index.html"));res.writeHead(200,{"Content-Type":"text/html; charset=utf-8"});res.end(html)}catch{res.writeHead(500);res.end("index.html not found")}return}
if(req.method==="GET"&&req.url==="/api/health"){res.writeHead(200,{"Content-Type":"application/json"});res.end(JSON.stringify({ok:true,mode:"local-rule-based"}));return}
if(req.method==="POST"&&req.url==="/api/analyze"){let body="";req.on("data",c=>{body+=c;if(body.length>5*1024*1024){res.writeHead(413,{"Content-Type":"application/json"});res.end(JSON.stringify({error:"Request exceeds 5 MB limit"});req.destroy()}});req.on("end",()=>{try{const p=JSON.parse(body);const records=parseLogInput(p.input);const report=analyzeLogs(records);res.writeHead(200,{"Content-Type":"application/json"});res.end(JSON.stringify({report,markdown:toMarkdownReport(report)}))}catch(e){res.writeHead(400,{"Content-Type":"application/json"});res.end(JSON.stringify({error:e.message||"Invalid request"}))}});return}
res.writeHead(404,{"Content-Type":"application/json"});res.end(JSON.stringify({error:"Not found"}))});
const port=Number(process.env.PORT||4173);server.listen(port,"127.0.0.1",()=>console.log(`Incident Triage Workbench running at http://127.0.0.1:${port}`));
