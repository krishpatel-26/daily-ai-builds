import unittest
from federatelab.mathops import sigmoid,predict,accuracy,log_loss
class Tests(unittest.TestCase):
 def test_sigmoid_stability(self):self.assertGreater(sigmoid(1000),.999);self.assertLess(sigmoid(-1000),.001)
 def test_accuracy(self):self.assertEqual(accuracy([1,0,0],[((2,0),1),((-2,0),0)]),1)
 def test_finite_loss(self):self.assertGreaterEqual(log_loss([10,0,0],[((1,0),1)]),0)
 def test_empty_eval(self):
  with self.assertRaises(ValueError):accuracy([0,0,0],[])
