# FactoryTwin — Industrial Condition Intelligence (Day 042/365)
A local-first industrial operations research prototype converting simulated machine telemetry into explainable condition scores, maintenance priorities and production exposure estimates.

## Features
- Five simulated assets with temperature, vibration, current, pressure and throughput signals.
- Rolling-window features, transparent threshold anomaly scoring and risk ranking.
- Diagnostic hints, human-reviewed maintenance windows and capacity-constrained scheduling.
- Production exposure estimates, FastAPI endpoints and responsive dashboard.

## Run
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000; API docs at /docs.

## Tests
```bash
python -m unittest discover -s tests -v
```

## API
GET /api/health · GET /api/fleet · GET /api/machines/{machine_id} · POST /api/telemetry · POST /api/work-orders · POST /api/schedule

## Limitations
Synthetic data and deterministic heuristics only; no trained failure model. Risk index is not a calibrated failure probability or remaining-useful-life estimate. No PLC/SCADA integration, CMMS connector, authentication or persistent database. Validate sensor calibration, operating modes and thresholds against plant data before operational use. Maintenance decisions require qualified human approval.