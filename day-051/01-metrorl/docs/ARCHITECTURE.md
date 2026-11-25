# System architecture
Three coupled intersections are represented as pairwise NS/EW queue aggregates. A deterministic seeded arrival generator feeds the queue model. Policies select a green phase once per discrete tick. The simulator applies changeover lost time, serves vehicle batches, forwards a fraction of EW traffic to the next junction, tracks demand loss when capacity is exceeded, and returns outcomes and queue history. Q-learning learns one shared table from discretized local observations. Evaluation uses held-out seeds, not training seeds.

The read-only HTTP server returns aggregate comparisons and scenario traces. It never connects to live traffic controllers.
