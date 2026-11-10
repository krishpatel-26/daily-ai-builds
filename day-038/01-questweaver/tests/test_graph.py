import unittest
from app.graph import quest_graph,topological_order
from app.templates import TEMPLATES
class T(unittest.TestCase):
 def test_order(self):
  g=quest_graph(TEMPLATES[0]);self.assertEqual(len(topological_order(g)),3)
 def test_cycle_rejected(self):
  with self.assertRaises(ValueError):topological_order({"nodes":["a","b"],"edges":[{"from":"a","to":"b"},{"from":"b","to":"a"}]})
if __name__=="__main__":unittest.main()