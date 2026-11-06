# QuestWeaver — World-Aware Adaptive Quest Engine
Day 035 / Daily AI Builds. Generates quest proposals from a structured world snapshot, validates objectives against registered entities and prerequisites, filters duplicates and emits deterministic plans.
Features: typed objectives; world-aware templates; entity and prerequisite validation; duplicate detection; explainable scoring; explicit accept/complete lifecycle; audit events; FastAPI, browser workbench and synthetic RPG tests.
Run: Python 3.10+, pip install -r requirements.txt, uvicorn app.main:app --reload. Open http://127.0.0.1:8000 and /docs.
Boundary: planner proposes; game server validates and decides. Deterministic templates and synthetic data; no live LLM or production multiplayer support.