def duplicate_check(q,active,completed):
 for e in active+completed:
  if e.get("quest_id")==q.quest_id:return {"duplicate":True,"reason":"QUEST_ID_ALREADY_USED"}
  a={(o.get("kind"),o.get("target_id")) for o in e.get("objectives",[])}
  b={(o.kind,o.target_id) for o in q.objectives}
  if a and a==b:return {"duplicate":True,"reason":"OBJECTIVE_PATTERN_ALREADY_USED"}
 return {"duplicate":False,"reason":None}