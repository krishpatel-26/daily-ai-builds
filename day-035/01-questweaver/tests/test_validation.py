import unittest
from app.schemas import QuestProposal,Objective
from app.validation import validate
from app.world import reset
def quest(target="marsh"):
 return QuestProposal(quest_id="test-quest",title="Test Quest",giver_id="elder",summary="A test quest with a valid objective.",objectives=[Objective(objective_id="o1",kind="visit",target_id=target,description="Visit the marsh.")])
class T(unittest.TestCase):
 def setUp(self):reset()
 def test_valid_target(self):self.assertTrue(validate(quest())["valid"])
 def test_unknown_target(self):self.assertIn("TARGET_NOT_REGISTERED:unknown",validate(quest("unknown"))["errors"])
 def test_unknown_giver(self):
  q=quest();q.giver_id="ghost";self.assertIn("GIVER_NOT_REGISTERED",validate(q)["errors"])
if __name__=="__main__":unittest.main()