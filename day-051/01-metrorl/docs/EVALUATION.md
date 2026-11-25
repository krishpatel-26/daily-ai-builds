# Evaluation protocol
Compare fixed-time, simple max-pressure and trained Q-learning on 12 shared evaluation seeds. Report mean and normal-approximation 95% confidence intervals for throughput, average queue occupancy, dropped demand, phase switches and number of emergency events served. All metrics must be considered together: a low average queue can indicate lost arrivals rather than excellent service. Verify conservation error is zero before interpreting performance.

For stronger research, add multiple training seeds, independent maps and demand patterns, held-out validation, confidence intervals on paired differences and calibrated real traffic data.
