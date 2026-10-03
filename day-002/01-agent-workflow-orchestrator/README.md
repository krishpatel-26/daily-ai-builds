# Agent Workflow Orchestrator

A provider-independent multi-agent workflow engine with typed planning, specialist agents, runtime execution, API boundaries, and tests.

Run: pip install -r requirements.txt && uvicorn app.main:app --reload

POST /v1/workflows with a JSON request field. Tests: pytest -q
