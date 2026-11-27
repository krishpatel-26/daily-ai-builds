import unittest
from federatelab.attack import poison
from federatelab.report import build
from federatelab.local import train_local
class Tests(unittest.TestCase):
 def test_poison(self):self.assertEqual(poison([1,-2],3),[-3,6])
 def test_invalid_scale(self):
  with self.assertRaises(ValueError):poison([1],0)
 def test_heldout_disclosed(self):self.assertIn('Synthetic',build(rounds=2)['disclaimer'])
 def test_seed_reject(self):
  with self.assertRaises(ValueError):build(seed=-1,rounds=1)
 def test_train_invalid(self):
  with self.assertRaises(ValueError):train_local([0,0,0],[],1,.1)
