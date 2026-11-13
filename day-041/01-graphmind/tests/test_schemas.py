import unittest
from app.schemas import TrainRequest,EvaluateRequest
class SchemaTests(unittest.TestCase):
 def test_defaults(self):self.assertEqual(TrainRequest().updates,40)
 def test_invalid_updates(self):
  with self.assertRaises(Exception):TrainRequest(updates=0)
 def test_eval_defaults(self):self.assertTrue(EvaluateRequest().communicate)
if __name__=="__main__":unittest.main()