from statistics import mean,stdev
from .dataset import split_dataset
from .model import LogisticModel
from .metrics import classify_metrics
from .drift import feature_drift
from .active import select

def one_trial(seed=51,budget=55):
    data=split_dataset(seed)
    baseline=LogisticModel().train(data['train'])
    results={'baseline':classify_metrics(baseline,data['shifted_test'])}
    for strategy in ('random','uncertainty','diversity'):
        selected=select(data['shifted_pool'],baseline,budget,strategy,seed=seed+999)
        retrained=LogisticModel().train(data['train']+selected)
        results[strategy]=classify_metrics(retrained,data['shifted_test'])
    return {'seed':seed,'budget':budget,'stable_baseline':classify_metrics(baseline,data['stable_test']),
            'shifted_baseline':results['baseline'],'results':results,
            'feature_psi':feature_drift(data['train'],data['shifted_pool']),
            'model':baseline.to_dict(),
            'review_candidates':[{'id':r.id,'features':list(r.x),
                                  'uncertainty':round(1-2*abs(baseline.predict_proba(r.x)-.5),3)} for r in select(data['shifted_pool'],baseline,min(12,budget),'uncertainty')]}

def benchmark(seeds=range(51,59),budget=55):
    trials=[one_trial(s,budget) for s in seeds]
    scores={}
    for method in ('baseline','random','uncertainty','diversity'):
        values=[t['results'][method]['f1'] for t in trials]
        sd=stdev(values) if len(values)>1 else 0.
        scores[method]={'mean_f1':round(mean(values),4),'ci95_approx':[round(mean(values)-1.96*sd/len(values)**.5,4),round(mean(values)+1.96*sd/len(values)**.5,4)],'trials':len(values)}
    return scores
