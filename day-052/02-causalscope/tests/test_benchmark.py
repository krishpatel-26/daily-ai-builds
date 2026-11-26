import unittest
from causalscope.benchmark import benchmark
from causalscope.report import report
class BenchmarkTests(unittest.TestCase):
    def test_case_count(self):self.assertEqual(benchmark(range(2))['trials'],16)
    def test_model_beats_peak_under_decoy(self):
        r=benchmark(range(3));self.assertGreater(r['root_top1_accuracy'],r['peak_baseline_accuracy'])
    def test_empty_seeds(self):
        with self.assertRaises(ValueError):benchmark([])
    def test_full_report(self):
        r=report(include_benchmark=False);self.assertEqual(r['diagnosis']['most_likely']['service'],'database');self.assertIsNone(r['benchmark'])
    def test_audit_trail(self):self.assertTrue(report(include_benchmark=False)['evidence_trace'])
