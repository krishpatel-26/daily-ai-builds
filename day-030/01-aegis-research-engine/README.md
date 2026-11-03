# AEGIS — Autonomous AI Research & Discovery Engine

**Day 030 / Daily AI Builds**

AEGIS is a reproducible AI experimentation workbench. It compares retrieval strategies under controlled conditions, applies distribution-shift stress tests, measures ranking quality, estimates uncertainty with bootstrap confidence intervals, tests paired differences, and writes an evidence-backed research report.

> Research prototype, not an autonomous scientist that can validate arbitrary scientific claims. The included benchmark is synthetic and deliberately transparent.

## Research question

Does a hybrid lexical retriever (BM25 + TF-IDF) improve retrieval quality and robustness over either component alone when queries are perturbed?

## What it does
- Runs BM25, TF-IDF, and hybrid retrieval on the same benchmark.
- Evaluates clean, typo, paraphrase-proxy, and distractor-heavy conditions.
- Reports Precision@K, Recall@K, MRR, and nDCG@K.
- Computes bootstrap confidence intervals for aggregate metrics.
- Uses paired randomization tests for per-query comparisons.
- Runs ablations and records configuration, seed, dataset fingerprint, and runtime.
- Emits machine-readable JSON plus a Markdown research report.

## Quick start
Requires Python 3.10+; standard library only.

```bash
python -m aegis run --seed 42 --bootstrap 500
python -m aegis run --seed 42 --bootstrap 500 --output artifacts
python -m unittest discover -s tests -v
```

## Architecture
- `aegis/data.py`: deterministic benchmark and stress transformations
- `aegis/retrieval.py`: BM25, TF-IDF, and hybrid rankers
- `aegis/metrics.py`: ranking metrics
- `aegis/statistics.py`: bootstrap intervals and paired randomization
- `aegis/experiment.py`: controlled experiment orchestration
- `aegis/report.py`: reproducibility manifest and research report
- `aegis/cli.py`: command-line interface

## Interpretation guardrails
- Synthetic benchmark results do not establish production superiority.
- Paraphrase-proxy and typo transforms are controlled stressors, not natural language understanding tests.
- Statistical significance is not practical significance.
- Confidence intervals quantify resampling uncertainty on this benchmark; they do not cover dataset bias.
- The hybrid weight is a tunable parameter, not a universally optimal setting.

## Research extensions
Add real datasets with licenses, dense embedding retrieval, cross-encoder reranking, LLM-as-judge with human calibration, temporal drift, cost/latency budgets, and preregistered hypotheses.

## License
MIT
