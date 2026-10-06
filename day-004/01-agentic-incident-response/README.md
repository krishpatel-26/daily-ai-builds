# Agentic Incident Response Engine

A production-minded incident triage system that turns noisy alerts into an explainable response plan.

**Architecture:** alerts → enrichment → specialist agents → severity scoring → evidence lineage → runbook retrieval → policy gate → human approval → audit trail.

### Governance layer
- deterministic evidence IDs for lineage
- configurable confidence threshold
- mandatory approval for high/critical incidents
- explicit approve/reject API
- SQLite audit trail with actor and timestamp
- no automatic destructive remediation

### Run
```bash
python -m venv .venv
pip install -r requirements.txt
uvicorn app.api:app --reload
pytest
```

POST `/v1/incidents/analyze`, then use the returned `incident_id` with `/v1/incidents/{incident_id}/approval`. Retrieve the full decision history from `/v1/incidents/{incident_id}/audit`.

External LLMs and observability systems can be added behind provider adapters; the default path remains deterministic and local.
