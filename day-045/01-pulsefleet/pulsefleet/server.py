from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
import json
from .service import build_demo
ROOT=Path(__file__).resolve().parent.parent
class Handler(BaseHTTPRequestHandler):
 def send_body(self,status,body,kind="application/json; charset=utf-8"):
  data=body if isinstance(body,bytes) else body.encode();self.send_response(status);self.send_header("Content-Type",kind);self.send_header("Content-Length",str(len(data)));self.send_header("X-Content-Type-Options","nosniff");self.end_headers();self.wfile.write(data)
 def do_GET(self):
  files={"/":("web/index.html","text/html; charset=utf-8"),"/index.html":("web/index.html","text/html; charset=utf-8"),"/styles.css":("web/styles.css","text/css; charset=utf-8"),"/app.js":("web/app.js","text/javascript; charset=utf-8")}
  if self.path=="/api/health":self.send_body(200,json.dumps(build_demo()));return
  if self.path in files:
   path,kind=files[self.path];self.send_body(200,(ROOT/path).read_bytes(),kind);return
  self.send_body(404,json.dumps({"error":"not found"}))
 def log_message(self,*args):pass
def main():
 server=ThreadingHTTPServer(("127.0.0.1",4195),Handler);print("PulseFleet at http://127.0.0.1:4195");server.serve_forever()
if __name__=="__main__":main()
