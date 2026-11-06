from . import world
VALID_KINDS={"visit":"locations","collect":"items","talk":"actors","defeat":"actors","deliver":"items","discover":"locations","activate":"locations"}
def validate(q,w=None):
 w=w or world.WORLD;errors=[];warnings=[]
 if q.giver_id not in w["actors"]:errors.append("GIVER_NOT_REGISTERED")
 elif not w["actors"][q.giver_id]["alive"]:errors.append("GIVER_UNAVAILABLE")
 seen=set()
 for o in q.objectives:
  if o.objective_id in seen:errors.append("DUPLICATE_OBJECTIVE_ID")
  seen.add(o.objective_id);registry=VALID_KINDS.get(o.kind)
  if not registry:errors.append("OBJECTIVE_KIND_UNSUPPORTED");continue
  if o.target_id not in w[registry]:errors.append("TARGET_NOT_REGISTERED:"+o.target_id)
  elif registry=="actors" and not w[registry][o.target_id]["alive"]:errors.append("TARGET_UNAVAILABLE:"+o.target_id)
 for p in q.prerequisites:
  if p not in w["completed_quests"]:errors.append("PREREQUISITE_INCOMPLETE:"+p)
 if q.reward_item and q.reward_item not in w["items"]:errors.append("REWARD_ITEM_UNKNOWN")
 if q.quest_id in w["active_quests"] or q.quest_id in w["completed_quests"]:errors.append("QUEST_ALREADY_EXISTS")
 if not q.objectives:errors.append("EMPTY_OBJECTIVES")
 if q.reward_xp>500:warnings.append("HIGH_REWARD_REVIEW")
 return {"valid":not errors,"errors":errors,"warnings":warnings,"checked_objectives":len(q.objectives)}