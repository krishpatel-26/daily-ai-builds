import http from "node:http";
import { readFile } from "node:fs/promises";
import { extname, join, normalize } from "node:path";
import { fileURLToPath } from "node:url";
import { simulateRollout, evaluateExposure } from "./rollout.js";

const root = fileURLToPath(new URL("../", import.meta.url));
const types = { ".html": "text/html; charset=utf-8", ".css": "text/css", ".js": "text/javascript" };

const server = http.createServer(async (req, res) => {
  try {
    const url = new URL(req.url, "http://localhost");
    if (req.method === "POST" && url.pathname === "/api/simulate") {
      let body = "";
      for await (const chunk of req) body += chunk;
      if (body.length > 1_000_000) throw new Error("Request too large");
      const input = JSON.parse(body || "{}");
      const result = simulateRollout(input);
      res.writeHead(200, { "content-type": "application/json" });
      return res.end(JSON.stringify({ ...result, sampleExposure: ["user-001", "user-002", "user-003", "user-004"].map(id => ({ id, included: evaluateExposure(id, input.steps?.[0] ?? 1, true) })) }));
    }
    const requested = url.pathname === "/" ? "index.html" : decodeURIComponent(url.pathname.slice(1));
    const path = normalize(join(root, requested));
    if (!path.startsWith(root)) throw new Error("Invalid path");
    const data = await readFile(path);
    res.writeHead(200, { "content-type": types[extname(path)] || "application/octet-stream" });
    res.end(data);
  } catch (error) {
    res.writeHead(error instanceof SyntaxError ? 400 : 404, { "content-type": "application/json" });
    res.end(JSON.stringify({ error: error.message }));
  }
});

server.listen(4176, "127.0.0.1", () => console.log("Rollout simulator: http://127.0.0.1:4176"));
