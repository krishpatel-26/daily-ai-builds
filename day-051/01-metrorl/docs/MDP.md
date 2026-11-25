# Markov decision process approximation
**State:** NS queue bin 0–3, EW queue bin 0–3, previous green phase 0/1, and emergency indicator 0/1/2. **Actions:** select NS or EW green. **Reward:** +2 per served vehicle, −0.13 per remaining queued vehicle, −5 per lost arrival, −1.4 per changeover, and −14 while an emergency vehicle is awaiting service. These weights express an arbitrary research objective, not a public-policy recommendation. Shared Q-table enables limited transfer across identically structured intersections.

The true system state includes unmodeled transfer and demand dynamics. The discrete state is not fully Markovian; treat results as a toy RL benchmark.
