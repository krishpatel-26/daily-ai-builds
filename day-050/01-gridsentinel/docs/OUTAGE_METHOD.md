# N−1 methodology

Each of the 12 lines is removed independently. The network is re-islanded; generation and served demand are recomputed; DC flows and line-limit violations are evaluated. For each strategy, aggregate outcomes are mean served percentage, critical demand unserved, overloaded scenario count, and worst-case served share. No multi-line contingencies or cascading tripping are simulated.

The demo network is intentionally generation-constrained (168 synthetic units capacity against 189 demand). Backup strategies add 48 modeled units at critical nodes to examine load restoration under stress. These are arbitrary educational assumptions, not an actual grid.
