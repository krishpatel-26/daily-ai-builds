# Agent Memory Service

Persistent, namespace-isolated memory for AI agents. Stores facts and events in SQLite and ranks memories using lexical relevance, importance, and recency.

Run: pip install -r requirements.txt && uvicorn app.main:app --reload
Tests: pytest
No external API or credentials required.
