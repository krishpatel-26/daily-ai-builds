import unittest
from app.scoring import score
from app.schemas import WorldState
from app.templates import TEMPLATES
class T(unittest.TestCase):
 def test_score_numeric(self):self.assertIsInstance(score(TEMPLATES[0],WorldState())[0],float)
 def test_high_trust_bonus(self):
  a=score(TEMPLATES[0],WorldState(village_trust=20))[0];b=score(TEMPLATES[0],WorldState(village_trust=90))[0];self.assertGreater(b,a)
if __name__=="__main__":unittest.main()