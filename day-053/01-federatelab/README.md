# FederateLab — Federated Learning & Poisoning Resilience Research

**Day 053/365 · 27 November 2026**

A dependency-free, runnable federated logistic-regression workbench demonstrating non-IID client data, local training, FedAvg, coordinate median, trimmed-mean aggregation, malicious client updates, held-out evaluation and communication accounting.

## Run

Python 3.11+ only. No tokens, packages or remote ML APIs.

```bash
python -m federatelab.server
python -m unittest discover -s tests -v
```

Dashboard: http://127.0.0.1:4210 . Report API: `/api/report?seed=53&rounds=18&attack=on`.

## What is measured

All methods start with the same weights and use reproducible client datasets and deterministic minibatches. Accuracy is measured on an independent synthetic held-out set. Robust methods are compared with standard FedAvg with and without Byzantine-style update inversion. Results are only about this small 2D simulation.

## Privacy and security boundary

Despite the name, **this is not a privacy-preserving training system**. It does not use secure aggregation, differential privacy, encrypted transport, authenticated clients or protection against model inversion. Coordinate median/trimmed mean are heuristic defenses, not poisoning-proof or Byzantine guarantees. The default mode shares raw model deltas with the server, and no real personal data should be used.
