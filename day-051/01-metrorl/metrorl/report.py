from functools import lru_cache
from .benchmark import evaluate
from .sensitivity import sweep
from .invariants import audit_trajectory

@lru_cache(maxsize=1)
def report():
    results=evaluate()
    # One illustration per policy, excluding all other large per-run traces.
    return {'project':'MetroRL','comparison':results['scores'],'training':results['training'],
            'examples':{k:v[0] for k,v in results['runs'].items()},
            'sensitivity':sweep(),
            'conservation_checks':{k:audit_trajectory(v[0]) for k,v in results['runs'].items()},
            'caveat':'Synthetic corridor research: coarse queues, simplified switching and no verified real traffic dynamics.'}
