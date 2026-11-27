import json
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse,parse_qs
from .report import build
ROOT=Path(__file__).resolve().parent.parent/'web'
class Handler(BaseHTTPRequestHandler):
    def reply(self,status,data,mime):
        self.send_response(status)
        for k,v in {'Content-Type':mime,'Content-Length':str(len(data)),'Cache-Control':'no-store','X-Content-Type-Options':'nosniff'}.items():self.send_header(k,v)
        self.end_headers();self.wfile.write(data)
    def do_GET(self):
        u=urlparse(self.path)
        if u.path=='/api/report':
            try:
                q=parse_qs(u.query);seed=int(q.get('seed',['53'])[0]);rounds=int(q.get('rounds',['18'])[0])
                result=build(seed,rounds)
                return self.reply(200,json.dumps(result).encode(),'application/json')
            except (ValueError,TypeError) as e:return self.reply(400,json.dumps({'error':str(e)}).encode(),'application/json')
        files={'/':'index.html','/index.html':'index.html','/style.css':'style.css','/app.js':'app.js'}
        if u.path not in files:return self.reply(404,b'Not found','text/plain')
        p=ROOT/files[u.path];mime={'.html':'text/html','.css':'text/css','.js':'text/javascript'}[p.suffix]
        return self.reply(200,p.read_bytes(),mime)
    def log_message(self,*args):pass
if __name__=='__main__':
    print('FederateLab http://127.0.0.1:4210');ThreadingHTTPServer(('127.0.0.1',4210),Handler).serve_forever()
