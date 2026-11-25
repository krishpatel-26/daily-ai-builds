from statistics import mean,stdev
from .environment import Corridor
from .policies import fixed_time,max_pressure
from .qlearning import train

def summarize(values):
    n=len(values);mu=mean(values);sd=stdev(values) if n>1 else 0.
    return {'mean':round(mu,2),'ci95_approx':[round(mu-1.96*sd/(n**.5),2),round(mu+1.96*sd/(n**.5),2)],'n':n}

def evaluate(seeds=range(501,513),episodes=160):
    policy,training=train(episodes=episodes)
    funcs={'fixed_time':fixed_time,'max_pressure':max_pressure,'q_learning':policy.act}
    trials={name:[Corridor(seed=s).run(fn) for s in seeds] for name,fn in funcs.items()}
    scores={name:{metric:summarize([r['metrics'][metric] for r in runs]) for metric in ('exits','mean_queue','dropped','switches','emergencies_served')} for name,runs in trials.items()}
    return {'training':training,'scores':scores,'runs':trials}
