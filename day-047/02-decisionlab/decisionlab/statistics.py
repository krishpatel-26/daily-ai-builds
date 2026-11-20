import math
import statistics

def summarize(values):
    if not values:raise ValueError('At least one observation required')
    mean=statistics.mean(values)
    sd=statistics.stdev(values) if len(values)>1 else 0.0
    half_width=1.96*sd/math.sqrt(len(values))
    return {'n':len(values),'mean':round(mean,3),'standard_deviation':round(sd,3),'ci95_normal_approx':[round(mean-half_width,3),round(mean+half_width,3)]}

def paired_difference(treatment,baseline):
    if len(treatment)!=len(baseline) or not treatment:raise ValueError('Paired samples must be nonempty and equal length')
    return summarize([a-b for a,b in zip(treatment,baseline)])
