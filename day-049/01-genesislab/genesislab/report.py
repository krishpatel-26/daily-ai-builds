from .domain import candidates
from .experiments import run_trial
from .benchmark import benchmark
from .process import true_quality


def report(seed=49,budget=16):
    trial = run_trial(seed,budget,'adaptive')
    pool = candidates()
    return {'project':'GenesisLab','trial':trial,'benchmark':benchmark(),
            'feasible_space':len(pool),
            'landscape':[{'t':c.temperature,'s':c.speed,'quality':true_quality(c)} for c in pool],
            'limitations':'Deterministic synthetic process, simulated noise and GP-guided experiment selection. No LLM, laboratory hardware, physical validation or claim of genuine scientific discovery.'}
