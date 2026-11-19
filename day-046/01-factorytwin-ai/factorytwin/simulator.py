import random
from dataclasses import dataclass
from .config import Config
from .validation import validate
@dataclass
class State:
 busy:int=0; down:int=0; maintained:int=0; age:int=0; work:int=0; failures:int=0; maintenance_events:int=0; produced:int=0; blocked:int=0

def simulate(config:Config=Config(),policy="reactive",interval_scale=1.0):
 validate(config)
 if policy not in ("reactive","preventive"):raise ValueError("unknown policy")
 if interval_scale<=0:raise ValueError("interval_scale must be positive")
 rng=random.Random(config.seed);machines=config.machines;states=[State() for _ in machines];buffers=[0]*(len(machines)-1);output=0;trace=[]
 for minute in range(config.minutes):
  for i in reversed(range(len(machines))):
   m=machines[i];s=states[i]
   if s.down>0:s.down-=1;continue
   if s.maintained>0:s.maintained-=1;continue
   if s.busy>0:
    s.busy-=1;s.work+=1;s.age+=1
    if s.busy==0:
     if i==len(machines)-1:output+=1;s.produced+=1
     elif buffers[i]<config.buffer_capacity:buffers[i]+=1;s.produced+=1
     else:s.busy=1;s.blocked+=1
    continue
   if policy=="preventive" and s.age>=max(1,int(m.maintenance_interval*interval_scale)):
    s.maintained=m.maintenance;s.maintenance_events+=1;s.age=0;continue
   if rng.random()<1/m.mtbf:
    s.down=m.repair;s.failures+=1;s.age=0;continue
   if i==0:s.busy=m.cycle
   elif buffers[i-1]>0:buffers[i-1]-=1;s.busy=m.cycle
  if minute%30==0 or minute==config.minutes-1:trace.append({"minute":minute+1,"completed":output,"buffers":buffers.copy()})
 total_down=sum(s.failures*machines[i].repair+s.maintenance_events*machines[i].maintenance for i,s in enumerate(states))
 late=max(0,config.demand-output)
 cost=total_down*config.downtime_cost+sum(buffers)*config.unit_holding_cost+late*config.unit_revenue
 return {"policy":policy,"interval_scale":interval_scale,"completed":output,"demand":config.demand,"late_units":late,"estimated_cost":round(cost,2),"downtime_minutes":total_down,"machines":[{"name":m.name,"failures":s.failures,"maintenance_events":s.maintenance_events,"work_minutes":s.work,"utilization":round(s.work/config.minutes,3),"blocked_minutes":s.blocked,"produced":s.produced} for m,s in zip(machines,states)],"trace":trace}
