# FactoryTwin AI — Industrial Digital Twin & Operations Optimizer
Day 046/365. A reproducible discrete-time manufacturing simulation, scenario comparison and constrained maintenance-policy search.

## Features
- Three-stage production line with finite buffers and configurable throughput
- Seeded stochastic failures and repair durations
- Preventive maintenance scheduling with downtime costs
- KPI engine: units, utilization, downtime, throughput, cost and late orders
- Grid-search scenario optimizer and Pareto filtering
- Local API, dashboard and automated unit tests

## Run
Python 3.11+, no third-party runtime dependencies.
```bash
python -m factorytwin.server
python -m unittest discover -s tests -v
```
Open http://127.0.0.1:4196.

## Scope
Simulation and optimization prototype, not validated for live factory control. All machine parameters are illustrative. No PLC or equipment integration; human approval required for operational decisions.
