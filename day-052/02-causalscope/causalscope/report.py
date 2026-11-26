from .topology import topology
from .simulator import simulate
from .infer import diagnose
from .evidence import evidence_trace
from .counterfactual import remove_injected_fault
from .benchmark import benchmark

def report(root='database',seed=52,strength=2.7,noise_sd=.19,include_benchmark=True):
    scenario=simulate(root,seed,strength,noise_sd)
    d=diagnose(scenario['timeline'])
    return {'project':'CausalScope','topology':topology(),'scenario':{k:v for k,v in scenario.items() if k!='timeline'},
            'timeline':scenario['timeline'],'diagnosis':d,
            'evidence_trace':evidence_trace(scenario['timeline'],d['most_likely']['service']),
            'counterfactual':remove_injected_fault(root,seed,strength,noise_sd),
            'benchmark':benchmark() if include_benchmark else None,
            'disclaimer':'Synthetic graph-based root-cause hypothesis. No production incident records or causal certification.'}
