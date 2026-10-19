import json
import tempfile
import unittest
from pathlib import Path

from agent_reliability.runner import evaluate_dataset, load_dataset


class RunnerTests(unittest.TestCase):
    def test_report_counts_cases(self):
        cases = [
            {"id": "a", "category": "format", "input": "x", "output": "hello",
             "checks": {"contains_all": ["hello"]}},
            {"id": "b", "category": "format", "input": "y", "output": "world",
             "checks": {"contains_all": ["expected"]}},
        ]
        report = evaluate_dataset(cases)
        self.assertEqual(report["case_count"], 2)
        self.assertEqual(report["passed"], 1)
        self.assertEqual(report["failed"], 1)
        self.assertEqual(report["pass_rate"], 0.5)

    def test_rejects_duplicate_ids(self):
        payload = '{"id":"x","input":"i","output":"o","checks":{}}\n{"id":"x","input":"i","output":"o","checks":{}}\n'
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "dataset.jsonl"
            path.write_text(payload, encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Duplicate case id"):
                load_dataset(path)

    def test_rejects_missing_fields(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "dataset.jsonl"
            path.write_text(json.dumps({"id": "x", "input": "i"}), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "missing required field"):
                load_dataset(path)


if __name__ == "__main__":
    unittest.main()
