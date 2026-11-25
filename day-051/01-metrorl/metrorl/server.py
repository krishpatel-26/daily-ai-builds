import json
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse
from .report import report
ROOT=Path(__file__).resolve().parent.parent/'web'
MIME={'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8'}
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path=urlparse(self.path).path
        if path=='/api/report':return self.respond(200,json.dumps(report()).encode(),'application/json')
        files={'/':'index.html','/index.html':'index.html','/style.css':'style.css','/app.js':'app.js'}
        if path not in files:return self.respond(404,b'Not Found','text/plain')
        file=ROOT/files[path]
        return self.respond(200,file.read_bytes(),MIME[file.suffix])
    def respond(self,status,data,mime):
        self.send_response(status)
        for key,value in {'Content-Type':mime,'Content-Length':str(len(data)),'Cache-Control':'no-store','X-Content-Type-Options':'nosniff'}.items():self.send_header(key,value)
        self.end_headers();self.wfile.write(data)
    def log_message(self,*args):pass
if __name__=='__main__':
    print('MetroRL http://127.0.0.1:4206');ThreadingHTTPServer(('127.0.0.1',4206),Handler).serve_forever()
