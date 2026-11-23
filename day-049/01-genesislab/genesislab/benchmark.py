"""Matched-seed comparison; no unsupported superiority claims."""
from statistics import mean,stdev
from .experiments import run_trial


def benchmark(seeds=range(8),budget=14):
    seeds=list(seeds)
    if not seeds:
        raise ValueError('At least one seed required')
    trials={policy:[run_trial(seed,budget,policy) for seed in seeds]
            for policy in ('adaptive','random')}
    out=[]
    for policy,runs in trials.items():
        values=[r['best']['synthetic_true_quality'] for r in runs]
        regrets=[r['cumulative_synthetic_regret'] for r in runs]
        out.append({'policy':policy,'seeds':len(seeds),'budget':budget,
                    'mean_best_true_quality':round(mean(values),3),
                    'mean_cumulative_regret':round(mean(regrets),3),
                    'sd_best_true_quality':round(stdev(values) if len(values)>1 else 0,3)})
    differences=[a['best']['synthetic_true_quality']-b['best']['synthetic_true_quality']
                 for a,b in zip(trials['adaptive'],trials['random'])]
    return {'strategies':out,'paired_quality_delta':round(mean(differences),3),
            'paired_seed_count':len(seeds),
            'caveat':'Synthetic objective and small matched-seed benchmark; not real scientific discovery.'}
