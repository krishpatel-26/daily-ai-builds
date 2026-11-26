from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse,parse_qs
import json
from .topology import SERVICES
from .report import report
ROOT=Path(__file__).resolve().parent.parent/'web'
class Handler(BaseHTTPRequestHandler):
    def send_data(self,status,data,mime='application/json'):
        body=data if isinstance(data,bytes) else data.encode()
        self.send_response(status)
        for k,v in {'Content-Type':mime,'Content-Length':str(len(body)),'Cache-Control':'no-store','X-Content-Type-Options':'nosniff','Content-Security-Policy':"default-src 'self'; style-src 'self'; script-src 'self'"}.items():self.send_header(k,v)
        self.end_headers();self.wfile.write(body)
    def do_GET(self):
        url=urlparse(self.path)
        if url.path=='/api/report':
            try:
                q=parse_qs(url.query);root=q.get('root',['database'])[0];seed=int(q.get('seed',['52'])[0]);strength=float(q.get('strength',['2.7'])[0])
                if root not in SERVICES or not (0<=seed<=100000) or not (0<=strength<=10):raise ValueError('Invalid root, seed or strength')
                return self.send_data(200,json.dumps(report(root,seed,strength)))
            except (ValueError,OverflowError) as e:return self.send_data(400,json.dumps({'error':str(e)}))
        files={'/':'index.html','/index.html':'index.html','/style.css':'style.css','/app.js':'app.js'}
        if url.path not in files:return self.send_data(404,'Not Found','text/plain')
        path=ROOT/files[url.path]
        return self.send_data(200,path.read_bytes(),{'.html':'text/html','.css':'text/css','.js':'text/javascript'}[path.suffix])
    def log_message(self,*args):pass
if __name__=='__main__':
    print('CausalScope at http://127.0.0.1:4209');ThreadingHTTPServer(('127.0.0.1',4209),Handler).serve_forever()
