import random
from .mathops import sigmoid

def sample(rng,client=None):
    # Distinct client feature distributions and label prevalence: non-IID by design.
    shift=0.0 if client is None else ((client % 5)-2)*0.75
    x1=rng.gauss(shift,1.0)
    x2=rng.gauss(-shift*.65,1.1)
    p=sigmoid(1.3*x1-.95*x2+0.15)
    y=1 if rng.random()<p else 0
    return (x1,x2),y

def make_dataset(seed=53, clients=9, per_client=140, test_size=700):
    if clients<5 or clients>30 or per_client<20 or test_size<100:
        raise ValueError('clients 5..30, per_client >=20, test >=100')
    rng=random.Random(seed)
    shards=[[sample(rng,c) for _ in range(per_client)] for c in range(clients)]
    test_rng=random.Random(seed+100003)
    holdout=[sample(test_rng,None) for _ in range(test_size)]
    return shards,holdout
