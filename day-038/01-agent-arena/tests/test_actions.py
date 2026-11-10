import unittest
from app.world import reset
from app.actions import apply
class T(unittest.TestCase):
 def test_rest(self):
  s=reset();s["agents"]["alpha"]["energy"]=1;apply({"agent_id":"alpha","action":"rest"},s);self.assertEqual(s["agents"]["alpha"]["energy"],4)
 def test_attack(self):
  s=reset();r=apply({"agent_id":"alpha","action":"attack","target":"cinder"},s);self.assertEqual(r["target_hp"],7)
if __name__=="__main__":unittest.main()