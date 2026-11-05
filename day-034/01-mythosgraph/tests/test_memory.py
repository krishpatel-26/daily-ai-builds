import unittest
from app.database import init_db,connect
from app.seed import seed
from app.memory import recall
class T(unittest.TestCase):
 @classmethod
 def setUpClass(c):init_db();seed()
 def test_witness_memory(self):self.assertTrue(any(x["event_id"]=="evt-002" for x in recall("mira","silver herb promise")))
 def test_private_memory_scoped(self):
  with connect() as c:r=c.execute("SELECT 1 FROM memories WHERE character_id='rowan' AND event_id='evt-002'").fetchone()
  self.assertIsNone(r)
if __name__=="__main__":unittest.main()