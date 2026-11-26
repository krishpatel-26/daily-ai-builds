from .topology import SERVICES
from .simulator import simulate
from .infer import diagnose

def benchmark(seeds=range(10)):
    trials=[]
    for seed in seeds:
        for root in SERVICES:
            run=simulate(root,seed)
            result=diagnose(run['timeline'])
            trials.append({'root':root,'predicted':result['most_likely']['service'],
                           'baseline':result['naive_peak_candidate']})
    if not trials:raise ValueError('No seeds provided')
    n=len(trials)
    return {'trials':n,'root_top1_accuracy':round(sum(x['predicted']==x['root'] for x in trials)/n,4),
            'peak_baseline_accuracy':round(sum(x['baseline']==x['root'] for x in trials)/n,4),
            'uniform_chance_reference':round(1/len(SERVICES),4),
            'limitations':'Matched graph and propagation kernel. Metrics not transferable to real microservices; decoy spikes are part of the synthetic challenge.'}
