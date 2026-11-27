import unittest
from orbitshield.report import build
from orbitshield.benchmark import sweep
class Tests(unittest.TestCase):
 def test_report(self):
  r=build(53,step=60);self.assertEqual(r['inputs']['seed'],53);self.assertIn('benchmark',r)
 def test_sweep(self):self.assertEqual(sweep(seeds=range(3),step=60)['cases'],3)
 def test_bad_step(self):
  with self.assertRaises(ValueError):build(53,0)
