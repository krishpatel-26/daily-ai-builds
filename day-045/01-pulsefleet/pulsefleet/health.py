from .detector import detect
from .models import RobotHealth
def assess_robot(robot_id,records):
 findings=detect(records[-1],records[:-1]);penalty=sum(25 if f.severity=="high" else 12 for f in findings);score=max(0,100-penalty)
 status="inspect" if any(f.severity=="high" for f in findings) else "monitor" if findings else "nominal"
 action="Schedule engineering inspection; verify manufacturer limits." if status=="inspect" else "Review trend at routine check." if status=="monitor" else "Continue routine monitoring."
 return RobotHealth(robot_id,score,status,findings,action,len(records))
def assess_fleet(grouped):return [assess_robot(k,v) for k,v in sorted(grouped.items()) if v]
