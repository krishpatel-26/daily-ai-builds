"""Sequential optimizer and paired random baseline."""
import random
from .domain import candidates
from .process import measure, true_quality
from .acquisition import propose
from .hypotheses import explain


def run_trial(seed=49,budget=16,policy='adaptive'):
    if policy not in ('adaptive','random'):
        raise ValueError('Unknown acquisition policy')
    pool = candidates()
    if not 4 <= budget <= min(40,len(pool)):
        raise ValueError('Experiment budget must be 4..40')
    rng = random.Random(seed)
    initialization = rng.sample(pool, 3)
    observed = []
    history = []
    for step in range(budget):
        prediction = None
        if step < 3:
            c = initialization[step]
        elif policy == 'random':
            remaining = [x for x in pool if x not in {p for p,_ in observed}]
            c = rng.choice(remaining)
        else:
            c,prediction = propose(pool, observed)
        previous = max([x for _,x in observed], default=float('-inf'))
        note = explain(c,prediction,previous)
        result = measure(c,seed)
        observed.append((c,result))
        history.append({'step':step+1,'parameters':c.to_dict(),
                        'quality':result,'best_quality':round(max(x for _,x in observed),3),
                        'prediction':prediction,'hypothesis':note,
                        'is_new_best':result>previous})
    best_candidate,best_value = max(observed,key=lambda x:x[1])
    oracle = max(pool,key=true_quality)
    return {'policy':policy,'seed':seed,'budget':budget,'best':{'parameters':best_candidate.to_dict(),
            'observed_quality':best_value,'synthetic_true_quality':true_quality(best_candidate)},
            'oracle':{'parameters':oracle.to_dict(),'synthetic_true_quality':true_quality(oracle)},
            'history':history,'experiments':len(history),
            'cumulative_synthetic_regret':round(sum(true_quality(oracle)-true_quality(c) for c,_ in observed),3)}
