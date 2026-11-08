import unittest
from app.engine import explain
class T(unittest.TestCase):
 def test_paths(self):self.assertTrue(explain("regional_stability")["root_paths"])
 def test_unknown(self):
  with self.assertRaises(ValueError):explain("nope")
if __name__=="__main__":unittest.main()