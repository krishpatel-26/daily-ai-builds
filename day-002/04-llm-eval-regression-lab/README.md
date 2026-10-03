# LLM Evaluation and Regression Lab

Local evaluation harness for testing prompt changes against a fixed dataset before shipping them.

Providers share one interface. The included mock provider needs no API key. Evaluations measure keyword coverage and enforce a regression threshold.

Run: pip install -r requirements.txt && python -m app.cli && pytest -q