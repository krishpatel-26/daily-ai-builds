import unittest
from metrorl.environment import Corridor
from metrorl.policies import max_pressure
from metrorl.invariants import audit_trajectory
class Tests(unittest.TestCase):
 def test_valid_run(self):self.assertTrue(audit_trajectory(Corridor().run(max_pressure))['ok'])
 def test_detect_corruption(self):
  r=Corridor().run(max_pressure);r['stats']['exits']+=1
  self.assertIn('mass_conservation',audit_trajectory(r)['errors'])
