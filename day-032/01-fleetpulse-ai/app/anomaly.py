"""Robust anomaly indicators based on median absolute deviation."""
from statistics import median

def robust_z(value,history):
 if len(history)<5:return 0.0
 center=median(history);mad=median([abs(x-center) for x in history])
 if mad<1e-9:return 0.0 if abs(value-center)<1e-9 else 8.0
 return 0.6745*(value-center)/mad

def anomaly_signals(rows,asset):
 if not rows:return {"score":0,"signals":[],"z_scores":{}}
 recent=rows[-1];baseline=rows[:-1][-50:]
 z={}
 for key in ("temperature","vibration","pressure","current","rpm"):
  z[key]=round(robust_z(recent[key],[float(r[key]) for r in baseline]),3)
 signals=[]
 if recent["temperature"]>asset["temperature_limit"]:signals.append({"code":"TEMP_LIMIT","severity":"high","message":"Temperature exceeds configured operating limit."})
 if recent["vibration"]>asset["vibration_limit"]:signals.append({"code":"VIBRATION_LIMIT","severity":"high","message":"Vibration exceeds configured operating limit."})
 if not asset["pressure_min"]<=recent["pressure"]<=asset["pressure_max"]:signals.append({"code":"PRESSURE_OUT_OF_RANGE","severity":"high","message":"Pressure is outside configured operating range."})
 for metric,value in z.items():
  if abs(value)>=3.5:signals.append({"code":f"{metric.upper()}_ROBUST_DEVIATION","severity":"medium","message":f"{metric.title()} differs strongly from recent baseline."})
 score=min(100,len(signals)*18+sum(min(abs(v),6)*4 for v in z.values()))
 return {"score":round(score,1),"signals":signals,"z_scores":z}
