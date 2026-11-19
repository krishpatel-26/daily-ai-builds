from .config import Config
def validate(c:Config):
 if not 1<=c.minutes<=10080:raise ValueError("minutes must be 1..10080")
 if c.demand<0 or c.buffer_capacity<1:raise ValueError("invalid demand or buffer capacity")
 if len(c.machines)<2:raise ValueError("at least two machines required")
 for m in c.machines:
  if min(m.cycle,m.mtbf,m.repair,m.maintenance,m.maintenance_interval)<=0:raise ValueError(f"invalid machine {m.name}")
 return c
