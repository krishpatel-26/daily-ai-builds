from .topology import SERVICES

def aggregate(timeline):
    return {s:[round(.6*row['metrics'][s]['latency_z']+.4*row['metrics'][s]['error_z'],5) for row in timeline] for s in SERVICES}

def peak_baseline(timeline):
    signals=aggregate(timeline)
    return sorted(SERVICES,key=lambda s:(-max(signals[s]),s))[0]

def total_anomaly(timeline):
    return round(sum(max(0,val) for arr in aggregate(timeline).values() for val in arr),3)
