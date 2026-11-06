import unittest
from app.world import reset,snapshot
from app.planner import generate
class T(unittest.TestCase):
 def setUp(self):reset()
 def test_candidates_are_valid(self):
  r=generate(snapshot());self.assertTrue(r);self.assertTrue(all(x["validation"]["valid"] for x in r))
 def test_tone_filter(self):
  r=generate(snapshot(),"social");self.assertTrue(all(x["quest"]["quest_id"]=="elder_report" for x in r))
if __name__=="__main__":unittest.main()