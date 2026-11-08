import unittest
from app.scenarios import run
class T(unittest.TestCase):
 def test_named(self):
  r=run("betrayal",{"player_reputation":0});self.assertEqual(r["name"],"betrayal");self.assertGreater(r["result"]["changed_count"],0)
if __name__=="__main__":unittest.main()