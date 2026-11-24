import unittest
from supplychain.simulator import simulate
class SimulationTests(unittest.TestCase):
 def test_reproducibility(self):self.assertEqual(simulate(seed=7),simulate(seed=7))
 def test_different_seeds(self):self.assertNotEqual(simulate(seed=7)['trace'],simulate(seed=8)['trace'])
 def test_invalid_policy(self):
  with self.assertRaises(ValueError):simulate(policy='unknown')
 def test_invalid_days(self):
  with self.assertRaises(ValueError):simulate(days=0)
 def test_accounting(self):
  for p in ('lean','diversified','resilient'):
   r=simulate(p,seed=33)
   self.assertEqual(r['metrics']['demand_units'],r['metrics']['sold_units']+r['metrics']['lost_sales_units'])
 def test_service_rate(self):
  for p in ('lean','diversified','resilient'):
   r=simulate(p)
   self.assertTrue(0<=r['metrics']['fill_rate_pct']<=100)
 def test_resilience_fills_more_in_demo(self):
  self.assertGreater(simulate('resilient')['metrics']['fill_rate_pct'],simulate('lean')['metrics']['fill_rate_pct'])
 def test_nonnegative_costs(self):self.assertGreaterEqual(simulate()['metrics']['estimated_cost'],0)
