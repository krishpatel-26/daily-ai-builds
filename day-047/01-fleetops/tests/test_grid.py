import unittest
from fleetops.grid import astar,valid,neighbors
class GridTests(unittest.TestCase):
    def test_same_cell(self):self.assertEqual(astar((0,0),(0,0)),[(0,0)])
    def test_obstacle_rejected(self):self.assertEqual(astar((0,0),(4,2)),[])
    def test_valid_path(self):
        route=astar((1,0),(8,10));self.assertTrue(route)
        self.assertTrue(all(valid(p) for p in route))
        self.assertTrue(all(b in neighbors(a) for a,b in zip(route,route[1:])))
