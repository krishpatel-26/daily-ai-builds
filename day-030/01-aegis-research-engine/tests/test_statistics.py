import unittest
from aegis.statistics import bootstrap_ci, paired_randomization

class StatisticsTests(unittest.TestCase):
    def test_bootstrap_is_reproducible(self):
        a = bootstrap_ci([1, 2, 3], 200, seed=9)
        b = bootstrap_ci([1, 2, 3], 200, seed=9)
        self.assertEqual(a, b)
        self.assertLessEqual(a["lower"], a["mean"])
        self.assertGreaterEqual(a["upper"], a["mean"])

    def test_identical_pairs(self):
        result = paired_randomization([1, 0, 1], [1, 0, 1], 100, seed=1)
        self.assertEqual(result["mean_difference"], 0)
        self.assertEqual(result["p_value"], 1)

    def test_pair_validation(self):
        with self.assertRaises(ValueError):
            paired_randomization([1], [], 10)

if __name__ == "__main__":
    unittest.main()
