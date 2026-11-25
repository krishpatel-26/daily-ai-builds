import unittest
from metrorl.sensitivity import sweep
class Tests(unittest.TestCase):
 def test_sweep_has_nine_rows(self):self.assertEqual(len(sweep(seeds=(1,),episodes=2)),9)
 def test_invalid_demand(self):
  with self.assertRaises(ValueError):sweep(arrivals=(-1,),seeds=(1,),episodes=2)
