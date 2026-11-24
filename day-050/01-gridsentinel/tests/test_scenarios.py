import unittest
from gridsentinel.scenarios import run,compare_outages
from gridsentinel.report import report

class TestScenarios(unittest.TestCase):
    def test_unknown_line(self):
        with self.assertRaises(ValueError):run('UNKNOWN')
    def test_unknown_strategy(self):
        with self.assertRaises(ValueError):run(None,'magic')
    def test_all_strategies(self):
        rows=compare_outages();self.assertEqual(len(rows),4)
        self.assertTrue(all(r['outages']==12 for r in rows))
    def test_report_comparisons(self):self.assertEqual(len(report()['comparisons']),4)
    def test_repeatable(self):self.assertEqual(report('backup','L04'),report('backup','L04'))
