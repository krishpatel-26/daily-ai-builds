import unittest
from crisismesh.routing import route
from crisismesh.world import make_scenario
class RoutingTests(unittest.TestCase):
 def test_same_point(self):self.assertEqual(route([[0,0]],(0,0),(0,0))['steps'],0)
 def test_blocks_unsafe_flood(self):self.assertIsNone(route([[0,4,0]],(0,0),(2,0),1))
 def test_detours_around_flood(self):
  grid=[[0,4,0],[0,0,0]];r=route(grid,(0,0),(2,0),1);self.assertEqual(r['steps'],4)
  self.assertTrue(all(grid[y][x]<=1 for x,y in r['path']))
 def test_deterministic(self):
  s=make_scenario(48);self.assertEqual(route(s['water'],s['base'],(8,8)),route(s['water'],s['base'],(8,8)))
 def test_policy_validation(self):
  with self.assertRaises(ValueError):route([[0]],(0,0),(0,0),policy='magic')