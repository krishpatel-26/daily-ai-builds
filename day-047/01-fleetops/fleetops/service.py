from .simulator import FleetSimulation
from .benchmark import compare

def report(seed=47,ticks=110):
    r=FleetSimulation(seed,ticks,True).run()
    r['benchmark']=compare()
    r['limitations']='Synthetic discrete grid; no live robot integration, safety certification or complete MAPF guarantees.'
    return r
