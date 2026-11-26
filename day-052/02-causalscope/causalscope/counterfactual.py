"""Intervention in the simulated generator, not causal inference from real observations."""
from .simulator import simulate
from .signals import total_anomaly

def remove_injected_fault(root='database',seed=52,strength=2.7,noise_sd=.19):
    observed=simulate(root,seed,strength,noise_sd)
    controlled=simulate(root,seed,0,noise_sd)
    before=total_anomaly(observed['timeline']);after=total_anomaly(controlled['timeline'])
    return {'simulated_impact_before':before,'counterfactual_without_fault':after,
            'modeled_reduction':round(before-after,3),
            'warning':'This synthetic intervention reuses the same noise stream and decoy; it is not an observed production intervention.'}
