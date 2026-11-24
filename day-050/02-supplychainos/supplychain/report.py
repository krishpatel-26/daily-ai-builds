from .simulator import simulate
from .experiments import compare_policies,pareto

def report(policy='diversified',seed=50,days=70,disrupted=True):
    run=simulate(policy,seed,days,disrupted)
    candidates=compare_policies(days=days,disrupted=disrupted)
    return {**run,'comparisons':candidates,'pareto_policies':pareto(candidates),
            'disclaimer':'Counterfactual outcomes are valid only within the synthetic model; no real supply-chain predictions.'}
