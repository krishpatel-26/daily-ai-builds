import unittest
from causalscope.simulator import simulate,STEPS
from causalscope.topology import SERVICES
class SimulationTests(unittest.TestCase):
    def test_deterministic(self):self.assertEqual(simulate(seed=7),simulate(seed=7))
    def test_time_length(self):self.assertEqual(len(simulate()['timeline']),STEPS)
    def test_services_per_step(self):self.assertEqual(set(simulate()['timeline'][0]['metrics']),set(SERVICES))
    def test_decoy_can_be_removed(self):self.assertIsNone(simulate(decoy=False)['decoy_service'])
    def test_invalid_root(self):
        with self.assertRaises(ValueError):simulate(root='unknown')
    def test_invalid_noise(self):
        with self.assertRaises(ValueError):simulate(noise_sd=-1)
    def test_invalid_strength(self):
        with self.assertRaises(ValueError):simulate(strength=21)
