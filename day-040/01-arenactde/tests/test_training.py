import unittest
from app.trainer import train
class T(unittest.TestCase):
 def test_history(self):self.assertEqual(len(train(2)["history"]),2)
if __name__=="__main__":unittest.main()