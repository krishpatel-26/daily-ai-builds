from datetime import datetime,timezone
EVENT_WEIGHTS={'pricing_view':20,'demo_request':50,'integration_view':15,'docs_view':8,'case_study_view':10,'email_click':6}
ACTION_BY_SCORE=[(80,'Contact account executive now'),(55,'Create high-priority SDR task'),(30,'Add to nurture sequence'),(0,'Continue monitoring')]
def score(activities):
 now=datetime.now(timezone.utc); total=0; reasons=[]
 for a in activities:
  base=EVENT_WEIGHTS.get(a.event,3)*a.weight
  age=max((now-a.occurred_at).total_seconds()/86400,0)
  freshness=1/(1+age/3)
  contribution=base*freshness
  total+=contribution
  if contribution>=6: reasons.append(f'{a.event} contributed {contribution:.1f} points')
 total=min(100,round(total,1))
 action=next(text for threshold,text in ACTION_BY_SCORE if total>=threshold)
 return total,reasons,action
