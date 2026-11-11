import unittest
from app.policy import update,choose_action
import random
class T(unittest.TestCase):
 def test_q_update(self):q={};v=update(q,"s","gather",1,"n",.5,.9,True);self.assertEqual(v,.5)
 def test_greedy(self):self.assertEqual(choose_action({"s":{"attack":4}},"s",0,random.Random(1)),"attack")
if __name__=="__main__":unittest.main()