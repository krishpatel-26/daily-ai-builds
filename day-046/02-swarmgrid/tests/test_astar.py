import unittest
from swarmgrid.astar import astar
from swarmgrid.world import valid
class Tests(unittest.TestCase):
 def test_start_goal(self):self.assertEqual(astar((0,0),(0,0)),[(0,0)])
 def test_route_valid(self):self.assertTrue(all(valid(p) for p in astar((0,0),(3,3))))
 def test_blocked_goal(self):self.assertEqual(astar((0,0),(5,3)),[])
