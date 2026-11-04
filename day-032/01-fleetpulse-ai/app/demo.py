"""Generate a repeatable synthetic fleet dataset for local demonstration."""
import math,random
from datetime import datetime,timedelta,timezone
from . import repository
from .schemas import AssetCreate,TelemetryInput

DEMO_ASSETS=[
 {"asset_id":"PUMP-101","name":"Cooling Water Pump 101","asset_type":"centrifugal_pump","location":"Plant A / Line 1","criticality":"critical"},
 {"asset_id":"MOTOR-204","name":"Conveyor Drive Motor 204","asset_type":"electric_motor","location":"Plant A / Line 2","criticality":"high"},
 {"asset_id":"COMP-307","name":"Air Compressor 307","asset_type":"compressor","location":"Plant B / Utilities","criticality":"high"},
 {"asset_id":"FAN-410","name":"Exhaust Fan 410","asset_type":"industrial_fan","location":"Plant B / Line 4","criticality":"medium"}
]
def seed_demo():
 rng=random.Random(32);created=[]
 for idx,raw in enumerate(DEMO_ASSETS):
  try:asset=repository.add_asset(AssetCreate(**raw).model_dump());created.append(asset)
  except Exception:
   asset=repository.get_asset(raw["asset_id"])
  prior=repository.telemetry_for(raw["asset_id"],1)
  if prior:continue
  for i in range(80):
   drift=max(0,(i-55)/25) if idx==0 else max(0,(i-72)/8) if idx==2 else 0
   row={"timestamp":(datetime.now(timezone.utc)-timedelta(minutes=(79-i)*10)).isoformat(),
   "temperature":round(55+idx*3+drift*24+rng.uniform(-1.5,1.5),2),
   "vibration":round(2.1+drift*5.4+rng.uniform(-.18,.18),3),
   "pressure":round(4.5+(.2 if idx==1 else 0)+rng.uniform(-.15,.15),2),
   "current":round(9+idx+drift*2+rng.uniform(-.3,.3),2),
   "rpm":round(1450+rng.uniform(-8,8),1),"runtime_hours":round(1200+i/6,2)}
   repository.add_telemetry(raw["asset_id"],row)
 return {"assets_seeded":len(created),"telemetry_points":sum(len(repository.telemetry_for(a["asset_id"])) for a in DEMO_ASSETS)}
