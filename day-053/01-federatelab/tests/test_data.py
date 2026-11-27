import unittest
from federatelab.data import make_dataset
class Tests(unittest.TestCase):
 def test_determinism(self):self.assertEqual(make_dataset(53),make_dataset(53))
 def test_size(self):
  c,t=make_dataset(53);self.assertEqual(len(c),9);self.assertEqual(len(t),700)
 def test_noniid(self):
  c,_=make_dataset(53);a=sum(x[0][0] for x in c[0])/len(c[0]);b=sum(x[0][0] for x in c[4])/len(c[4]);self.assertGreater(abs(a-b),1.0)
 def test_bad_clients(self):
  with self.assertRaises(ValueError):make_dataset(clients=3)
