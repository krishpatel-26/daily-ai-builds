import unittest
from fleetops.benchmark import compare
class BenchmarkTests(unittest.TestCase):
    def test_returns_two_conditions(self):
        rows=compare(seeds=(1,2),ticks=50)
        self.assertEqual(len(rows),2);self.assertEqual(rows[0]['trials'],2)
        self.assertFalse(rows[0]['faults_enabled']);self.assertTrue(rows[1]['faults_enabled'])
