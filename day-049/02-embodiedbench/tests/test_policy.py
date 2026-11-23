import unittest
from embodiedbench.world import State
from embodiedbench.policy import validate
from embodiedbench.executor import execute
class Tests(unittest.TestCase):
 def test_invented_object_blocked(self):self.assertEqual(validate(State(),'pick','unicorn')[1],'UNKNOWN_OBJECT')
 def test_illegal_move_unchanged(self):
  s=State();b=s.position;self.assertFalse(execute(s,'move',(10,10))['ok']);self.assertEqual(s.position,b)
 def test_no_teleport(self):self.assertEqual(validate(State(),'move',(5,5))[1],'INVALID_STEP')
 def test_cannot_place_empty_gripper(self):self.assertEqual(validate(State(),'place','zone_a')[1],'NOT_HOLDING')
 def test_forbidden_action(self):self.assertEqual(validate(State(),'destroy_world')[1],'ACTION_NOT_ALLOWED')
