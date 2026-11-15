def prioritize(items,available_hours):
 ranked=sorted(items,key=lambda x:(-x["priority"],-x["risk_score"]));selected=[];deferred=[];used=0
 for x in ranked:
  (selected if used+x["duration_hours"]<=available_hours else deferred).append(x)
  if x in selected:used+=x["duration_hours"]
 return {"selected":selected,"deferred":deferred,"hours_used":round(used,2),"hours_remaining":round(available_hours-used,2)}