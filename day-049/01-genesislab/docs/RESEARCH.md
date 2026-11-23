# Research design
The demonstrator implements a small exact Gaussian process with an RBF covariance kernel and independently modeled Gaussian measurement noise. Candidate selection maximizes expected improvement over the current best measurement. Every candidate passes a fixed feasibility constraint, and no candidate is re-measured during a trial.

Comparison uses matched random seeds and identical initial three experiments for adaptive and random strategies. Report real best synthetic objective and cumulative regret, not just noisy observed maxima. Evaluation is restricted to the synthetic landscape and cannot substantiate general claims of Bayesian optimization superiority.
