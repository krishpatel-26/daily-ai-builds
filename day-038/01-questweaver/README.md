# QuestWeaver — Adaptive Quest Generation & Planning Engine
Day 038 / Daily AI Builds.

QuestWeaver creates structured, state-aware quest plans from a fictional game's world state. It scores authored quest templates, validates prerequisites, builds branching objectives, and emits explainable recommendations.

## Features
- State-aware quest template ranking.
- Prerequisite and objective validation.
- Branch selection based on trust, faction tension, resources and reputation.
- Dependency graph validation and topological quest ordering.
- Deterministic plan generation and explanation traces.
- FastAPI REST endpoints and interactive workbench.
- Synthetic fantasy-world data and unit tests.

## Run
Python 3.10+:
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000 and /docs.

## Boundary
This prototype uses hand-authored templates and deterministic scoring. It does not call an LLM, generate arbitrary code, or connect to a live game engine. Quest plans are recommendations; the authoritative game server must validate execution.