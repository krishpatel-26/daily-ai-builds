import json
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse,parse_qs
from .service import report
ROOT=Path(__file__).resolve().parent.parent
MIME={'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8'}
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url=urlparse(self.path)
        if url.path=='/api/report':
            q=parse_qs(url.query)
            try: data=json.dumps(report(seed=int(q.get('seed',['47'])[0]),ticks=int(q.get('ticks',['110'])[0]))).encode()
            except ValueError as err:return self.send_data(400,json.dumps({'error':str(err)}).encode(),'application/json')
            return self.send_data(200,data,'application/json')
        mapping={'/':'index.html','/index.html':'index.html','/style.css':'style.css','/app.js':'app.js'}
        if url.path not in mapping:return self.send_data(404,b'Not Found','text/plain')
        path=ROOT/'web'/mapping[url.path]
        return self.send_data(200,path.read_bytes(),MIME[path.suffix])
    def send_data(self,status,data,mime):
        self.send_response(status);self.send_header('Content-Type',mime);self.send_header('Content-Length',str(len(data)));self.send_header('Cache-Control','no-store');self.send_header('X-Content-Type-Options','nosniff');self.end_headers();self.wfile.write(data)
    def log_message(self,*args):pass
if __name__=='__main__':
    print('FleetOps http://127.0.0.1:4198');ThreadingHTTPServer(('127.0.0.1',4198),Handler).serve_forever()
