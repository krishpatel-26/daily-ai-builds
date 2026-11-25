"""Fictional inspection embeddings; not camera imagery or real defect labels."""
from dataclasses import dataclass
import random, math

FEATURES=('contrast','texture','edge','brightness')
@dataclass(frozen=True)
class Sample:
    id:str
    x:tuple[float,...]
    y:int
    group:str='stable'

def generate(seed=51,n=300,shift=0.0,group='stable'):
    if not 0<=shift<=2 or n<1:raise ValueError('invalid dataset parameters')
    rng=random.Random(seed)
    result=[]
    for i in range(n):
        # Covariate drift and gradual concept drift in a fictional inspection process.
        x=(rng.gauss(.20+.58*shift,1),rng.gauss(-.12+.35*shift,1.1),
           rng.gauss(.06-.30*shift,.9),rng.gauss(.10+.52*shift,1.0))
        latent=1.25*x[0]+1.38*x[1]+.76*x[2]-.55*x[3]-0.35*shift+ rng.gauss(0,.95)
        label=int(latent>0.15)
        result.append(Sample(f'{group}-{seed}-{i:04}',tuple(round(v,5) for v in x),label,group))
    return result

def split_dataset(seed=51):
    return {'train':generate(seed,200,0,'training'),
            'stable_test':generate(seed+100,180,0,'stable'),
            'shifted_pool':generate(seed+200,400,1.25,'pool'),
            'shifted_test':generate(seed+300,180,1.25,'shifted')}
