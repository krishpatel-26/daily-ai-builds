import unittest
from app.world import reset
from app.schemas import SocialAction
from app.actions import process
class T(unittest.TestCase):
 def setUp(self):self.s=reset()
 def test_betrayal(self):
  b=self.s["relationships"]["mira->player"]["trust"];process(self.s,SocialAction(actor_id="mira",target_id="player",action="betray"));self.assertLess(self.s["relationships"]["mira->player"]["trust"],b)
 def test_unknown(self):
  with self.assertRaises(ValueError):process(self.s,SocialAction(actor_id="ghost",target_id="player",action="help"))
if __name__=="__main__":unittest.main()