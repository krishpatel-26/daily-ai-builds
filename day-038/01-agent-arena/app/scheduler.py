from .planner import propose
from .validation import validate
def schedule(state):
 proposals=[]
 for a in state["agents"].values():
  if a["alive"]:proposals.append(propose(a,state))
 proposals.sort(key=lambda x:(-x["utility"],x["action"]["agent_id"]))
 return proposals
def resolve_conflicts(proposals,state):
 accepted=[];used=set()
 for p in proposals:
  aid=p["action"]["agent_id"]
  if aid in used:continue
  ok,reason=validate(p["action"],state)
  if ok:accepted.append(p)
  else:p["rejection"]=reason
  used.add(aid)
 return accepted