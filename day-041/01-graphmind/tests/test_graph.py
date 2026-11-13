import unittest
from app.environment import CorridorEnv
from app.graph import build_adjacency,edge_count
class GraphTests(unittest.TestCase):
 def test_self_loops(self):self.assertTrue((build_adjacency(CorridorEnv().reset()).diagonal()==1).all())
 def test_symmetric(self):
  a=build_adjacency(CorridorEnv().reset());self.assertTrue((a==a.T).all())
 def test_edge_count(self):self.assertGreaterEqual(edge_count(build_adjacency(CorridorEnv().reset())),0)
if __name__=="__main__":unittest.main()