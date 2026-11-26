import unittest
from causalscope.kernel import effect,shape
class KernelTests(unittest.TestCase):
    def test_no_preincident_signal(self):self.assertEqual(effect(0,5,12),0)
    def test_delayed_hop(self):self.assertEqual(effect(2,14,12),0)
    def test_positive_after_onset(self):self.assertGreater(effect(0,15,12),0)
    def test_decay_per_hop(self):self.assertLess(effect(2,20,12),effect(0,20,12))
    def test_bad_distance(self):
        with self.assertRaises(ValueError):effect(-1,10,10)
