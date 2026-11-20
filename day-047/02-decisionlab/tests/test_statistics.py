import unittest
from decisionlab.statistics import summarize,paired_difference
class StatisticsTests(unittest.TestCase):
    def test_constant_ci(self):self.assertEqual(summarize([5,5,5])['ci95_normal_approx'],[5,5])
    def test_paired(self):self.assertEqual(paired_difference([4,5],[2,3])['mean'],2)
    def test_mismatched_pairs(self):
        with self.assertRaises(ValueError):paired_difference([1],[1,2])
