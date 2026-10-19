# Python evaluation CLI

The repository includes a dependency-free deterministic grader harness.

## Run from the project folder

With Python 3.10 or newer:

```bash
python -m venv .venv
```

Activate the environment, then install the package locally:

```bash
python -m pip install -e .
python -m agent_reliability --dataset data/evaluation_dataset.jsonl --output artifacts/report.json
```

The command prints case count, passing and failing cases, and pass rate. It exits with code 0 if no checks fail, 1 when cases fail, and 2 when the dataset cannot be loaded.

## Run tests

```bash
python -m unittest discover -s tests -p "test_*.py"
```

The graders check configured surface properties. They do not prove answer correctness. Review failure details, tune checks against labeled examples, and test false positives before using a release gate.