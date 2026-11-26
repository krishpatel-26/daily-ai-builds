"""Topology-and-time template matching, using least-squares amplitude fitting."""
from .topology import SERVICES,downstream_hops
from .kernel import effect
from .signals import aggregate,peak_baseline

def rank_roots(timeline,possible_starts=range(11,21)):
    if not timeline:raise ValueError('timeline is empty')
    observed=aggregate(timeline)
    entries=[]
    for root in SERVICES:
        hops=downstream_hops(root)
        best=None
        for start in possible_starts:
            cross=energy=0.0
            # Fit an unknown amplitude; zeros outside the expected downstream footprint.
            for service in SERVICES:
                distance=hops.get(service)
                if distance is None:continue
                for t,y in enumerate(observed[service]):
                    k=.96*effect(distance,t,start)
                    cross+=k*y;energy+=k*k
            amplitude=max(0,min(20,cross/energy)) if energy else 0
            residual=0
            for service in SERVICES:
                distance=hops.get(service)
                for t,y in enumerate(observed[service]):
                    pred=amplitude*.96*effect(distance,t,start) if distance is not None else 0
                    residual+=(y-pred)**2
            candidate={'service':root,'estimated_start':start,'estimated_strength':round(amplitude,3),'sse':round(residual,4)}
            if best is None or candidate['sse']<best['sse']:best=candidate
        entries.append(best)
    return sorted(entries,key=lambda x:(x['sse'],x['service']))

def diagnose(timeline):
    rankings=rank_roots(timeline)
    return {'most_likely':rankings[0],'alternatives':rankings[:5],'all_candidates':rankings,
            'naive_peak_candidate':peak_baseline(timeline),
            'fit_gap':round(rankings[1]['sse']-rankings[0]['sse'],4),
            'disclaimer':'Model-matched root hypothesis only; no real-world causal identification.'}
