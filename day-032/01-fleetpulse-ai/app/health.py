"""Explainable asset health scoring and maintenance recommendations."""
from .features import rolling_features
from .anomaly import anomaly_signals

def assess(asset,rows):
 if not rows:
  return {"asset_id":asset["asset_id"],"health_index":None,"status":"no_data","priority":"unknown","anomaly_score":0,"reasons":["No telemetry available."],"features":None,"signals":[]}
 features=rolling_features(rows);anomaly=anomaly_signals(rows,asset)
 signals=anomaly["signals"];reasons=[s["message"] for s in signals]
 latest=rows[-1];metrics=features["metrics"]
 trend_penalty=sum(8 for m in ("temperature","vibration") if metrics[m]["slope"]>0.05)
 raw=100-anomaly["score"]*0.55-trend_penalty
 health=round(max(0,min(100,raw)),1)
 if anomaly["score"]>=70 or health<45:status,priority="critical","critical"
 elif anomaly["score"]>=40 or health<65:status,priority="degraded","high"
 elif anomaly["score"]>=20 or health<80:status,priority="watch","medium"
 else:status,priority="healthy","low"
 if not reasons:reasons.append("No configured limits breached and no strong robust deviations detected.")
 if trend_penalty:reasons.append("Increasing temperature/vibration trend added a precautionary penalty.")
 action={"critical":"Inspect asset promptly under site safety procedures; verify sensor integrity.","high":"Schedule maintenance assessment and inspect relevant operating conditions.","medium":"Increase monitoring frequency and review trends.","low":"Continue routine monitoring and scheduled preventive maintenance."}[priority]
 return {"asset_id":asset["asset_id"],"health_index":health,"status":status,"priority":priority,"anomaly_score":anomaly["score"],"reasons":reasons,"signals":signals,"features":features,"recommendation":action,"latest":latest}
