# Priority rules

This prototype uses a deterministic heuristic, not a model:
- high severity: 60 points; medium: 30; low: 10;
- implementation blocker: +30; delivery/renewal risk: +25; expansion opportunity: +15;
- past-due open signal: +10;
- completed signal: 0.

P1 starts at 80, P2 at 45, otherwise P3. The score organizes a queue; it is not a revenue forecast or customer-risk prediction. Teams should tune and validate rules before operational use.
