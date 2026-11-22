from .world import make_scenario
from .dispatch import dispatch
from .metrics import evaluate

def compare(seed=48):
    s=make_scenario(seed)
    results={}
    for policy in ('shortest','risk_aware'):
        d=dispatch(s,policy)
        results[policy]={'dispatch':d,'metrics':evaluate(s,d)}
    return {'project':'CrisisMesh','scenario':s,'policies':results,'disclaimer':'Synthetic planning simulation only. No live emergency data or operational routing.'}

def benchmark(seeds=range(40,60)):
    rows=[]
    for policy in ('shortest','risk_aware'):
        metrics=[compare(seed)['policies'][policy]['metrics'] for seed in seeds]
        rows.append({'policy':policy,'seeds':len(metrics),'mean_coverage_pct':round(sum(m['coverage_pct'] for m in metrics)/len(metrics),2),'mean_arrival_min':round(sum(m['mean_arrival_min'] for m in metrics)/len(metrics),2),'mean_high_severity_coverage_pct':round(sum(m['high_severity_coverage_pct'] for m in metrics)/len(metrics),2)})
    return rows