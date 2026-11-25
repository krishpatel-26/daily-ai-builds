import unittest
from visionshift.experiment import one_trial,benchmark
from visionshift.report import report
class Tests(unittest.TestCase):
    def test_one_trial(self):self.assertIn('feature_psi',one_trial(3,5))
    def test_benchmark(self):self.assertEqual(benchmark(seeds=(2,3),budget=5)['uncertainty']['trials'],2)
    def test_report(self):self.assertIn('benchmark',report())
