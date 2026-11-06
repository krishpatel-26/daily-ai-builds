import unittest
from app.world import reset,snapshot
from app.planner import generate
from app.lifecycle import activate,complete
class T(unittest.TestCase):
 def setUp(self):reset()
 def test_accept_complete(self):
  q=generate(snapshot())[0]["quest"];self.assertTrue(activate(q)["ok"]);self.assertTrue(complete(q["quest_id"])["ok"])
 def test_unknown_completion(self):self.assertFalse(complete("missing")["ok"])
if __name__=="__main__":unittest.main()