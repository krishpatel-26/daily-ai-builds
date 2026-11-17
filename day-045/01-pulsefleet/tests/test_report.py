import unittest
from pulsefleet.report import fleet_report
class ReportTests(unittest.TestCase):
 def test_empty_report(self):
  r=fleet_report([]);self.assertEqual(r["fleet_size"],0);self.assertEqual(r["average_health"],0)
if __name__=="__main__":unittest.main()
