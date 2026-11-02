const http = require("node:http");
const fs = require("node:fs");
const path = require("node:path");
const { analyzeUsage } = require("./analytics");
const ROOT = path.join(__dirname, "..");
const PORT = Number(process.env.PORT || 4178);
const sample = JSON.parse(fs.readFileSync(path.join(ROOT, "data/sample-usage.json"), "utf8"));
let events = sample.events;
let monthlyBudget = Number(process.env.MONTHLY_BUDGET || sample.monthlyBudget || 100);
const mime = { ".html":"text/html", ".css":"text/css", ".js":"text/javascript", ".json":"application/json" };
function send(res, status, body, type="application/json") { res.writeHead(status, { "content-type": type }); res.end(type === "application/json" ? JSON.stringify(body) : body); }
const server = http.createServer((req,res) => {
  const url = new URL(req.url, "http://localhost");
  if (req.method === "GET" && url.pathname === "/api/analytics") return send(res,200,analyzeUsage(events,{monthlyBudget}));
  if (req.method === "GET" && url.pathname === "/api/events") return send(res,200,{events});
  if (req.method === "POST" && url.pathname === "/api/events") {
    let body = ""; req.on("data", chunk => body += chunk);
    req.on("end", () => {
      try {
        const incoming = JSON.parse(body);
        const batch = Array.isArray(incoming) ? incoming : [incoming];
        if (!batch.length) throw new Error("At least one event is required");
        for (const event of batch) {
          if (!event.model || !Number.isFinite(Number(event.inputTokens)) || !Number.isFinite(Number(event.outputTokens))) throw new Error("Each event requires model, inputTokens and outputTokens");
        }
        events = [...events, ...batch.map(e => ({...e, timestamp: e.timestamp || new Date().toISOString()}))];
        send(res,201,{added:batch.length,total:events.length});
      } catch (error) { send(res,400,{error:error.message}); }
    });
    return;
  }
  if (req.method === "POST" && url.pathname === "/api/budget") {
    let body = ""; req.on("data", chunk => body += chunk);
    req.on("end", () => { try { const value = Number(JSON.parse(body).monthlyBudget); if (!Number.isFinite(value) || value <= 0) throw new Error("Budget must be greater than zero"); monthlyBudget=value; send(res,200,{monthlyBudget}); } catch(e) { send(res,400,{error:e.message}); } });
    return;
  }
  const requested = url.pathname === "/" ? "/index.html" : url.pathname;
  const file = path.resolve(ROOT, "public", "." + requested);
  if (!file.startsWith(path.join(ROOT,"public") + path.sep)) return send(res,403,{error:"Forbidden"});
  fs.readFile(file,(err,data) => err ? send(res,404,{error:"Not found"}) : send(res,200,data,mime[path.extname(file)] || "text/plain"));
});
server.listen(PORT,"127.0.0.1",() => console.log(`Token Cost Observatory running at http://127.0.0.1:${PORT}`));