# ArenaCTDE — Centralized Training, Decentralized Execution
Day 040. Cooperative two-agent MARL research sandbox demonstrating parameter-shared PPO actors with local observations and a centralized joint-state critic.
Features: partial observations, centralized value estimation, clipped PPO, GAE, entropy regularization, seeded training, held-out evaluation, FastAPI and dashboard.
Run: Python 3.10+, pip install -r requirements.txt, uvicorn app.main:app --reload. Open http://127.0.0.1:8000.
Research boundary: compact synthetic corridor environment, educational MAPPO-style implementation, not a canonical benchmark or convergence claim.