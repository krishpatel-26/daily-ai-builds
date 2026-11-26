from .sensors import observe
from .inverse import infer
from .network import JUNCTIONS

def benchmark(seeds=range(25),noise_sd=.07):
    rows=[]
    for seed in seeds:
        for j in JUNCTIONS:
            rate=3.0+seed%5*.5
            observations=observe(j.id,rate,seed,noise_sd)
            result=infer(observations,noise_sd)
            rows.append({'actual':j.id,'predicted':result['most_likely']['node'],'rate':rate,
                         'estimated_rate':result['most_likely']['estimated_rate'],
                         'correct':result['most_likely']['node']==j.id})
    if not rows:raise ValueError('seeds must be nonempty')
    n=len(rows);accuracy=sum(x['correct'] for x in rows)/n
    mae=sum(abs(x['estimated_rate']-x['rate']) for x in rows)/n
    return {'trials':n,'seeds':len(set(seeds)) if isinstance(seeds,range) else None,
            'top1_node_accuracy':round(accuracy,4),'leak_rate_mae':round(mae,4),
            'naive_location_accuracy':round(1/len(JUNCTIONS),4),
            'note':'Synthetic, model-matched test: inverse model and data generator share assumptions; results do not generalize to actual water utilities.'}

def noise_sweep(levels=(.07,.3,.5,1.0),seeds=range(15)):
    return [{'sensor_noise_sd':noise,**benchmark(seeds=seeds,noise_sd=noise)} for noise in levels]
