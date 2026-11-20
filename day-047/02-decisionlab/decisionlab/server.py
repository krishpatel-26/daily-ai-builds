from pathlib import Path
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
import json
from .report import report
ROOT=Path(__file__).resolve().parent.parent
MIME={'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8'}
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/api/report':
            return self.send_data(200,json.dumps(report()).encode(),'application/json')
        files={'/':'index.html','/index.html':'index.html','/style.css':'style.css','/app.js':'app.js'}
        if self.path not in files:return self.send_data(404,b'Not Found','text/plain')
        p=ROOT/'web'/files[self.path]
        self.send_data(200,p.read_bytes(),MIME[p.suffix])
    def send_data(self,status,data,mime):
        self.send_response(status);self.send_header('Content-Type',mime);self.send_header('Content-Length',str(len(data)));self.send_header('Cache-Control','no-store');self.send_header('X-Content-Type-Options','nosniff');self.end_headers();self.wfile.write(data)
    def log_message(self,*args):pass
if __name__=='__main__':
    print('DecisionLab http://127.0.0.1:4199');ThreadingHTTPServer(('127.0.0.1',4199),Handler).serve_forever()
