import unittest
from swarmgrid.benchmark import run
class Tests(unittest.TestCase):
 def test_demo(self):
  r=run();self.assertEqual(r["traffic"]["robots"],4);self.assertEqual(r["tasks"],6)
