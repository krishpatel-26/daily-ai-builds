def fleet_summary(items):
 counts={k:sum(x["risk_level"]==k for x in items) for k in ["HIGH","MEDIUM","LOW"]}
 return {"machine_count":len(items),"risk_counts":counts,"fleet_risk_score":round(sum(x["risk_score"] for x in items)/max(1,len(items)),4),"high_risk_machines":[x["machine_id"] for x in items if x["risk_level"]=="HIGH"]}