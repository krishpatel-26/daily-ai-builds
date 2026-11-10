import unittest
from app.branches import choose
from app.schemas import WorldState
from app.templates import TEMPLATES
class T(unittest.TestCase):
 def test_route_changes(self):
  t=TEMPLATES[0];a=choose(t,WorldState(village_trust=80));b=choose(t,WorldState(village_trust=20));self.assertNotEqual(a[0]["route"],b[0]["route"])
if __name__=="__main__":unittest.main()