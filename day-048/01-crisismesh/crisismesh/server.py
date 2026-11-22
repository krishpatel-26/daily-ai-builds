import json
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse,parse_qs
from .experiment import compare,benchmark
ROOT=Path(__file__).resolve().parent.parent/'web'
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url=urlparse(self.path); q=parse_qs(url.query)
        if url.path=='/api/scenario':
            try:
                seed=int(q.get('seed',['48'])[0]); assert 0<=seed<=100000
                data=json.dumps(compare(seed)).encode()
            except (ValueError,AssertionError):return self.send_data(400,b'{"error":"seed must be 0..100000"}','application/json')
            return self.send_data(200,data,'application/json')
        if url.path=='/api/benchmark':return self.send_data(200,json.dumps(benchmark()).encode(),'application/json')
        files={'/':'index.html','/index.html':'index.html','/app.js':'app.js','/style.css':'style.css'}
        if url.path not in files:return self.send_data(404,b'Not Found','text/plain')
        name=files[url.path];kind={'html':'text/html','js':'text/javascript','css':'text/css'}[name.rsplit('.',1)[-1]]
        return self.send_data(200,(ROOT/name).read_bytes(),kind)
    def send_data(self,status,content,kind):
        self.send_response(status)
        for k,v in {'Content-Type':kind,'Content-Length':str(len(content)),'Cache-Control':'no-store','X-Content-Type-Options':'nosniff','Access-Control-Allow-Origin':'same-origin'}.items():self.send_header(k,v)
        self.end_headers();self.wfile.write(content)
    def log_message(self,*args):pass
if __name__=='__main__':
    print('CrisisMesh http://127.0.0.1:4200');ThreadingHTTPServer(('127.0.0.1',4200),Handler).serve_forever()