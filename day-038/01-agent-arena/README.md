# AgentArena — Multi-Agent Game Simulation & Policy Evaluation
Day 038 / Daily AI Builds.
A deterministic sandbox for autonomous game agents. Agents observe world state, generate candidate actions, score utility, pass precondition validation, resolve conflicts and produce an auditable event trace.
Features: typed action proposals, utility policies, resource constraints, initiative ordering, turn scheduler, state transitions, conflict handling, replayable event log, metrics, REST API and browser workbench.
Run with Python 3.10+: pip install -r requirements.txt && uvicorn app.main:app --reload. Open http://127.0.0.1:8000 and /docs.
Boundary: deterministic authored policies and synthetic map; not an LLM agent, learned policy or production multiplayer server.