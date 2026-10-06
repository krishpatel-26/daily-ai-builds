# Agentic Incident Response Engine

A production-minded AI incident triage system that turns noisy service alerts into an explainable incident plan. It combines deterministic signal normalization, specialist agents, severity scoring, runbook retrieval, action planning, and an auditable execution boundary.

## Architecture
`ingest -> normalize -> classify -> specialist analysis -> runbook retrieval -> plan -> approval boundary`

The default runtime is deterministic and local. External LLMs and observability systems can be added behind provider interfaces without changing the orchestration contract.

## Run
```bash
python -m venv .venv
pip install -r requirements.txt
uvicorn app.api:app --reload
```

POST `/v1/incidents/analyze` with an incident payload. Run `pytest` for tests.

## Safety
The engine generates proposed actions but never executes destructive remediation automatically. Production integrations should sit behind an explicit approval/execution adapter.
