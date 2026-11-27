from .experiments import compare,benchmark

def build(seed=53,rounds=18):
    if not 0<=seed<=999999:raise ValueError('seed must be 0..999999')
    cases=compare(seed,rounds)
    return {'name':'FederateLab','inputs':{'seed':seed,'rounds':rounds,'clients':9,'poisoned_clients':2,'features':2},'experiments':cases,'benchmark':benchmark(rounds=rounds),'disclaimer':'Synthetic data only. No secure aggregation, differential privacy or real adversarial guarantees.'}
