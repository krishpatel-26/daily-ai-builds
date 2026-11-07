import unittest
from app.world import reset
from app.schemas import RumourInput
from app.rumours import create,propagate
class T(unittest.TestCase):
 def test_decay(self):
  s=reset();create(s,RumourInput(source_id="mira",subject_id="player",claim="Player betrayed the village.",confidence=1,audience=["rowan"]));o=propagate(s);self.assertEqual(len(o),1);self.assertLess(o[0]["confidence"],1)
if __name__=="__main__":unittest.main()