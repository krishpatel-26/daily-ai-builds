import unittest
from crisismesh.experiment import compare,benchmark
class ExperimentTests(unittest.TestCase):
 def test_repeatable(self):self.assertEqual(compare(48),compare(48))
 def test_policies_present(self):self.assertEqual(set(compare()['policies']),{'shortest','risk_aware'})
 def test_benchmark_size(self):self.assertTrue(all(row['seeds']==2 for row in benchmark(range(1,3))))