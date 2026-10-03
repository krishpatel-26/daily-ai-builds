# Agent Memory Service

Persistent, namespace-isolated memory for AI agents. Includes SQLite persistence, idempotent writes, importance weighting, recency decay and lexical retrieval.

Run: pip install -r requirements.txt && uvicorn app.main:app --reload
Tests: pytest -q
No external API or credential is required.