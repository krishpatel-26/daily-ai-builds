import unittest,math
from orbitshield.dynamics import circular_state,derivative,rk4,specific_energy,impulse_prograde
from orbitshield.constants import R_EARTH
class Tests(unittest.TestCase):
 def test_radius(self):self.assertAlmostEqual(math.hypot(*circular_state(550)[:2]),R_EARTH+550)
 def test_energy_stability(self):
  s=circular_state(550);e=specific_energy(s)
  for _ in range(360):s=rk4(s,20)
  self.assertLess(abs((specific_energy(s)-e)/e),1e-6)
 def test_acceleration_radial(self):
  d=derivative(circular_state(550));self.assertLess(d[2],0);self.assertAlmostEqual(d[3],0)
 def test_impulse(self):
  a=circular_state(550);b=impulse_prograde(a,2)
  self.assertAlmostEqual(b[3]-a[3],.002,places=6)
 def test_bad_altitude(self):
  with self.assertRaises(ValueError):circular_state(30)
