import random
from dataclasses import dataclass
from .config import Experiment, POLICIES, validate

@dataclass
class MachineState:
    age:int=0
    health:float=100.0
    remaining:int=0
    downtime:int=0
    failed:int=0
    repairs:int=0
    maintenance:int=0
    blocked:int=0
    busy:int=0

def shocks(seed, experiment):
    rng=random.Random(seed)
    return [[rng.random() for _ in experiment.machines] for _ in range(experiment.horizon)]

def simulate(policy='reactive',seed=47,experiment=Experiment(),interval=90,threshold=55):
    validate(experiment)
    if policy not in POLICIES:raise ValueError('Invalid policy')
    if interval<1 or not 0<threshold<100:raise ValueError('Invalid maintenance rule')
    values=shocks(seed,experiment)
    machines=experiment.machines
    states=[MachineState() for _ in machines]
    buffers=[0]*(len(machines)-1)
    produced=0
    trace=[]
    for minute in range(experiment.horizon):
        for index in reversed(range(len(machines))):
            cfg=machines[index];s=states[index]
            if s.downtime:
                s.downtime-=1
                continue
            if s.remaining:
                if index<len(machines)-1 and buffers[index]>=experiment.buffer_capacity:
                    s.blocked+=1
                    continue
                s.remaining-=1;s.busy+=1;s.age+=1;s.health=max(0,s.health-.19)
                if s.remaining==0:
                    if index==len(machines)-1:produced+=1
                    else:buffers[index]+=1
                continue
            maintain=(policy=='periodic' and s.age>=interval) or (policy=='condition_based' and s.health<=threshold)
            if maintain:
                s.downtime=cfg.maintenance_time-1;s.maintenance+=1;s.health=100;s.age=0
                continue
            probability=cfg.base_failure_prob+(1-s.health/100)*.028
            if values[minute][index]<probability:
                s.downtime=cfg.repair_time-1;s.failed+=1;s.repairs+=cfg.repair_time;s.health=100;s.age=0
                continue
            if index==0:s.remaining=cfg.cycle
            elif buffers[index-1]>0:
                buffers[index-1]-=1;s.remaining=cfg.cycle
        if minute%20==0 or minute==experiment.horizon-1:
            trace.append({'minute':minute+1,'output':produced,'buffers':list(buffers)})
    late=max(0,experiment.demand-produced)
    failed_mins=sum(s.repairs for s in states)
    maintenance_mins=sum(s.maintenance*m.maintenance_time for s,m in zip(states,machines))
    cost=late*experiment.late_unit_penalty+(failed_mins+maintenance_mins)*experiment.downtime_cost_per_min+sum(s.maintenance for s in states)*experiment.maintenance_cost_per_event
    return {'seed':seed,'policy':policy,'interval':interval,'threshold':threshold,'units_produced':produced,'demand':experiment.demand,'late_units':late,'estimated_cost':round(cost,2),'failure_events':sum(s.failed for s in states),'maintenance_events':sum(s.maintenance for s in states),'downtime_minutes':failed_mins+maintenance_mins,'buffers':buffers,'machine_states':[{'name':m.name,'health':round(s.health,1),'busy_minutes':s.busy,'utilization':round(s.busy/experiment.horizon,3),'blocked_minutes':s.blocked,'failures':s.failed,'preventive_events':s.maintenance} for m,s in zip(machines,states)],'trace':trace}
