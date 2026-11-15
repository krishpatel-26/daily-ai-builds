def estimate_impact(risk,throughput,buffer_hours=2):
 exposure=max(0,1-buffer_hours/24)
 return {"downtime_exposure_hours":round(risk*8*exposure,2),"throughput_at_risk_percent":round(min(100,risk*max(0,100-throughput)),2),"buffer_hours":buffer_hours}