import unittest
from app.health import assess
class HealthTests(unittest.TestCase):
 def setUp(self):self.asset={"asset_id":"A1","temperature_limit":85,"vibration_limit":7.1,"pressure_min":1,"pressure_max":10}
 def test_no_data(self):self.assertEqual(assess(self.asset,[])["status"],"no_data")
 def test_explainable_output(self):
  rows=[{"temperature":60,"vibration":2,"pressure":5,"current":4,"rpm":1500,"runtime_hours":100+i} for i in range(8)]
  result=assess(self.asset,rows);self.assertIn("health_index",result);self.assertIn("reasons",result);self.assertIn("features",result)
if __name__=="__main__":unittest.main()