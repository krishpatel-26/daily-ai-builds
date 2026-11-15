import unittest
from app.risk import classify,risk_index
class T(unittest.TestCase):
 def test_bands(self):self.assertEqual(classify(.8),"HIGH");self.assertEqual(classify(.5),"MEDIUM");self.assertEqual(classify(.1),"LOW")
 def test_bound(self):self.assertLessEqual(risk_index(2,4,1),1)
if __name__=="__main__":unittest.main()