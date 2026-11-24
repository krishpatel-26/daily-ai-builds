import math
import statistics

def summary(values):
    if not values:raise ValueError('Need at least one observation')
    mean=statistics.mean(values)
    sd=statistics.stdev(values) if len(values)>1 else 0.0
    width=1.96*sd/math.sqrt(len(values))
    return {'n':len(values),'mean':round(mean,3),'ci95_normal':[round(mean-width,3),round(mean+width,3)]}

def paired_delta(a,b):
    if not a or len(a)!=len(b):raise ValueError('Expected equal nonempty samples')
    return summary([x-y for x,y in zip(a,b)])
