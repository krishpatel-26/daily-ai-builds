import unittest
from supplychain.scenarios import demand_stream,availability
class ScenarioTests(unittest.TestCase):
 def test_seed_reproducible(self):self.assertEqual(demand_stream(10,70),demand_stream(10,70))
 def test_surge_present(self):
  baseline=demand_stream(10,70,False);disrupted=demand_stream(10,70,True)
  self.assertGreater(sum(disrupted[35].values()),sum(baseline[35].values()))
 def test_disruption_reduces_availability(self):self.assertLess(availability('SOURCE-A',25,True),availability('SOURCE-A',25,False))
 def test_no_disruption(self):self.assertEqual(availability('SOURCE-A',25,False),1)
