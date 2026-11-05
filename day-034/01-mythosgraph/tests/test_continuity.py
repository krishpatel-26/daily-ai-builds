import unittest
from app.database import init_db
from app.seed import seed
from app.continuity import check
class T(unittest.TestCase):
 @classmethod
 def setUpClass(c):init_db();seed()
 def test_conflict(self):self.assertFalse(check("silver herb","location","frozen desert")["consistent"])
 def test_unknown_not_verified(self):self.assertTrue(check("moon crown","owner","queen")["consistent"])
if __name__=="__main__":unittest.main()