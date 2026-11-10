import unittest
from app.planner import plan
from app.schemas import WorldState
class T(unittest.TestCase):
 def test_limit(self):self.assertLessEqual(len(plan(WorldState(),limit=2)["recommendations"]),2)
 def test_completed_excluded(self):
  r=plan(WorldState(),completed=["Q001"]);self.assertNotIn("Q001",[q["quest_id"] for q in r["recommendations"]])
 def test_deterministic(self):
  s=WorldState();self.assertEqual(plan(s),plan(s))
if __name__=="__main__":unittest.main()