import random
from .dynamics import circular_state

def make(seed=53):
    if not 0<=seed<=999999:raise ValueError('seed out of range')
    rng=random.Random(seed)
    return {'seed':seed,'primary':{'id':'SAT-ALPHA','altitude_km':550.0,'state':circular_state(550.0,0)},'objects':[
        {'id':'DEBRIS-01','altitude_km':550.8,'state':circular_state(550.8,0.03),'class':'near-orbit'},
        {'id':'DEBRIS-02','altitude_km':560.0,'state':circular_state(560,-.55),'class':'separate-orbit'},
        {'id':'DEBRIS-03','altitude_km':545.0,'state':circular_state(545,1.5),'class':'separate-orbit'},
        {'id':'DEBRIS-04','altitude_km':575.0,'state':circular_state(575,.08),'class':'separate-orbit'},
        {'id':'DEBRIS-05','altitude_km':550.6,'state':circular_state(550.6,0.036+rng.uniform(-.008,.008)),'class':'uncertain-neighbor'}]}
