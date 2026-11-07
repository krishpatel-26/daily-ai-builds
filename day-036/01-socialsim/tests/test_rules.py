import unittest
from app.world import reset
from app.relationship import apply_delta
from app.rules import evaluate
class T(unittest.TestCase):
 def test_distrust(self):
  s=reset();apply_delta(s,"mira","player",{"trust":-60});self.assertTrue(any(x["rule"]=="trust" for x in evaluate(s)))
if __name__=="__main__":unittest.main()