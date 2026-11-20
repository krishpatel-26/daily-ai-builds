from dataclasses import dataclass

@dataclass(frozen=True)
class Machine:
    name:str
    cycle:int
    repair_time:int
    maintenance_time:int
    base_failure_prob:float

@dataclass(frozen=True)
class Experiment:
    horizon:int=480
    buffer_capacity:int=12
    demand:int=90
    late_unit_penalty:float=85.0
    downtime_cost_per_min:float=3.0
    maintenance_cost_per_event:float=30.0
    machines:tuple[Machine,...]=(Machine('CUT',3,15,7,.004),Machine('ASSEMBLY',4,18,8,.006),Machine('QUALITY',2,10,6,.003))

POLICIES=('reactive','periodic','condition_based')

def validate(e):
    if not 1<=e.horizon<=10080 or not 1<=e.buffer_capacity<=1000 or e.demand<0:raise ValueError('Invalid experiment configuration')
    for m in e.machines:
        if not 0<m.cycle and m.repair_time>0 and m.maintenance_time>0 and 0<=m.base_failure_prob<1:raise ValueError('Invalid machine configuration')
    return e
