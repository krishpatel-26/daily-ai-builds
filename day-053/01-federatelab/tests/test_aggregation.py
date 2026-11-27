import unittest
from federatelab.aggregation import aggregate
class Tests(unittest.TestCase):
 def test_mean(self):self.assertEqual(aggregate([[1,2],[3,4]]),[2.,3.])
 def test_median_rejects_outlier(self):self.assertEqual(aggregate([[1],[1],[1],[1],[999]],'median'),[1])
 def test_trimmed_mean(self):self.assertEqual(aggregate([[1],[1],[1],[1],[100],[200],[300]],'trimmed_mean',2),[34.0])
 def test_trim_reject_small(self):
  with self.assertRaises(ValueError):aggregate([[1],[2],[3]],'trimmed_mean',2)
 def test_bad_method(self):
  with self.assertRaises(ValueError):aggregate([[1]],'magic')
