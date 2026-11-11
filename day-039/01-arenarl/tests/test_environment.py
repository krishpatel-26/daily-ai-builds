import unittest
from app.environment import reset,step
class T(unittest.TestCase):
 def test_turn_advances(self):s=reset();s,_,_=step(s,{"blue":"rest","red":"rest"});self.assertEqual(s["step"],1)
 def test_resource_gathered(self):s=reset();s["players"]["blue"].pos=2;s,rew,_=step(s,{"blue":"gather","red":"rest"});self.assertEqual(s["players"]["blue"].score,2);self.assertGreater(rew["blue"],0)
 def test_terminal_after_resources(self):s=reset();s["resources"]={};s,_,done=step(s,{"blue":"rest","red":"rest"});self.assertTrue(done)
if __name__=="__main__":unittest.main()