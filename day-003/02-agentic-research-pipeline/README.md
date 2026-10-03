# Agentic Research Pipeline

A local-first research workflow: planner -> specialist agents -> evidence scoring -> synthesis. Provider boundaries make it easy to replace the deterministic knowledge adapter with web search or an LLM later.

Run: pip install -r requirements.txt && uvicorn app.main:app --reload
Tests: pytest -q