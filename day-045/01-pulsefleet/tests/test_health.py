import unittest
from pulsefleet.simulator import generate_fleet
from pulsefleet.ingestion import group_by_robot
from pulsefleet.health import assess_fleet
class HealthTests(unittest.TestCase):
 def test_six_robots(self):self.assertEqual(len(assess_fleet(group_by_robot(generate_fleet()))),6)
 def test_fault_injection_flagged(self):self.assertTrue(any(x.status=="inspect" for x in assess_fleet(group_by_robot(generate_fleet()))))
if __name__=="__main__":unittest.main()
