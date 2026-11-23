import json
import threading
import unittest
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer
from genesislab.server import Handler

class ApiTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.http=ThreadingHTTPServer(('127.0.0.1',0),Handler)
  cls.thread=threading.Thread(target=cls.http.serve_forever,daemon=True)
  cls.thread.start()
 @classmethod
 def tearDownClass(cls):cls.http.shutdown();cls.http.server_close();cls.thread.join(timeout=5)
 def url(self,path):return f'http://127.0.0.1:{self.http.server_port}{path}'
 def test_report(self):
  with urllib.request.urlopen(self.url('/api/report?seed=49&budget=8')) as response:
   data=json.load(response);self.assertEqual(data['trial']['experiments'],8)
 def test_invalid_budget(self):
  with self.assertRaises(urllib.error.HTTPError) as caught:urllib.request.urlopen(self.url('/api/report?budget=2'))
  self.assertEqual(caught.exception.code,400)
 def test_index(self):
  with urllib.request.urlopen(self.url('/')) as response:self.assertIn(b'GENESIS',response.read())
