"""Traffic demand sensitivity, with identical seeds per evaluated policy."""
from dataclasses import replace
from statistics import mean
from .config import Config
from .environment import Corridor
from .policies import fixed_time,max_pressure
from .qlearning import train

def sweep(arrivals=(.75,1.05,1.35),seeds=(901,902,903),episodes=160):
    model,_=train(episodes=episodes)
    results=[]
    for demand in arrivals:
        if demand<=0:raise ValueError('arrival rate must be positive')
        c=replace(Config(),base_arrival=demand)
        for policy,fn in [('fixed_time',fixed_time),('max_pressure',max_pressure),('q_learning',model.act)]:
            values=[Corridor(seed=seed,config=c).run(fn)['metrics'] for seed in seeds]
            results.append({'base_arrival':demand,'policy':policy,
                            'mean_exits':round(mean(v['exits'] for v in values),2),
                            'mean_dropped':round(mean(v['dropped'] for v in values),2),
                            'mean_queue':round(mean(v['mean_queue'] for v in values),2),
                            'n':len(values)})
    return results
