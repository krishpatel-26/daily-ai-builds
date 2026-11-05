import unittest,uuid
from app.database import init_db,connect
from app.seed import seed
from app.schemas import EventInput
from app.events import record_event
class T(unittest.TestCase):
 @classmethod
 def setUpClass(c):init_db();seed()
 def test_public_memory(self):
  eid="test-"+uuid.uuid4().hex[:10];e=EventInput(event_id=eid,event_type="discovery",actor_id="player",summary="A comet appeared over the northern ridge.",visibility="public")
  record_event(e)
  with connect() as c:n=c.execute("SELECT COUNT(*) FROM memories WHERE event_id=?",(eid,)).fetchone()[0]
  self.assertGreaterEqual(n,4)
if __name__=="__main__":unittest.main()