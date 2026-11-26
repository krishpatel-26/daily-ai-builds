import unittest
from causalscope.signals import aggregate,total_anomaly,peak_baseline
from causalscope.simulator import simulate
class SignalsTests(unittest.TestCase):
    def test_aggregate_length(self):self.assertEqual(len(aggregate(simulate()['timeline'])['database']),45)
    def test_no_fault_less_aggregate_anomaly(self):
        self.assertGreater(total_anomaly(simulate(strength=3)['timeline']),total_anomaly(simulate(strength=0)['timeline']))
    def test_peak_exists(self):self.assertIsInstance(peak_baseline(simulate()['timeline']),str)
