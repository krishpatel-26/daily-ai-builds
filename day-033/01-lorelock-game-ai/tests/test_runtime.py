import unittest
from app import world,runtime
from app.mock_agent import propose
class Tests(unittest.TestCase):
 def setUp(self):world.reset();runtime.clear()
 def test_invalid_no_mutation(self):
  before=world.snapshot();self.assertFalse(runtime.execute(propose("hallucinated"))["executed"]);self.assertEqual(before,world.snapshot())
 def test_idempotent(self):
  p=propose("safe");runtime.execute(p);r=runtime.execute(p);self.assertTrue(r["idempotent_replay"]);self.assertEqual(len(world.STATE["event_log"]),1)
if __name__=="__main__":unittest.main()