# FleetPulse AI — Predictive Maintenance & Fleet Intelligence

**Day 032 / Daily AI Builds**

FleetPulse AI is a local-first industrial equipment health platform. It ingests machine telemetry, derives rolling condition indicators, calculates a transparent anomaly score, estimates maintenance priority, tracks assets, and generates explainable maintenance recommendations.

This is a working engineering prototype, not a certified safety system or validated remaining-useful-life predictor. The included telemetry is synthetic. Scores are decision-support indicators, not failure probabilities.

## Capabilities
- Register and inspect industrial assets.
- Ingest vibration, temperature, pressure, current, RPM, and runtime telemetry.
- Derive rolling statistics and engineering-rule features.
- Detect anomalies using robust median/MAD scoring plus explicit operating limits.
- Compute health index and maintenance priority with explanation codes.
- View asset trends, alerts, and fleet-level risk distribution.
- Record maintenance work orders and close them with notes.
- Export asset telemetry and health assessments as JSON/CSV.
- Seed a sample fleet and synthetic sensor streams.
- SQLite persistence and REST API.

## Quick start
Python 3.10+.

```bash
cd day-032/01-fleetpulse-ai
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000 and interactive API docs at /docs.

## Demo data
Click **Load demo fleet** in the UI or call:
```bash
curl -X POST http://127.0.0.1:8000/api/demo/seed
```

## API
- `GET /api/health`
- `GET/POST /api/assets`
- `GET /api/assets/{asset_id}`
- `POST /api/assets/{asset_id}/telemetry`
- `GET /api/assets/{asset_id}/telemetry`
- `GET /api/assets/{asset_id}/health`
- `GET /api/fleet/summary`
- `GET /api/alerts`
- `GET/POST /api/work-orders`
- `PATCH /api/work-orders/{work_order_id}/close`
- `POST /api/demo/seed`

## Model transparency
The current health score combines normalized deviation from configured operating limits, robust deviation from a recent baseline, and trend change. Every assessment contains feature values and reason codes. It does not use a trained predictive model and must not be interpreted as remaining useful life.

## Production gaps
Real sensor connectors (OPC UA/MQTT), asset-specific calibration, labeled failure data, validated prognostics, edge buffering, role-based access, auditability, time-series storage, and industrial cybersecurity review are required before deployment in an operational environment.

## Safety
Use FleetPulse AI for experimentation and decision support only. Maintenance actions must be reviewed by qualified personnel under the site's established procedures.
