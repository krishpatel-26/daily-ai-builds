# PulseFleet — Robot Fleet Health & Predictive Maintenance Lab

**Day 045/365** — a local research prototype that turns mobile-robot telemetry into explainable health signals and a maintenance work queue.

## Capabilities
- Deterministic AMR telemetry simulation
- Schema validation and CSV ingestion
- Rolling baseline features
- Median/MAD robust anomaly scoring plus transparent rules
- Explainable findings and heuristic health index
- Local JSON API and browser dashboard
- Unit tests and synthetic sample data

## Run
Python 3.11+, no third-party runtime dependencies.

```bash
python -m pulsefleet.server
```
Open http://127.0.0.1:4195.

Tests: `python -m unittest discover -s tests -v`

## Limitations
Synthetic-data prototype only. It does not predict failure dates, estimate true remaining useful life, connect to robots, or issue safety-critical commands. Thresholds are illustrative and require fleet-specific calibration and engineering review before operational use.
