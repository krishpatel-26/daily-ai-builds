# CausalScope — Topology-Aware Root-Cause Intelligence Lab

**Day 052/365 · 26 November 2026**. An explainable, reproducible experimental system for diagnosing synthetic cascading incidents in service dependencies.

## Capabilities

- Eight-service directed dependency graph.
- Seeded incident simulator with downstream latency/error propagation and unrelated transient decoy spikes.
- Graph-distance and time-lag response kernels.
- Topology/time-constrained least-squares template matching, with ranked candidate root services and fault onset estimation.
- Naive peak-anomaly root-cause baseline.
- Matched-seed synthetic root-cause benchmark across all service roots.
- Simulator intervention removing the injected fault to estimate modeled anomaly reduction.
- Evidence-trace visualization, interactive graph and local JSON API.
- Automated unit tests for graph reachability, reproducibility, root ranking, negative cases and recovery interpretation.

## Run

Python 3.11+, zero external runtime packages.

```bash
python -m causalscope.server
python -m unittest discover -s tests -v
```

Dashboard: **http://127.0.0.1:4209**. JSON endpoint: `/api/report?root=database&seed=52&strength=2.7`.

## Research integrity

This is **not causal identification on production data**. The scoring model knows the same graph and propagation kernel as the synthetic generator; the comparison primarily tests recovery of simulated latent variables under noise and decoy spikes. A simulator intervention is not a real operational fix. Real distributed incidents involve unknown dependencies, feedback cycles, correlated faults, incomplete traces, load effects, instrumentation problems and changed deployments. The product does not execute remediation commands or claim operational performance.
