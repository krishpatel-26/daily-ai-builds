import unittest
from app.world import reset
from app.validation import validate
class T(unittest.TestCase):
 def setUp(self):self.s=reset()
 def test_friendly_fire(self):self.assertEqual(validate({"agent_id":"alpha","action":"attack","target":"bravo"},self.s)[1],"friendly_fire_blocked")
 def test_bad_move(self):self.assertFalse(validate({"agent_id":"alpha","action":"move","destination":[9,9]},self.s)[0])
 def test_unknown_agent(self):self.assertFalse(validate({"agent_id":"ghost","action":"rest"},self.s)[0])
if __name__=="__main__":unittest.main()