from http.server import ThreadingHTTPServer,BaseHTTPRequestHandler
from urllib.parse import urlsplit,parse_qs
from pathlib import Path
import json
from .scenarios import run,compare_outages
ROOT=Path(__file__).resolve().parent.parent/'web'

class Handler(BaseHTTPRequestHandler):
    def respond(self,status,data,kind='application/json; charset=utf-8'):
        raw=data if isinstance(data,bytes) else data.encode('utf-8')
        self.send_response(status)
        for k,v in {'Content-Type':kind,'Content-Length':str(len(raw)),'Cache-Control':'no-store','X-Content-Type-Options':'nosniff'}.items():self.send_header(k,v)
        self.end_headers();self.wfile.write(raw)
    def do_GET(self):
        url=urlsplit(self.path);params=parse_qs(url.query)
        if url.path=='/api/scenario':
            try:r=run(params.get('failed_line',[None])[0],params.get('strategy',['baseline'])[0])
            except ValueError as e:return self.respond(400,json.dumps({'error':str(e)}))
            return self.respond(200,json.dumps(r))
        if url.path=='/api/compare':return self.respond(200,json.dumps(compare_outages()))
        files={'/':'index.html','/index.html':'index.html','/style.css':'style.css','/app.js':'app.js'}
        if url.path not in files:return self.respond(404,'Not found','text/plain')
        name=files[url.path];kind={'.html':'text/html','.css':'text/css','.js':'text/javascript'}[Path(name).suffix]
        return self.respond(200,(ROOT/name).read_bytes(),kind+'; charset=utf-8')
    def log_message(self,*args):pass

if __name__=='__main__':
    print('GridSentinel at http://127.0.0.1:4204')
    ThreadingHTTPServer(('127.0.0.1',4204),Handler).serve_forever()
