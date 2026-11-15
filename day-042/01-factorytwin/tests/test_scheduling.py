import unittest
from app.scheduling import prioritize
class T(unittest.TestCase):
 def test_capacity(self):
  x=prioritize([{"priority":5,"duration_hours":4,"risk_score":.8},{"priority":2,"duration_hours":6,"risk_score":.2}],8);self.assertLessEqual(x["hours_used"],8)
 def test_defer(self):self.assertEqual(len(prioritize([{"priority":1,"duration_hours":9,"risk_score":.1}],8)["deferred"]),1)
if __name__=="__main__":unittest.main()