# GridSentinel — Power-Grid Resilience Research Lab

**Day 050/365 · Research project 1**

A Python-standard-library, locally runnable educational power-network simulator for N−1 line outage experiments, simplified DC power flow, islanding, critical-load service, corridor reinforcement and backup generation. Includes an interactive SVG dashboard, a JSON API, and reproducible unit tests.

## Quickstart

Requires Python 3.11+; no pip install.

```bash
cd day-050/01-gridsentinel
python -m gridsentinel.api
# Open http://127.0.0.1:4204
```

Tests: `python -m unittest discover -s tests -v`.

## What it does
- Models eight synthetic buses, 12 transmission corridors, and a deliberately generation-constrained stress scenario.
- Splits the network into electrical islands after any corridor outage.
- Calculates balanced injection schedules, prioritizing critical loads when generation is insufficient.
- Solves DC power flow with partial-pivot Gaussian elimination and reports line thermal utilization.
- Benchmarks all 12 single-line outages across baseline, backup, reinforcement and combined scenarios.
- Displays synthetic transmission topology, flow ratings and critical services.

## Research limitations (read before interpreting)
This is **not** a real grid, safety controller, certified power-system study, contingency-clearing algorithm or stability model. The lossless DC approximation ignores reactive power, voltage magnitudes, AC losses, inertia, load dynamics and protective relays. Line overloads are flagged, **not resolved or automatically tripped**. Backup generation is an illustrative supply-capacity increase, not a realistic grid-forming microgrid. Load prioritization is a simplified capacity-allocation heuristic, not feasible security-constrained optimal power flow. All numbers are synthetic power units (shown as MW* in the UI), not observed grid measurements.

See `docs/` for methodology, constraints, engineering validation, API and extension plans.
