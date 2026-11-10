# AgentGuard — AI Agent Permission & Action Guard

A local-first policy gateway that sits between an AI agent and business tools. It evaluates proposed actions against explicit permissions, risk rules, approval requirements, and current resource state before execution.

## Why
LLMs can propose actions; they should not decide their own authority. AgentGuard makes authorization deterministic and auditable.

## Features
- Typed action proposals and policy decisions
- Role/resource/action allowlists
- Risk classification and approval gates
- Resource-state preconditions
- SQLite audit trail
- Approval queue and decision API
- Minimal dashboard for reviewing requests
- Dry-run mode; no external systems are touched

## Run
Python 3.10+
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000

## Test
```bash
python -m unittest discover -s tests -v
```

## Demo
Submit a request to update a customer record. Low-risk actions can be allowed; sensitive actions require approval; unknown actions and invalid state transitions are denied.

## Safety boundary
This prototype records decisions and simulates execution. It does not connect to production tools, perform real financial transactions, or establish that an action is safe merely because it passes a policy. Integrate only behind your own authentication, network controls, and human review.

## API
- POST /api/evaluate — evaluate a proposed action
- GET /api/requests — list recent requests
- GET /api/approvals — list pending approvals
- POST /api/approvals/{request_id} — approve or reject
- GET /api/audit — inspect audit events
- GET /health — health check
