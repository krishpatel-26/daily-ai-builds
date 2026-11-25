import unittest
from visionshift.monitor import monitor
from visionshift.dataset import generate
class Tests(unittest.TestCase):
 def test_monitor_labels(self):
  m=monitor(generate(1,100),generate(2,100,1))
  self.assertTrue(all(x['level'] in ('stable','watch','investigate') for x in m['features'].values()))
 def test_bad_thresholds(self):
  with self.assertRaises(ValueError):monitor(generate(1,20),generate(2,20),watch=.7,investigate=.4)
