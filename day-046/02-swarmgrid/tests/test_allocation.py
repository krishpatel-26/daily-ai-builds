import unittest
from swarmgrid.world import demo
from swarmgrid.allocator import assign
class Tests(unittest.TestCase):
 def test_all_tasks_assigned(self):
  robots,tasks=demo();a,pending=assign(robots,tasks);self.assertEqual(sum(map(len,a.values()))+len(pending),len(tasks))
