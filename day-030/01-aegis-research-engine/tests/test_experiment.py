import unittest
from aegis.experiment import run_experiment

class ExperimentTests(unittest.TestCase):
    def test_scenarios_and_manifest(self):
        result = run_experiment(seed=7, bootstrap_samples=30)
        self.assertEqual(set(result["results"]), {"clean", "typo", "paraphrase_proxy", "distractor_heavy"})
        self.assertEqual(result["manifest"]["seed"], 7)
        self.assertEqual(len(result["manifest"]["dataset_sha256"]), 64)

    def test_deterministic_metrics(self):
        a = run_experiment(seed=11, bootstrap_samples=25)
        b = run_experiment(seed=11, bootstrap_samples=25)
        self.assertEqual(a["results"], b["results"])

if __name__ == "__main__":
    unittest.main()
