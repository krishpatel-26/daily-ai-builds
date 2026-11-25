import unittest
from visionshift.model import LogisticModel,sigmoid
from visionshift.dataset import generate
from visionshift.metrics import classify_metrics
class Tests(unittest.TestCase):
    def test_sigmoid(self):self.assertAlmostEqual(sigmoid(0),.5)
    def test_sigmoid_stable(self):self.assertGreater(sigmoid(1000),.99);self.assertLess(sigmoid(-1000),.01)
    def test_training(self):
        rows=generate(4,260);m=LogisticModel().train(rows)
        self.assertGreater(classify_metrics(m,rows)['accuracy'],.75)
    def test_reproducible(self):self.assertEqual(LogisticModel().train(generate(4,100)).weights,LogisticModel().train(generate(4,100)).weights)
    def test_invalid_features(self):
        with self.assertRaises(ValueError):LogisticModel().predict_proba([1,2])
    def test_empty_train(self):
        with self.assertRaises(ValueError):LogisticModel().train([])
