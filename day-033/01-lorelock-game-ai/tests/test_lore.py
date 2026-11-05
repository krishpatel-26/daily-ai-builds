import unittest
from app.lore import ground
from app import world
class Tests(unittest.TestCase):
 def setUp(self):world.reset()
 def test_known_fact(self):self.assertTrue(ground("What does healing potion do?")["grounded"])
 def test_unknown_fact(self):self.assertFalse(ground("Who rules moon empire?")["grounded"])
if __name__=="__main__":unittest.main()