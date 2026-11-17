from .statistics import robust_z
from .models import Finding
from .features import METRICS
THRESHOLDS={"battery_v":22.0,"motor_temp_c":75.0,"vibration_mm_s":8.0,"current_a":18.0}
def detect(record,history):
 findings=[]
 for metric in METRICS:
  value=getattr(record,metric);baseline=[getattr(x,metric) for x in history[-30:]];z=robust_z(value,baseline)
  absolute=metric!="battery_v" and value>THRESHOLDS[metric];low=metric=="battery_v" and value<THRESHOLDS[metric]
  if abs(z)>=3.5 or absolute or low:
   severity="high" if abs(z)>=6 or (metric=="motor_temp_c" and value>=90) else "medium"
   why=f"{metric}={value:.2f}; robust deviation={z:.2f}"
   if absolute or low:why+=f"; illustrative threshold={THRESHOLDS[metric]:.1f}"
   findings.append(Finding(metric,round(value,3),round(abs(z),2),severity,why))
 return findings
