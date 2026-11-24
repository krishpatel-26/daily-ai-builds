# SupplyChainOS — Disruption-Aware Supply Network Simulator

**Day 050/365 · Research project 2**

A local-first, Python-standard-library simulator for a three-tier supply network with two suppliers, two distribution hubs and four downstream outlets. It compares lean single sourcing, diversified sourcing and resilience buffers under synthetic primary supplier disruption and demand surges, using matched random seeds.

## Quickstart

Requires Python 3.11+; no external dependencies.

```bash
cd day-050/02-supplychainos
python -m supplychain.api
# Open http://127.0.0.1:4205
```

Tests: `python -m unittest discover -s tests -v`.

## Engineering highlights
- Multi-echelon inventory conservation, finite supplier capacity and explicit inbound/outbound pipeline lead times.
- Priority-aware replenishment of clinic/pharmacy outlets before general retail.
- Synthetic stochastic daily demand, supplier availability disruption and demand surge.
- Policy-specific safety stocks and alternate sourcing, with daily inventory tracking and fulfillment trace.
- Multi-seed paired experiments, normal-approximation confidence intervals and Pareto cost/service tradeoffs.
- Interactive demand vs fulfillment visualization, policy benchmark and local read-only JSON API.

## Important limitations
This is **not** a trained AI forecasting system, ERP, inventory optimizer, validated supply-chain forecast or clinical inventory allocation system. The outlets, lead times, supplier costs, demand and disruptions are entirely fictional. Medical-related outlet names do not imply medication guidance or healthcare suitability. Procurement uses simple heuristics, not an optimal mathematical program; shortages are modeled as lost sales, not backorders. Costs use arbitrary demo units. Results are scenario-specific and **must not be used for real inventory or healthcare decisions**.
