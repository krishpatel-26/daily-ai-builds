# GenesisLab — Autonomous Experiment Design & Bayesian Optimization Research Lab

**Day 049/365 · Research Build 01**

A real, reproducible Gaussian-process (GP) Bayesian optimization loop operating on a constrained **synthetic** process-quality landscape. It proposes experiments, makes noisy measurements, updates a GP posterior, and selects the next experiment through expected improvement. Includes a random-search baseline and matched-seed comparison.

## Run

Python 3.11+, standard library only. No LLM, external package or API key.

```bash
python -m genesislab.server
python -m unittest discover -s tests -v
```

Open `http://127.0.0.1:4202`, or `GET /api/report?seed=49&budget=16`.

## Architecture

Synthetic process → bounded feasible parameter grid → initial randomized observations → GP posterior (RBF kernel, Cholesky solution) → expected-improvement acquisition → new measurement → experiment history → multi-seed benchmark → dashboard.

## Important limits

There is **no real scientific discovery, real laboratory, generative model, autonomous wet-lab, or claims of industrial performance**. This is a computational research method demonstration using synthetic quality and cost functions. Human oversight and physical experimentation would be mandatory for real-world adoption.
