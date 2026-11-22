from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
import json
from .report import demo
ROOT=Path(__file__).resolve().parent.parent/'web'
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/api/demo':return self.respond(200,json.dumps(demo()).encode(),'application/json')
        files={'/':'index.html','/index.html':'index.html','/app.js':'app.js','/style.css':'style.css'}
        if self.path not in files:return self.respond(404,b'Not Found','text/plain')
        file=ROOT/files[self.path]
        return self.respond(200,file.read_bytes(),{'html':'text/html','js':'text/javascript','css':'text/css'}[file.suffix[1:]])
    def respond(self,status,data,kind):
        self.send_response(status)
        for k,v in {'Content-Type':kind,'Content-Length':str(len(data)),'Cache-Control':'no-store','X-Content-Type-Options':'nosniff'}.items():self.send_header(k,v)
        self.end_headers();self.wfile.write(data)
    def log_message(self,*args):pass
if __name__=='__main__':
    print('TrustLayer http://127.0.0.1:4201');ThreadingHTTPServer(('127.0.0.1',4201),Handler).serve_forever()