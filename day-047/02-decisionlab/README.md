# DecisionLab — Counterfactual Maintenance & Operations Research

**Day 047/365, project two** — a reproducible simulation laboratory comparing factory maintenance policies using matched exogenous random shocks, paired policy differences and approximate uncertainty intervals.

Includes three-stage production simulation with finite buffers, stochastic failures and degradation; reactive, periodic and condition-based policies; 25-seed paired cost and throughput comparisons; confidence intervals; demand sensitivity; read-only API; responsive experimental dashboard and automated tests. Python 3.11+, standard library only.

```bash
python -m decisionlab.server
python -m unittest discover -s tests -v
```

Open http://127.0.0.1:4199. API: http://127.0.0.1:4199/api/report.

**Research boundary:** All assumptions, prices, failure rates and maintenance rules are synthetic. Paired simulation estimates differences *within this model only*, not real-world causal effects. Normal-approximation CIs are exploratory. No equipment integration or safety control. Do not deploy to an actual factory without engineering validation.
