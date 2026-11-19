import unittest
from factorytwin.simulator import simulate
from factorytwin.config import Config
class Tests(unittest.TestCase):
 def test_reproducible(self):self.assertEqual(simulate(Config(seed=9)),simulate(Config(seed=9)))
 def test_nonnegative(self):self.assertGreaterEqual(simulate()["completed"],0)
 def test_invalid_policy(self):
  with self.assertRaises(ValueError):simulate(policy="unknown")
