import unittest
from federatelab.training import train
from federatelab.experiments import compare,benchmark
class Tests(unittest.TestCase):
 def test_training_deterministic(self):self.assertEqual(train(seed=11,rounds=4),train(seed=11,rounds=4))
 def test_accuracy_bounded(self):self.assertTrue(0<=train(rounds=3)['final_accuracy']<=1)
 def test_history(self):self.assertEqual(len(train(rounds=5)['history']),5)
 def test_communication(self):self.assertGreater(train(rounds=4)['communication_kb'],0)
 def test_six_experiments(self):self.assertEqual(len(compare(rounds=2)),6)
 def test_benchmark_rows(self):self.assertEqual(len(benchmark(seeds=(11,12),rounds=2)),6)
 def test_bad_rounds(self):
  with self.assertRaises(ValueError):train(rounds=0)
