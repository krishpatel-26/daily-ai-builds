# Training protocol
Tabular Q-learning with epsilon-greedy exploration, 160 seeded episodes, up to 135 ticks each, learning rate 0.13, discount 0.91, exploration declining from roughly 0.39 to 0.04. Q-values initialize to zero. The Bellman target is immediate local reward plus discounted maximum next-state action value. Policies are evaluated after training without further updates. Training and evaluation seeds do not overlap.

Test both reproducibility and sensitivity to hyperparameters; do not imply convergence from a declining episode-level queue statistic alone.
