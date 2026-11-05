import unittest
from app import world
from app.schemas import ActionProposal
from app.validation import validate
class Tests(unittest.TestCase):
 def setUp(self):world.reset()
 def p(self,**kw):
  d={"request_id":"test-001","actor_id":"player","action":"talk","target_id":"elder"};d.update(kw);return ActionProposal(**d)
 def test_valid_talk(self):self.assertTrue(validate(self.p())["valid"])
 def test_fake_quest(self):self.assertEqual(validate(self.p(action="start_quest",target_id="fake"))["reason_code"],"QUEST_NOT_FOUND")
 def test_out_of_range(self):self.assertEqual(validate(self.p(action="attack",target_id="goblin"))["reason_code"],"OUT_OF_RANGE")
 def test_fake_item(self):self.assertEqual(validate(self.p(action="use_item",target_id=None,item_id="fake"))["reason_code"],"ITEM_NOT_FOUND")
 def test_extra_field(self):
  with self.assertRaises(Exception):ActionProposal(request_id="test-002",actor_id="player",action="talk",target_id="elder",script="exec")
if __name__=="__main__":unittest.main()