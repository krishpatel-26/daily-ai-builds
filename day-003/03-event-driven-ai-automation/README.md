# Event-Driven AI Automation Engine

Local event-driven automation with rules, idempotency, retries, audit events and pluggable actions. Example: lead.created triggers qualification and account enrichment.

Run: pip install -r requirements.txt && uvicorn app.main:app --reload
Tests: pytest -q