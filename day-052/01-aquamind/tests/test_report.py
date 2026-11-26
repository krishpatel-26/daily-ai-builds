import unittest
from aquamind.report import report
class ReportTests(unittest.TestCase):
    def test_full_report(self):
        r=report();self.assertEqual(r['scenario']['leak_node'],'J-07');self.assertEqual(len(r['noise_sweep']),4)
    def test_without_benchmark(self):
        r=report(include_benchmark=False);self.assertIsNone(r['benchmark']);self.assertIsNone(r['noise_sweep'])
