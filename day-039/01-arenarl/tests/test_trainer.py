import unittest
from app.trainer import train
class T(unittest.TestCase):
 def test_reproducible(self):
  a=train(4,seed=9);b=train(4,seed=9);self.assertEqual(a["history"],b["history"])
 def test_table_created(self):self.assertIn("blue",train(2)["q_tables"])
if __name__=="__main__":unittest.main()