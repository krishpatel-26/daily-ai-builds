import unittest
from app.anomaly import robust_z,anomaly_signals
class AnomalyTests(unittest.TestCase):
 def test_mad_detects_outlier(self):
  self.assertGreater(abs(robust_z(100,[10,11,10,9,10,11,10])),3.5)
 def test_limit_signal(self):
  asset={"temperature_limit":80,"vibration_limit":7,"pressure_min":2,"pressure_max":8}
  rows=[{"temperature":95,"vibration":2,"pressure":5,"current":4,"rpm":1000}]
  result=anomaly_signals(rows,asset)
  self.assertTrue(any(s["code"]=="TEMP_LIMIT" for s in result["signals"]))
if __name__=="__main__":unittest.main()