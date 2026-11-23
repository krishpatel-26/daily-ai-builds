import unittest
from embodiedbench.world import valid,WALLS,State
class Tests(unittest.TestCase):
 def test_static_wall_rejected(self):self.assertFalse(valid(next(iter(WALLS))))
 def test_start_valid(self):self.assertTrue(valid(State().position))
 def test_state_snapshot(self):self.assertEqual(State().public()['battery'],220)
