# QuestGuard — Game NPC Action Safety & World Grounding (Day 043/365)

A deterministic verification layer for LLM-driven game agents. The model proposes; authoritative game state and policy decide whether actions execute.

Features: typed action allowlist, evidence grounding, visibility/inventory/stamina/door/quest/navigation preconditions, rejection codes, audit trail, no state mutation on rejection, quest candidate generation, event memory and FastAPI dashboard.

Run: `python -m venv .venv` then `pip install -e .[test]` then `uvicorn questguard.main:app --reload`. Open http://127.0.0.1:8000 and /docs. Tests: `pytest -q`.

Limitations: deterministic demo proposals; no live LLM or game-engine integration. In-memory stores. Exact fact grounding, not semantic entailment. No multiplayer authority, persistence, authentication or load testing.