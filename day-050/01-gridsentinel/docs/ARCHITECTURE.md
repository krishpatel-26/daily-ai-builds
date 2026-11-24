# Architecture

Static eight-node/12-corridor graph → simulated corridor outage → connected components → generation-vs-load allocation per island → balanced bus injections → DC linearized power-flow solution → line utilization and unserved critical-load metrics → N−1 comparisons → local JSON API and SVG visualization.

`models.py` holds immutable network records; `network.py` owns topology; `linear.py` performs Gaussian elimination; `powerflow.py` assembles bus admittance; `dispatch.py` applies prioritization; `scenarios.py` runs contingencies; `api.py` serves localhost visualization.
