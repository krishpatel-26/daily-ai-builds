import unittest
from app.environment import CoopGrid
class T(unittest.TestCase):
 def test_shapes(self):o,s=CoopGrid().reset();self.assertEqual(o.shape,(2,6));self.assertEqual(s.shape,(14,))
 def test_goal(self):e=CoopGrid();e.reset();e.pos[:]=e.goal;_,_,r,d,i=e.step([3,3]);self.assertTrue(d);self.assertTrue(i["success"]);self.assertTrue((r>0).all())
if __name__=="__main__":unittest.main()