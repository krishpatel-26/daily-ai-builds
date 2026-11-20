# FleetOps — Autonomous Fleet Mission Control & Fault Recovery

**Day 047/365, project one** — a self-contained Python 3.11+ simulation of four autonomous mobile robots completing twelve warehouse tasks.

Capabilities include weighted assignment of tasks by priority, distance and deadlines; battery-aware dispatch; A* routing; station charging; injected robot failure with task requeue; conflict blocking; per-tick frame replay; and multi-seed comparison of fault and no-fault scenarios. Runs locally with Python's standard library.

```bash
python -m fleetops.server
python -m unittest discover -s tests -v
```

Open http://127.0.0.1:4198. JSON: http://127.0.0.1:4198/api/report.

**Research boundary:** Grid-world simulator, not connected to robots. Conservative conflict blocking can deadlock; planner does not solve full multi-agent pathfinding. No safety certification, real battery model, dynamic human obstacle detection or industrial operational recommendation. Faults and completion metrics are synthetic.
