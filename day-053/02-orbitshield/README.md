# OrbitShield — Orbital Conjunction & Maneuver Trade-off Research Lab

**Day 053/365 · 27 November 2026**

A self-contained educational research workbench implementing two-body orbital dynamics with RK4 numerical integration, synthetic debris objects, minimum-separation screening, an illustrative conjunction threshold, and prograde/retrograde impulse scenario comparison.

## Run

Requires Python 3.11+. No third-party runtime packages or API keys.

```bash
python -m orbitshield.server
python -m unittest discover -s tests -v
```

Dashboard: http://127.0.0.1:4211 . Scenario JSON: `/api/report?seed=53&step=20`.

## Research boundary

This is **not** satellite conjunction assessment or collision-avoidance guidance. It uses deterministic synthetic, planar two-body orbits and hypothetical impulsive maneuvers. It ignores real satellite ephemerides, tracking uncertainty, covariance propagation, perturbations (Earth oblateness J2, drag, solar radiation), 3D relative geometry, collision probability, operational flight constraints, fuel budgets, and regulatory coordination. The thresholds and maneuver ranking are only for simulation education. Never use this to maneuver spacecraft. Real conjunction analysis requires validated high-fidelity dynamics, uncertainties, and operator review.
