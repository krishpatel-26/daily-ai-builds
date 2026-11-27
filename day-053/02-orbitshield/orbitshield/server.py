import json
from pathlib import Path
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from urllib.parse import urlparse,parse_qs
from .report import build
ROOT=Path(__file__).resolve().parent.parent/'web'
class Handler(BaseHTTPRequestHandler):
    def send_body(self,status,blob,mime):
        self.send_response(status)
        for k,v in {'Content-Type':mime,'Content-Length':str(len(blob)),'Cache-Control':'no-store','X-Content-Type-Options':'nosniff'}.items():self.send_header(k,v)
        self.end_headers();self.wfile.write(blob)
    def do_GET(self):
        u=urlparse(self.path)
        if u.path=='/api/report':
            try:
                q=parse_qs(u.query);result=build(int(q.get('seed',['53'])[0]),int(q.get('step',['20'])[0]))
                return self.send_body(200,json.dumps(result).encode(),'application/json')
            except (ValueError,TypeError) as e:return self.send_body(400,json.dumps({'error':str(e)}).encode(),'application/json')
        paths={'/':'index.html','/index.html':'index.html','/style.css':'style.css','/app.js':'app.js'}
        if u.path not in paths:return self.send_body(404,b'Not found','text/plain')
        p=ROOT/paths[u.path];mime={'.html':'text/html','.css':'text/css','.js':'text/javascript'}[p.suffix]
        return self.send_body(200,p.read_bytes(),mime)
    def log_message(self,*args):pass
if __name__=='__main__':
    print('OrbitShield http://127.0.0.1:4211');ThreadingHTTPServer(('127.0.0.1',4211),Handler).serve_forever()
