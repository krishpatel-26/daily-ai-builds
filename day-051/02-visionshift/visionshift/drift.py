"""Population stability index (PSI) for aggregate feature shift.
PSI is NOT a classifier accuracy or safety metric.
"""
import math
from .dataset import FEATURES

def quantiles(values,k=10):
    s=sorted(values)
    if len(s)<k:raise ValueError('insufficient reference samples')
    return [s[min(len(s)-1,int(i*len(s)/k))] for i in range(1,k)]

def proportions(values,cuts):
    counts=[0.]*(len(cuts)+1)
    for v in values:
        index=sum(v>c for c in cuts)
        counts[index]+=1
    return [(c+.5)/(len(values)+.5*len(counts)) for c in counts]

def psi(a,b,k=10):
    if len(a)<k or not b:raise ValueError('not enough samples')
    cuts=quantiles(a,k)
    ref=proportions(a,cuts);obs=proportions(b,cuts)
    return sum((q-p)*math.log(q/p) for p,q in zip(ref,obs))

def feature_drift(training,observed):
    return {name:round(psi([r.x[i] for r in training],[r.x[i] for r in observed]),4) for i,name in enumerate(FEATURES)}
