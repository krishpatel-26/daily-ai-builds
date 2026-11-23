import json
import threading
import unittest
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer
from embodiedbench.server import Handler
class ApiTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.server=ThreadingHTTPServer(('127.0.0.1',0),Handler)
  cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True);cls.thread.start()
 @classmethod
 def tearDownClass(cls):cls.server.shutdown();cls.server.server_close();cls.thread.join(timeout=5)
 def url(self,path):return f'http://127.0.0.1:{self.server.server_port}{path}'
 def test_report(self):
  with urllib.request.urlopen(self.url('/api/report?policy=nearest&fault=true')) as r:
   data=json.load(r);self.assertEqual(data['simulation']['metrics']['completed_tasks'],3)
 def test_invalid_policy(self):
  with self.assertRaises(urllib.error.HTTPError) as e:urllib.request.urlopen(self.url('/api/report?policy=magic'))
  self.assertEqual(e.exception.code,400)
