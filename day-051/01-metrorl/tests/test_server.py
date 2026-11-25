import unittest
from metrorl.report import report
class Tests(unittest.TestCase):
    def test_report_schema(self):
        r=report();self.assertIn('examples',r);self.assertIn('training',r)
    def test_all_policy_metrics(self):
        r=report();self.assertIn('q_learning',r['comparison'])
