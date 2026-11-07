import unittest
from app.world import reset
from app.engine import tick
class T(unittest.TestCase):
 def test_ticks(self):reset();r=tick(2);self.assertEqual(r[-1]["tick"],2)
if __name__=="__main__":unittest.main()