# AquaMind — Water Network Leak Intelligence Lab

**Day 052/365 · 26 November 2026** — an inverse-model research prototype for exploring leak localization in a synthetic municipal water network.

## Implemented

- Nine demand junctions, reservoir, sixteen pipes, eight pressure sensor locations.
- Linearized pressure/flow network solved with dependency-free Gaussian elimination.
- Seeded synthetic leak injection with configurable rate and sensor noise.
- Inverse least-squares leak localization and rate estimation, with top-five alternative locations.
- Residual comparison and noise-sweep benchmarks across nodes and random seeds.
- What-if pipe isolation calculations (not recommended operational actions).
- Interactive local dashboard and read-only HTTP endpoint.
- Automated tests for flow conservation, recovery, reproducibility, and validation.

## Run

Python 3.11+; no external packages required.

```bash
python -m aquamind.server
python -m unittest discover -s tests -v
```

Open **http://127.0.0.1:4208**. JSON endpoint: `/api/report?node=J-07&rate=4.5&seed=52`.

## Scientific limitations

**This is not hydraulic software or a real leak-detection service.** Pipe flows follow a linear conductive analogy. Real drinking-water pressure networks obey nonlinear hydraulic relations, have pumps, valves, dynamic demands, sensor errors, unobserved leaks, and pressure regulations. Because synthetic observations and inverse models use the *same* model, benchmarks measure model-matched recovery rather than independent field validity. No API issues equipment commands, and no real-world leak performance or financial savings are claimed. Field deployment requires comparison to a trusted simulator such as EPANET, calibrated network data, professional verification, safety and security review.
