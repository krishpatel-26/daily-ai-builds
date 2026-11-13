# GraphMind — Adaptive Multi-Agent Communication & Coordination Engine
Day 041/365. Research prototype for studying whether graph-based information exchange improves cooperative multi-agent navigation.

## Research question
Can agents improve coordinated decisions by selectively aggregating information from nearby agents rather than acting only on local observations?

## Implemented
- Four-agent cooperative corridor environment with local observations and shared team reward.
- Dynamic radius-based communication graph.
- Graph-attention message aggregation implemented in PyTorch.
- Shared communication-aware actor and centralized value critic.
- PPO-style clipped policy update with GAE.
- Baseline evaluation with communication enabled/disabled.
- Communication edge counts, success rate, reward and episode length.
- FastAPI endpoints and browser dashboard.
- Unit tests for environment, graph construction, attention, returns and API contracts.

## Run
Python 3.10+
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000

## Research limitations
This is a compact synthetic environment and experimental implementation, not a validated MARL benchmark. The communication graph is radius-based rather than learned; the attention weights are learned. Compare multiple seeds and baselines before drawing conclusions. Tests are provided but must be run locally.