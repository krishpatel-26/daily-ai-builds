from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse,parse_qs
import json
from .report import report
from .network import JUNCTIONS
ROOT=Path(__file__).resolve().parent.parent/'web'
class Handler(BaseHTTPRequestHandler):
    def send_data(self,status,payload,mime='application/json'):
        data=payload if isinstance(payload,bytes) else payload.encode()
        self.send_response(status)
        for k,v in {'Content-Type':mime,'Content-Length':str(len(data)),'Cache-Control':'no-store','X-Content-Type-Options':'nosniff','Content-Security-Policy':"default-src 'self'; style-src 'self'; script-src 'self'"}.items():self.send_header(k,v)
        self.end_headers();self.wfile.write(data)
    def do_GET(self):
        url=urlparse(self.path)
        if url.path=='/api/report':
            try:
                q=parse_qs(url.query);node=q.get('node',['J-07'])[0];rate=float(q.get('rate',['4.5'])[0]);seed=int(q.get('seed',['52'])[0])
                if node not in {j.id for j in JUNCTIONS} or not (0<=rate<=12) or not (0<=seed<=100000):raise ValueError('Invalid node, rate or seed')
                return self.send_data(200,json.dumps(report(node,rate,seed)).encode())
            except (ValueError,OverflowError) as e:return self.send_data(400,json.dumps({'error':str(e)}))
        paths={'/':'index.html','/index.html':'index.html','/style.css':'style.css','/app.js':'app.js'}
        if url.path not in paths:return self.send_data(404,'Not Found','text/plain')
        p=ROOT/paths[url.path]
        return self.send_data(200,p.read_bytes(),{'.html':'text/html','.css':'text/css','.js':'text/javascript'}[p.suffix])
    def log_message(self,*args):pass
if __name__=='__main__':
    print('AquaMind at http://127.0.0.1:4208');ThreadingHTTPServer(('127.0.0.1',4208),Handler).serve_forever()
