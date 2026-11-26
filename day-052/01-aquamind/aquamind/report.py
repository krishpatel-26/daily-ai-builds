from .network import graph_payload
from .hydraulics import model
from .sensors import observe,residuals
from .inverse import infer
from .benchmark import benchmark,noise_sweep

def report(leak_node='J-07',leak_rate=4.5,seed=52,noise_sd=.07,include_benchmark=True):
    baseline=model();truth=model(leak_node,leak_rate)
    readings=observe(leak_node,leak_rate,seed,noise_sd)
    diagnosis=infer(readings,noise_sd)
    return {'project':'AquaMind','network':graph_payload(),'scenario':{'leak_node':leak_node,'leak_rate':leak_rate,'seed':seed,'noise_sd':noise_sd},
            'baseline':baseline,'truth':truth,'readings':readings,
            'pressure_residuals':residuals(readings,baseline['pressure']),
            'diagnosis':diagnosis,'benchmark':benchmark() if include_benchmark else None,'noise_sweep':noise_sweep() if include_benchmark else None,
            'disclaimer':'Synthetic linear conductive analogy, not validated hydraulic modeling or live leak detection.'}
