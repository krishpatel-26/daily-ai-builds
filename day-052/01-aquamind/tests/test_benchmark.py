import unittest
from aquamind.benchmark import benchmark,noise_sweep
class BenchmarkTests(unittest.TestCase):
    def test_trial_count(self):self.assertEqual(benchmark(range(2))['trials'],18)
    def test_easy_noise_is_identifiable(self):self.assertGreater(benchmark(range(4))['top1_node_accuracy'],.7)
    def test_noisy_accuracy_declines(self):
        levels=noise_sweep((.07,1.0),range(5))
        self.assertGreater(levels[0]['top1_node_accuracy'],levels[1]['top1_node_accuracy'])
    def test_empty_seeds(self):
        with self.assertRaises(ValueError):benchmark([])
