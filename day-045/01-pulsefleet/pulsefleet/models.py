from dataclasses import dataclass,asdict
from typing import Any
@dataclass(frozen=True)
class Telemetry:
 robot_id:str; timestamp:str; battery_v:float; motor_temp_c:float; vibration_mm_s:float; current_a:float; mission_id:str="unknown"
 def to_dict(self)->dict[str,Any]: return asdict(self)
@dataclass
class Finding:
 metric:str; value:float; score:float; severity:str; explanation:str
 def to_dict(self): return asdict(self)
@dataclass
class RobotHealth:
 robot_id:str; health_score:int; status:str; findings:list[Finding]; recommended_action:str; sample_count:int
 def to_dict(self): return {**asdict(self),"findings":[f.to_dict() for f in self.findings]}
