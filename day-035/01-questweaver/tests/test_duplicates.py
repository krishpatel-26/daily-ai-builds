import unittest
from app.duplicates import duplicate_check
from app.schemas import QuestProposal,Objective
class T(unittest.TestCase):
 def test_duplicate_id(self):
  q=QuestProposal(quest_id="q1",title="A Quest",giver_id="elder",summary="A sufficiently long summary.",objectives=[Objective(objective_id="o",kind="visit",target_id="marsh",description="Visit marsh.")])
  self.assertTrue(duplicate_check(q,[{"quest_id":"q1","objectives":[]}],[])["duplicate"])
if __name__=="__main__":unittest.main()