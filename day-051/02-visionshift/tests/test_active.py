import unittest
from visionshift.dataset import generate
from visionshift.model import LogisticModel
from visionshift.active import select
class Tests(unittest.TestCase):
    def setUp(self):self.pool=generate(2,30);self.model=LogisticModel()
    def test_reproducible(self):self.assertEqual(select(self.pool,self.model,8,'random',7),select(self.pool,self.model,8,'random',7))
    def test_uncertainty_size(self):self.assertEqual(len(select(self.pool,self.model,9,'uncertainty')),9)
    def test_diversity_unique(self):
        r=select(self.pool,self.model,12,'diversity');self.assertEqual(len(set(x.id for x in r)),12)
    def test_budget_overflow(self):
        with self.assertRaises(ValueError):select(self.pool,self.model,31)
    def test_unknown_strategy(self):
        with self.assertRaises(ValueError):select(self.pool,self.model,2,'unknown')
