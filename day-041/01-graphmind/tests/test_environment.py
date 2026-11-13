import unittest
from app.environment import CorridorEnv
class EnvTests(unittest.TestCase):
 def test_observation_shape(self):self.assertEqual(CorridorEnv().reset().shape,(4,6))
 def test_step_contract(self):
  e=CorridorEnv();e.reset();o,r,d,i=e.step([1,1,1,1]);self.assertEqual(o.shape,(4,6));self.assertEqual(r.shape,(4,));self.assertIsInstance(d,bool)
if __name__=="__main__":unittest.main()