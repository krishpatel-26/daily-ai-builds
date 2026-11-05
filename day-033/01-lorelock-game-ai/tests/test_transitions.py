import unittest
from app import world,runtime
from app.schemas import ActionProposal
class Tests(unittest.TestCase):
 def setUp(self):world.reset();runtime.clear()
 def test_potion_consumed(self):
  p=ActionProposal(request_id="heal-001",actor_id="player",action="use_item",item_id="healing_potion")
  self.assertTrue(runtime.execute(p)["executed"]);self.assertNotIn("healing_potion",world.STATE["actors"]["player"]["inventory"])
if __name__=="__main__":unittest.main()