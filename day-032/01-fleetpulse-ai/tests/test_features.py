import unittest
from app.features import rolling_features
class FeatureTests(unittest.TestCase):
 def test_trend_and_latest(self):
  rows=[{"temperature":v,"vibration":2,"pressure":4,"current":8,"rpm":1500,"runtime_hours":i} for i,v in enumerate([10,11,12,13])]
  result=rolling_features(rows)
  self.assertEqual(result["metrics"]["temperature"]["latest"],13)
  self.assertGreater(result["metrics"]["temperature"]["slope"],0)
if __name__=="__main__":unittest.main()