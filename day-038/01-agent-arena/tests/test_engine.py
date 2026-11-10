import unittest
from app.world import reset
from app.engine import run_turn
class T(unittest.TestCase):
 def test_turn_advances(self):reset();r=run_turn();self.assertEqual(r["turn"],1)
 def test_event_log(self):reset();run_turn();self.assertGreater(len(__import__("app.world",fromlist=["STATE"]).STATE["log"]),0)
if __name__=="__main__":unittest.main()