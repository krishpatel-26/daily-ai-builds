import unittest
from app.world import reset
from app.planner import propose
class T(unittest.TestCase):
 def test_policy_proposes(self):
  s=reset();p=propose(s["agents"]["bravo"],s);self.assertIn(p["action"]["action"],("gather","guard","rest","trade","attack"))
if __name__=="__main__":unittest.main()