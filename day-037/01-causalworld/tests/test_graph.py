import unittest
from app.graph import validate_graph,topological_order
class T(unittest.TestCase):
 def test_dag(self):self.assertTrue(validate_graph()["acyclic"])
 def test_order(self):self.assertEqual(len(topological_order()),8)
if __name__=="__main__":unittest.main()