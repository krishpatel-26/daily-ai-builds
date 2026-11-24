import unittest
from supplychain.experiments import compare_policies,pareto
from supplychain.statistics import summary,paired_delta
class ExperimentTests(unittest.TestCase):
 def test_comparison_three_policies(self):self.assertEqual(len(compare_policies(seeds=(1,2),days=20)),3)
 def test_paired_count(self):self.assertEqual(compare_policies(seeds=(1,2),days=20)[0]['paired_cost_delta_vs_lean']['n'],2)
 def test_pareto(self):
  candidates=[{'policy':'a','cost':{'mean':5},'fill_rate':{'mean':90}}, {'policy':'b','cost':{'mean':6},'fill_rate':{'mean':80}}]
  self.assertEqual(pareto(candidates),['a'])
 def test_empty_samples(self):
  with self.assertRaises(ValueError):summary([])
 def test_mismatched_pairs(self):
  with self.assertRaises(ValueError):paired_delta([1],[1,2])
