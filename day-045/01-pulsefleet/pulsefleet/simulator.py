import random
from datetime import datetime,timedelta,timezone
from .models import Telemetry
def generate_fleet(seed=7,robots=6,samples=48):
 rng=random.Random(seed);start=datetime(2026,11,18,tzinfo=timezone.utc);out=[]
 for r in range(robots):
  rid=f"AMR-{r+1:02d}"
  for i in range(samples):
   fault=r==2 and i>=samples-8
   out.append(Telemetry(rid,(start+timedelta(minutes=15*i)).isoformat(),round(rng.gauss(25.2 if not fault else 23.5,.35),2),round(rng.gauss(48 if not fault else 82,2.5),2),round(rng.gauss(2.2 if not fault else 10.5,.45),2),round(rng.gauss(7.5 if not fault else 20,.8),2),f"MISSION-{i//4:03d}"))
 return out
