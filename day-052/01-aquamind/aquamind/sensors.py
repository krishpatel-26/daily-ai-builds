import random
from .network import SENSORS
from .hydraulics import model

def observe(leak_node='J-07',leak_rate=4.5,seed=52,noise_sd=0.07):
    if noise_sd<0 or noise_sd>5:raise ValueError('noise_sd must be 0..5')
    rng=random.Random(seed)
    truth=model(leak_node,leak_rate)
    return {name:round(truth['pressure'][name]+rng.gauss(0,noise_sd),5) for name in SENSORS}

def residuals(observations,predictions):
    keys=sorted(set(observations)&set(predictions))
    if not keys:raise ValueError('No overlapping sensors')
    return {k:round(observations[k]-predictions[k],6) for k in keys}
