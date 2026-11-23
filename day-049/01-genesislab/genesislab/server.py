import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs
from .report import report
ROOT=Path(__file__).resolve().parent.parent/'web'
MIME={'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8'}
class Handler(BaseHTTPRequestHandler):
    def send_data(self,status,contents,kind):
        self.send_response(status)
        for k,v in {'Content-Type':kind,'Content-Length':str(len(contents)),
                    'X-Content-Type-Options':'nosniff','Cache-Control':'no-store'}.items():self.send_header(k,v)
        self.end_headers();self.wfile.write(contents)
    def do_GET(self):
        parsed=urlparse(self.path)
        if parsed.path=='/api/report':
            q=parse_qs(parsed.query)
            try:
                seed=int(q.get('seed',['49'])[0]);budget=int(q.get('budget',['16'])[0])
                if not 0<=seed<=100000:raise ValueError('Seed must be 0..100000')
                payload=report(seed,budget)
            except (ValueError,OverflowError) as exc:
                return self.send_data(400,json.dumps({'error':str(exc)}).encode(),'application/json')
            return self.send_data(200,json.dumps(payload).encode(),'application/json')
        files={'/':'index.html','/index.html':'index.html','/style.css':'style.css','/app.js':'app.js'}
        if parsed.path not in files:return self.send_data(404,b'Not Found','text/plain')
        path=ROOT/files[parsed.path]
        return self.send_data(200,path.read_bytes(),MIME[path.suffix])
    def log_message(self,*args):pass
if __name__=='__main__':
    print('GenesisLab available at http://127.0.0.1:4202')
    ThreadingHTTPServer(('127.0.0.1',4202),Handler).serve_forever()
