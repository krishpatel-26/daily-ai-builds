# MythosGraph — Persistent Memory for AI Game Worlds
Day 034 / Daily AI Builds. A character-scoped memory engine for game NPCs: episodic events, witness visibility, relationships, canon facts and continuity checks.
Features: SQLite event store; witnessed/public/private memories; retrieval ranked by lexical relevance and importance; directed reputation scores; canon contradiction checks; timeline and analytics; FastAPI and browser console.
Run: Python 3.10+, pip install -r requirements.txt, uvicorn app.main:app --reload. Open http://127.0.0.1:8000 and /docs.
Prototype limitations: synthetic data, lexical retrieval, rule-based contradiction checks, no live LLM, no embeddings or production multiplayer authentication.