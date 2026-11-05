import unittest
from app.database import init_db
from app.seed import seed
from app.relationships import update,sentiment
class T(unittest.TestCase):
 @classmethod
 def setUpClass(c):init_db();seed()
 def test_clamp(self):self.assertEqual(update("mira","player",1000,"test clamp")["score"],100)
 def test_sentiment(self):self.assertEqual(sentiment(-70),"hostile")
if __name__=="__main__":unittest.main()