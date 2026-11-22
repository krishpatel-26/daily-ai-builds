# CrisisMesh — Disaster Response Coordination Simulator

**Day 048/365 — Research Build 01.** A reproducible, flood-aware disaster-response routing and resource-allocation simulator built with Python 3.11+ and zero external packages.

## Features
- Seeded synthetic 22×14 flood terrain with four flood epicenters.
- Ten incidents with severity, population counts, and emergency type.
- Four response teams with water-depth capability, capacity, speed, and range limits.
- Cost-weighted Dijkstra routing that never enters a cell above the responding team's flood tolerance.
- Deterministic, severity-prioritized team assignment with availability constraints.
- Comparison of risk-aware routing against shortest-distance routing.
- Interactive browser heat map, routes, mission queue, and coverage metrics.
- Automated unit tests and an optional 20-seed experiment.

## Run
```bash
python -m crisismesh.server
# In a second terminal
python -m unittest discover -s tests -v
```
Open http://127.0.0.1:4200, or GET /api/scenario?seed=48 and /api/benchmark.

## Research limitations
This is a synthetic educational simulator. It does not contain live incident information, realistic hydrodynamics, calibrated travel time, evacuation ethics or real dispatch integrations. **Never use it for emergency response decisions.** Coverage scores measure hypothetical response-team allocation, not actual rescues. Risk-weighting does not guarantee higher coverage or faster arrival. Independent emergency services and safety professionals must govern any operational system.