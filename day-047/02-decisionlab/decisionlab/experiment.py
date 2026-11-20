from .simulator import simulate
from .statistics import summarize,paired_difference
from .config import Experiment

CANDIDATES=[('reactive',90,55),('periodic',70,55),('periodic',100,55),('condition_based',90,50),('condition_based',90,65)]

def compare(seeds=range(20,45),settings=Experiment()):
    seeds=list(seeds)
    if not seeds:raise ValueError('At least one seed needed')
    outputs=[]
    baseline=[simulate('reactive',seed,settings) for seed in seeds]
    for policy,interval,threshold in CANDIDATES:
        trials=[simulate(policy,seed,settings,interval,threshold) for seed in seeds]
        costs=[x['estimated_cost'] for x in trials]
        produced=[x['units_produced'] for x in trials]
        diffs=paired_difference(costs,[x['estimated_cost'] for x in baseline])
        outputs.append({'policy':policy,'interval':interval,'threshold':threshold,'cost':summarize(costs),'throughput':summarize(produced),'paired_cost_delta_vs_reactive':diffs,'mean_failure_events':round(sum(x['failure_events'] for x in trials)/len(trials),2)})
    return sorted(outputs,key=lambda x:x['cost']['mean'])
