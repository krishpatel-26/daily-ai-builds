from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
import json
from .report import build_report
ROOT=Path(__file__).resolve().parent.parent
class Handler(BaseHTTPRequestHandler):
 def do_GET(self):
  paths={"/":"web/index.html","/index.html":"web/index.html","/app.js":"web/app.js","/style.css":"web/style.css"}
  if self.path=="/api/report":data=json.dumps(build_report()).encode();kind="application/json"
  elif self.path in paths:
   data=(ROOT/paths[self.path]).read_bytes();kind="text/html" if self.path in ("/","/index.html") else "text/javascript" if self.path.endswith(".js") else "text/css"
  else:data=b'{"error":"not found"}';kind="application/json"
  self.send_response(200 if self.path in paths or self.path=="/api/report" else 404);self.send_header("Content-Type",kind);self.send_header("Content-Length",str(len(data)));self.end_headers();self.wfile.write(data)
 def log_message(self,*args):pass
if __name__=="__main__":
 print("FactoryTwin AI http://127.0.0.1:4196");ThreadingHTTPServer(("127.0.0.1",4196),Handler).serve_forever()
