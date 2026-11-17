import unittest
from pulsefleet.statistics import median,mad,robust_z
class StatisticsTests(unittest.TestCase):
 def test_median_even(self):self.assertEqual(median([1,3,2,4]),2.5)
 def test_mad(self):self.assertEqual(mad([1,2,3]),1)
 def test_robust_z_short_baseline(self):self.assertEqual(robust_z(9,[1,2]),0)
if __name__=="__main__":unittest.main()
