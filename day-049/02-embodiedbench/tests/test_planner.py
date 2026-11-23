import unittest
from embodiedbench.world import State,WALLS,ITEMS,ZONES
from embodiedbench.pathfinding import astar
from embodiedbench.planner import choose_task
from embodiedbench.intent import sample_tasks
class Tests(unittest.TestCase):
 def test_route_avoids_walls(self):
  path=astar((1,1),(13,3));self.assertTrue(path);self.assertTrue(all(p not in WALLS for p in path))
 def test_blocked_goal(self):self.assertIsNone(astar((1,1),next(iter(WALLS))))
 def test_task_choice(self):self.assertIsNotNone(choose_task(State(),sample_tasks()))
 def test_invalid_strategy(self):
  with self.assertRaises(ValueError):choose_task(State(),sample_tasks(),'magic')
