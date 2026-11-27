import unittest
from orbitshield.dynamics import circular_state
from orbitshield.propagate import propagate,closest
class Tests(unittest.TestCase):
 def test_length(self):self.assertEqual(len(propagate(circular_state(550),20,60)),4)
 def test_identical(self):
  p=propagate(circular_state(550),20,120);self.assertEqual(closest(p,p)['min_separation_km'],0)
 def test_different_lengths(self):
  with self.assertRaises(ValueError):closest([(0,(0,0,0,0))],[])
 def test_invalid_step(self):
  with self.assertRaises(ValueError):propagate(circular_state(550),130,120)
