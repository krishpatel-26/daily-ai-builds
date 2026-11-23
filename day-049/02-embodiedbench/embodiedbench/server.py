import json
from pathlib import Path
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from urllib.parse import urlparse,parse_qs
from .report import report
ROOT=Path(__file__).resolve().parent.parent/'web'
MIME={'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8'}
class Handler(BaseHTTPRequestHandler):
    def send_data(self,status,body,kind):
        self.send_response(status)
        for k,v in {'Content-Type':kind,'Content-Length':str(len(body)),
                    'Cache-Control':'no-store','X-Content-Type-Options':'nosniff'}.items():self.send_header(k,v)
        self.end_headers();self.wfile.write(body)
    def do_GET(self):
        u=urlparse(self.path)
        if u.path=='/api/report':
            q=parse_qs(u.query)
            try:
                policy=q.get('policy',['nearest'])[0]
                fault=q.get('fault',['true'])[0]=='true'
                limit=int(q.get('limit',['200'])[0])
                data=report(policy,fault,limit)
            except (ValueError,OverflowError) as exc:
                return self.send_data(400,json.dumps({'error':str(exc)}).encode(),'application/json')
            return self.send_data(200,json.dumps(data).encode(),'application/json')
        mapping={'/':'index.html','/index.html':'index.html','/style.css':'style.css','/app.js':'app.js'}
        if u.path not in mapping:return self.send_data(404,b'Not Found','text/plain')
        p=ROOT/mapping[u.path]
        return self.send_data(200,p.read_bytes(),MIME[p.suffix])
    def log_message(self,*args):pass
if __name__=='__main__':
    print('EmbodiedBench http://127.0.0.1:4203')
    ThreadingHTTPServer(('127.0.0.1',4203),Handler).serve_forever()
