import unittest
from app.returns import gae
class T(unittest.TestCase):
 def test_shapes(self):a,r=gae([1,1],[0,0],[0,1]);self.assertEqual(a.shape,(2,));self.assertEqual(r.shape,(2,))
 def test_terminal(self):self.assertAlmostEqual(float(gae([1],[0],[1])[0][0]),1)
if __name__=="__main__":unittest.main()