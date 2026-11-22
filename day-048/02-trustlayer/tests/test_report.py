import unittest
from trustlayer.report import demo
class ReportTests(unittest.TestCase):
 def test_expected_cases(self):self.assertEqual(demo()['metrics']['proposals'],9)
 def test_rejects_more_than_accepts(self):
  m=demo()['metrics'];self.assertGreater(m['rejected'],m['validated'])
 def test_ledger_integrity(self):self.assertTrue(demo()['metrics']['ledger_integrity'])