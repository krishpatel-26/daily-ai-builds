import unittest
from genesislab.experiments import run_trial
from genesislab.benchmark import benchmark
class Tests(unittest.TestCase):
 def test_seed_determinism(self):self.assertEqual(run_trial(49,9),run_trial(49,9))
 def test_unique_experiments(self):
  h=run_trial(49,12)['history'];self.assertEqual(len({(x['parameters']['temperature'],x['parameters']['speed']) for x in h}),len(h))
 def test_best_monotonic(self):
  values=[x['best_quality'] for x in run_trial(49,12)['history']];self.assertEqual(values,sorted(values))
 def test_budget_enforced(self):
  with self.assertRaises(ValueError):run_trial(49,3)
 def test_invalid_policy(self):
  with self.assertRaises(ValueError):run_trial(49,6,'fiction')
 def test_benchmark(self):
  b=benchmark(range(3),8);self.assertEqual(b['paired_seed_count'],3)
 def test_same_initial_observations(self):
  a=run_trial(2,8,'adaptive')['history'][:3];b=run_trial(2,8,'random')['history'][:3];self.assertEqual(a,b)
