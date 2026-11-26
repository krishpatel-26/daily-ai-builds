import random
from .topology import SERVICES,downstream_hops
from .kernel import effect

STEPS=45

def simulate(root='database',seed=52,strength=2.7,noise_sd=.19,start=None,decoy=True):
    if root not in SERVICES:raise ValueError('Unknown injected root')
    if noise_sd<0 or noise_sd>3:raise ValueError('noise_sd must be between 0 and 3')
    if strength<0 or strength>20:raise ValueError('strength must be between 0 and 20')
    rng=random.Random(seed);start=13+seed%6 if start is None else start
    if not 0<=start<STEPS:raise ValueError('invalid injection time')
    hops=downstream_hops(root); other=[s for s in SERVICES if s!=root]
    decoy_service=other[seed%len(other)];decoy_at=23+seed%5
    rows=[]
    for t in range(STEPS):
        state={}
        for service in SERVICES:
            propagation=strength*effect(hops[service],t,start) if service in hops else 0
            spike=3.1 if decoy and service==decoy_service and t==decoy_at else 0
            latency=propagation+spike+rng.gauss(0,noise_sd)
            errors=.9*propagation+.8*spike+rng.gauss(0,noise_sd)
            state[service]={'latency_z':round(latency,5),'error_z':round(errors,5)}
        rows.append({'tick':t,'metrics':state})
    return {'root':root,'seed':seed,'strength':strength,'start':start,'noise_sd':noise_sd,
            'decoy_service':decoy_service if decoy else None,'decoy_tick':decoy_at if decoy else None,
            'timeline':rows,'steps':STEPS}
