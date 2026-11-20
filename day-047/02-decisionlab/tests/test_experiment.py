import unittest
from decisionlab.experiment import compare
class ExperimentTests(unittest.TestCase):
    def test_five_policies(self):self.assertEqual(len(compare(seeds=(1,2))),5)
    def test_sorted_by_mean_cost(self):
        r=compare(seeds=(1,2));self.assertEqual([x['cost']['mean'] for x in r],sorted(x['cost']['mean'] for x in r))
    def test_paired_counts(self):self.assertEqual(compare(seeds=(1,2))[0]['paired_cost_delta_vs_reactive']['n'],2)
