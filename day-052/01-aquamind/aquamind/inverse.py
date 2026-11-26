"""Exhaustive inverse search with continuous least-squares leak magnitude fitting."""
from .network import JUNCTIONS,SENSORS
from .hydraulics import model
from .sensors import residuals

def infer(observed,noise_sd=.07):
    sensors=[s for s in SENSORS if s in observed]
    if len(sensors)<3:raise ValueError('At least three recognized pressure sensors required')
    if noise_sd<=0:raise ValueError('noise_sd must be positive')
    base=model()['pressure']
    ranked=[]
    for node in [j.id for j in JUNCTIONS]:
        at_one=model(node,1.0)['pressure']
        influence=[base[s]-at_one[s] for s in sensors]
        delta=[base[s]-observed[s] for s in sensors]
        den=sum(x*x for x in influence)
        rate=max(0,min(20,sum(x*y for x,y in zip(influence,delta))/den)) if den>0 else 0
        pred=[base[s]-rate*influence[i] for i,s in enumerate(sensors)]
        mse=sum((pred[i]-observed[s])**2 for i,s in enumerate(sensors))/len(sensors)
        ranked.append({'node':node,'estimated_rate':round(rate,4),'rmse':round(mse**.5,5),'sse':round(mse*len(sensors),6)})
    ranked.sort(key=lambda x:(x['sse'],x['node']))
    null_error=sum((base[s]-observed[s])**2 for s in sensors)
    top=ranked[0]
    return {'most_likely':top,'alternatives':ranked[:5],'all_candidates':ranked,
            'baseline_rmse':round((null_error/len(sensors))**.5,5),
            'residual_improvement_pct':round(100*(1-top['sse']/null_error),2) if null_error>0 else 0,
            'likelihood_gap_sse':round(ranked[1]['sse']-ranked[0]['sse'],6),
            'sensor_count':len(sensors),
            'caveat':'Least-squares ranking within an assumed linear network; not a calibrated leak probability or field diagnosis.'}
