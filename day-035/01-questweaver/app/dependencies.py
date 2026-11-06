def validate_dependencies(proposals):
 ids={q.quest_id for q in proposals};errors=[]
 for q in proposals:
  for p in q.prerequisites:
   if p==q.quest_id:errors.append("SELF_DEPENDENCY:"+q.quest_id)
   elif p in ids:errors.append("DEPENDENCY_CYCLE_RISK:"+q.quest_id+":"+p)
 return {"valid":not errors,"errors":errors,"nodes":len(ids)}