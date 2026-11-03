import unittest
from aegis.metrics import precision_at_k, recall_at_k, reciprocal_rank, ndcg_at_k

class MetricTests(unittest.TestCase):
    def test_perfect_ranking(self):
        ranked, relevant = ["a", "b", "c"], {"a", "b"}
        self.assertAlmostEqual(precision_at_k(ranked, relevant, 2), 1.0)
        self.assertAlmostEqual(recall_at_k(ranked, relevant, 2), 1.0)
        self.assertAlmostEqual(reciprocal_rank(ranked, relevant), 1.0)
        self.assertAlmostEqual(ndcg_at_k(ranked, relevant, 2), 1.0)

    def test_missing_relevant_document(self):
        self.assertEqual(reciprocal_rank(["x", "y"], {"z"}), 0.0)
        self.assertEqual(recall_at_k(["x"], {"z"}, 1), 0.0)

    def test_invalid_k(self):
        with self.assertRaises(ValueError):
            precision_at_k(["a"], {"a"}, 0)

if __name__ == "__main__":
    unittest.main()
