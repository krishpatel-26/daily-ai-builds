import unittest
from app.engine import simulate,compare
class T(unittest.TestCase):
 def test_bounds(self):self.assertTrue(all(0<=v<=100 for v in simulate().values()))
 def test_descendant(self):self.assertNotEqual(compare({"player_reputation":90})["baseline"]["village_trust"],simulate({"player_reputation":90})["village_trust"])
 def test_unknown(self):
  with self.assertRaises(ValueError):simulate({"dragon":9})
 def test_intervention_fixed(self):self.assertEqual(simulate({"resource_supply":5})["resource_supply"],5)
if __name__=="__main__":unittest.main()