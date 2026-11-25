import unittest
from visionshift.drift import psi,feature_drift
from visionshift.dataset import generate
class Tests(unittest.TestCase):
    def test_identical_psi_zero(self):
        data=list(range(100));self.assertAlmostEqual(psi(data,data),0)
    def test_shift_increases_psi(self):
        ref=list(range(100));self.assertGreater(psi(ref,[x+40 for x in ref]),psi(ref,ref))
    def test_feature_names(self):
        d=feature_drift(generate(1,70),generate(2,70,1.0));self.assertEqual(len(d),4)
    def test_bad_input(self):
        with self.assertRaises(ValueError):psi([1],[])
