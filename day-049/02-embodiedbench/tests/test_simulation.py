import unittest
from embodiedbench.simulator import Simulator
from embodiedbench.benchmark import compare
class Tests(unittest.TestCase):
 def test_deterministic(self):self.assertEqual(Simulator().run(),Simulator().run())
 def test_all_tasks_complete(self):self.assertEqual(Simulator().run()['metrics']['completed_tasks'],3)
 def test_dynamic_obstacle_replan(self):
  result=Simulator().run();self.assertGreaterEqual(result['metrics']['replans'],1)
 def test_no_obstacle_intersection(self):
  result=Simulator().run();walls={tuple(p) for p in result['world']['static_obstacles']}
  for frame in result['frames']:
   p=tuple(frame['state']['position']);dynamic={tuple(x) for x in frame['state']['dynamic_obstacles']}
   self.assertNotIn(p,walls|dynamic)
 def test_comparison(self):self.assertEqual(len(compare()),4)
 def test_policy_difference(self):self.assertNotEqual(Simulator(fault=False).run()['fault_injection'],Simulator().run()['fault_injection'])
