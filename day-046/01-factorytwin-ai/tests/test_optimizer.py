import unittest
from factorytwin.optimizer import evaluate
from factorytwin.pareto import pareto_front
class Tests(unittest.TestCase):
 def test_six_candidates(self):self.assertEqual(len(evaluate(seeds=(1,))),6)
 def test_pareto(self):self.assertEqual(len(pareto_front([{"mean_cost":1,"mean_completed":10},{"mean_cost":2,"mean_completed":9}])),1)
