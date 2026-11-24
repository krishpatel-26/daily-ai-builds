from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from urllib.parse import urlsplit,parse_qs
from pathlib import Path
import json
from .report import report
ROOT=Path(__file__).resolve().parent.parent/'web'

class Handler(BaseHTTPRequestHandler):
    def respond(self,status,data,kind='application/json; charset=utf-8'):
        data=data if isinstance(data,bytes) else data.encode()
        self.send_response(status)
        for k,v in {'Content-Type':kind,'Content-Length':str(len(data)),'Cache-Control':'no-store','X-Content-Type-Options':'nosniff'}.items():self.send_header(k,v)
        self.end_headers();self.wfile.write(data)
    def do_GET(self):
        u=urlsplit(self.path);q=parse_qs(u.query)
        if u.path=='/api/report':
            try:
                policy=q.get('policy',['diversified'])[0];seed=int(q.get('seed',['50'])[0]);days=int(q.get('days',['70'])[0]);disrupted=q.get('disrupted',['true'])[0].lower()=='true'
                if not 0<=seed<=100000:raise ValueError('seed out of range')
                value=report(policy,seed,days,disrupted)
            except ValueError as e:return self.respond(400,json.dumps({'error':str(e)}))
            return self.respond(200,json.dumps(value))
        files={'/':'index.html','/index.html':'index.html','/style.css':'style.css','/app.js':'app.js'}
        if u.path not in files:return self.respond(404,'Not found','text/plain')
        name=files[u.path];kind={'.html':'text/html','.css':'text/css','.js':'text/javascript'}[Path(name).suffix]
        return self.respond(200,(ROOT/name).read_bytes(),kind+'; charset=utf-8')
    def log_message(self,*args):pass

if __name__=='__main__':
    print('SupplyChainOS at http://127.0.0.1:4205')
    ThreadingHTTPServer(('127.0.0.1',4205),Handler).serve_forever()
