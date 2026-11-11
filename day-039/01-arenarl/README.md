# ArenaRL — Multi-Agent Reinforcement Learning Lab
Day 039 / Daily AI Builds.

ArenaRL extends AgentArena with a reproducible training and evaluation loop for independent tabular Q-learning agents in a shared competitive environment.

## Features
- Compact discrete observations and bounded action space.
- Independent Q-learning with epsilon-greedy exploration.
- Reward shaping for resource collection, survival and objective control.
- Seeded training episodes and configurable hyperparameters.
- Greedy evaluation against heuristic and random baselines.
- Episode metrics, policy snapshots and JSON export.
- FastAPI endpoints and browser dashboard.
- Unit tests for environment transitions, learning updates and evaluation.

## Run
Python 3.10+:
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000 and API docs at /docs.

## Model boundary
This is a small synthetic grid-world research sandbox using independent tabular Q-learning. It is not deep reinforcement learning, a general-purpose game agent, or evidence of convergence. Results depend on the authored reward function and environment.