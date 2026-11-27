import math
from .dynamics import rk4
from .constants import DEFAULT_HORIZON,DEFAULT_STEP,CONJUNCTION_KM

def propagate(s,step=DEFAULT_STEP,horizon=DEFAULT_HORIZON):
    if not 1<=step<=120 or not 60<=horizon<=21600:raise ValueError('invalid propagation horizon or step')
    out=[(0.,tuple(s))];t=0.;cur=tuple(s)
    while t<horizon:
        dt=min(step,horizon-t);cur=rk4(cur,dt);t+=dt;out.append((t,cur))
    return out

def closest(primary,secondary):
    if len(primary)!=len(secondary):raise ValueError('time histories differ')
    best=(float('inf'),0.0)
    for (t,a),(u,b) in zip(primary,secondary):
        if abs(t-u)>1e-6:raise ValueError('time samples differ')
        d=math.hypot(a[0]-b[0],a[1]-b[1])
        if d<best[0]:best=(d,t)
    return {'min_separation_km':round(best[0],5),'time_of_closest_sec':round(best[1],2),'illustrative_flag':best[0]<CONJUNCTION_KM}
