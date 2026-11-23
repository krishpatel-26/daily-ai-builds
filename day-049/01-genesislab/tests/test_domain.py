import unittest
from genesislab.domain import candidates,Candidate,safe
from genesislab.process import measure,true_quality
class Tests(unittest.TestCase):
 def test_all_candidates_safe(self):self.assertTrue(all(safe(c) for c in candidates()))
 def test_boundary_rejected(self):self.assertFalse(safe(Candidate(240,120)))
 def test_unsafe_measurement_blocked(self):
  with self.assertRaises(ValueError):measure(Candidate(240,120),4)
 def test_reproducible_measurement(self):self.assertEqual(measure(candidates()[5],4),measure(candidates()[5],4))
 def test_true_quality_finite(self):self.assertTrue(all(-100<true_quality(c)<150 for c in candidates()))
