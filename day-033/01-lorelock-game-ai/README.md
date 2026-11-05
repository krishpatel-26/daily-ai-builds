# LoreLock — Hallucination-Resistant Game AI
Day 033 / Daily AI Builds. A constrained runtime for LLM-powered NPCs: models propose typed actions, but only the authoritative game server validates and applies changes.
Features: strict action schema; server allowlist; actor/target/range/inventory/quest checks; deterministic state transitions; curated lore retrieval with source IDs and safe fallback; idempotency; audit log; FastAPI and browser console; synthetic RPG scenario.
Run: Python 3.10+, `pip install -r requirements.txt`, `uvicorn app.main:app --reload`; open http://127.0.0.1:8000 and /docs.
Invariant: model is an untrusted proposer, never the authority. Mock proposer only; no live LLM. In-memory demo, lexical lore matching, not production multiplayer or semantic truth verification.