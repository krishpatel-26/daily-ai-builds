from .statistics import median
METRICS=("battery_v","motor_temp_c","vibration_mm_s","current_a")
def rolling_features(records,window=10):
 result=[]
 for i,r in enumerate(records):
  prior=records[max(0,i-window):i];row={"robot_id":r.robot_id,"timestamp":r.timestamp,"sample_index":i}
  for metric in METRICS:
   vals=[getattr(x,metric) for x in prior];base=median(vals) if vals else getattr(r,metric)
   row[f"{metric}_baseline"]=base;row[f"{metric}_delta"]=getattr(r,metric)-base
  result.append(row)
 return result
