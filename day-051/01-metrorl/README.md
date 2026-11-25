# MetroRL — Adaptive Traffic Signal Reinforcement Learning Lab

**Day 051/365 · Wednesday build 01** — a fully local, reproducible traffic-control simulation that trains a shared tabular Q-learning policy and evaluates it against fixed-time and queue-pressure controllers.

## Real implementation
- Three-intersection synthetic corridor with coupled vehicle queues and capacity limits.
- Seeded stochastic arrivals, green-phase service and lost time on phase changes.
- Eastbound vehicle transfers, queue spillback / dropped demand, emergency vehicle events.
- **Tabular Q-learning** (shared Q-table) trained using epsilon-greedy exploration and Bellman TD updates.
- Matched-seed evaluation across 12 seeds with approximate uncertainty intervals.
- Metrics: departures, queue lengths, dropped demand, switching, emergency service, conservation error.
- Local dark dashboard visualizing traffic policies and queue traces.

## Run
Python 3.11+, standard library only.

```bash
python -m metrorl.server
```

Open http://127.0.0.1:4206. Run tests: `python -m unittest discover -s tests -v`.

## Research boundary
**No physical signal integration.** This model simplifies lane geometry, turning decisions, road safety rules, demand, vehicle interactions and traffic regulations. Q-learning is tabular, not deep RL; superiority over max-pressure is **not** assumed. Matched synthetic simulation outcomes do not establish real-world benefits. Never connect to traffic controllers without specialist engineering validation.
