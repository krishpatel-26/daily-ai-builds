import unittest
from orbitshield.scenarios import make
from orbitshield.maneuvers import compare
from orbitshield.dynamics import circular_state,impulse_prograde
class Tests(unittest.TestCase):
 def test_seven_scenarios(self):self.assertEqual(len(compare(make(53),step=40)['scenarios']),7)
 def test_nonnegative(self):self.assertTrue(all(x['worst_miss_km']>=0 for x in compare(make(53),step=40)['scenarios']))
 def test_avoid_operational_claim(self):self.assertIn('educational',compare(make(53),step=60)['warning'])
 def test_impulse_bound(self):
  with self.assertRaises(ValueError):impulse_prograde(circular_state(550),10)
