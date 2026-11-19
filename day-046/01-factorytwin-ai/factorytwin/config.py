from dataclasses import dataclass
@dataclass(frozen=True)
class Machine:
 name:str; cycle:int; mtbf:int; repair:int; maintenance:int; maintenance_interval:int
@dataclass(frozen=True)
class Config:
 minutes:int=480; seed:int=42; demand:int=120; unit_revenue:float=75; unit_holding_cost:float=.1; downtime_cost:float=2
 machines:tuple=(Machine("CUT",3,150,12,6,180),Machine("ASSEMBLE",4,120,15,8,160),Machine("QA",2,200,10,5,210))
 buffer_capacity:int=10
