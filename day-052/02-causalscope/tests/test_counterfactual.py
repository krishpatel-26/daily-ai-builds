import unittest
from causalscope.counterfactual import remove_injected_fault
class CounterfactualTests(unittest.TestCase):
    def test_reduced_synthetic_anomaly(self):self.assertGreater(remove_injected_fault()['modeled_reduction'],0)
    def test_reproducibility(self):self.assertEqual(remove_injected_fault(seed=6),remove_injected_fault(seed=6))
    def test_zero_strength(self):self.assertAlmostEqual(remove_injected_fault(strength=0)['modeled_reduction'],0)
