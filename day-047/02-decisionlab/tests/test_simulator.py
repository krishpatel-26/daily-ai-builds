import unittest
from decisionlab.simulator import simulate,shocks
from decisionlab.config import Experiment
class SimulationTests(unittest.TestCase):
    def test_seed_deterministic(self):self.assertEqual(simulate(seed=7),simulate(seed=7))
    def test_baseline_produces_units(self):self.assertGreater(simulate()['units_produced'],0)
    def test_invalid_policy(self):
        with self.assertRaises(ValueError):simulate(policy='magic')
    def test_nonnegative_metrics(self):
        r=simulate();self.assertGreaterEqual(r['estimated_cost'],0);self.assertGreaterEqual(r['units_produced'],0)
    def test_bounded_buffers(self):
        r=simulate();self.assertTrue(all(0<=x<=Experiment().buffer_capacity for x in r['buffers']))
    def test_common_random_numbers(self):self.assertEqual(shocks(3,Experiment()),shocks(3,Experiment()))
