import random
from .models import STORES

def demand_stream(seed: int, days: int, disrupted=True):
    rng=random.Random(seed)
    stream=[]
    for day in range(days):
        surge=1.35 if disrupted and 30<=day<50 else 1.0
        stream.append({s.id:max(0,round(rng.gauss(s.avg_demand*surge,s.avg_demand*.17))) for s in STORES})
    return stream

def availability(source, day, disrupted=True):
    if source=='SOURCE-A' and disrupted and 22<=day<44:return .20
    return 1.0
