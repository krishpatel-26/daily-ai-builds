from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
import json
from .benchmark import run
ROOT=Path(__file__).resolve().parent.parent
class Handler(BaseHTTPRequestHandler):
 def do_GET(self):
  mapping={"/":"web/index.html","/index.html":"web/index.html","/app.js":"web/app.js","/style.css":"web/style.css"}
  if self.path=="/api/demo":data=json.dumps(run()).encode();kind="application/json"
  elif self.path in mapping:
   data=(ROOT/mapping[self.path]).read_bytes();kind="text/html" if self.path in ("/","/index.html") else "text/javascript" if self.path.endswith(".js") else "text/css"
  else:data=b'{"error":"not found"}';kind="application/json"
  self.send_response(200 if self.path in mapping or self.path=="/api/demo" else 404);self.send_header("Content-Type",kind);self.send_header("Content-Length",str(len(data)));self.end_headers();self.wfile.write(data)
 def log_message(self,*args):pass
if __name__=="__main__":
 print("SwarmGrid http://127.0.0.1:4197");ThreadingHTTPServer(("127.0.0.1",4197),Handler).serve_forever()
