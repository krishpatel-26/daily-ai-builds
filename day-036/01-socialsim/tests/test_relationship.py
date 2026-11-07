import unittest
from app.world import reset
from app.relationship import apply_delta,get
class T(unittest.TestCase):
 def setUp(self):self.s=reset()
 def test_clamp(self):self.assertEqual(apply_delta(self.s,"mira","player",{"trust":999})["trust"],100)
 def test_directed(self):apply_delta(self.s,"mira","player",{"trust":20});self.assertNotEqual(get(self.s,"mira","player")["trust"],get(self.s,"player","mira")["trust"])
if __name__=="__main__":unittest.main()