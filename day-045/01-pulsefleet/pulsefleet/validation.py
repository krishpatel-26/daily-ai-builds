from datetime import datetime
from .models import Telemetry
LIMITS={"battery_v":(0,100),"motor_temp_c":(-20,180),"vibration_mm_s":(0,100),"current_a":(0,500)}
def parse_record(raw):
 required=("robot_id","timestamp",*LIMITS.keys()); missing=[k for k in required if k not in raw]
 if missing: raise ValueError("Missing fields: "+", ".join(missing))
 rid=str(raw["robot_id"]).strip()
 if not rid or len(rid)>64: raise ValueError("robot_id must contain 1–64 characters")
 try: datetime.fromisoformat(str(raw["timestamp"]).replace("Z","+00:00"))
 except ValueError as exc: raise ValueError("timestamp must be ISO-8601") from exc
 values={}
 for key,(lo,hi) in LIMITS.items():
  try: value=float(raw[key])
  except (TypeError,ValueError) as exc: raise ValueError(f"{key} must be numeric") from exc
  if not lo<=value<=hi: raise ValueError(f"{key} outside accepted range [{lo}, {hi}]")
  values[key]=value
 return Telemetry(rid,str(raw["timestamp"]),**values,mission_id=str(raw.get("mission_id","unknown"))[:80])
