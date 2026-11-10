from .policies import score
from .validation import validate
ACTIONS=("gather","guard","rest","trade","attack")
def candidates(agent,state):
 rows=[]
 for kind in ACTIONS:
  action={"agent_id":agent["id"],"action":kind,"priority":1}
  if kind=="attack":
   enemies=[x for x in state["agents"].values() if x["alive"] and x["team"]!=agent["team"]]
   if enemies:action["target"]=min(enemies,key=lambda x:(x["hp"],x["id"]))["id"]
  ok,reason=validate(action,state)
  if ok:rows.append({"action":action,"utility":score(agent,action,state),"reason":"policy_utility"})
 return sorted(rows,key=lambda x:(-x["utility"],x["action"]["action"]))
def propose(agent,state):
 rows=candidates(agent,state)
 return rows[0] if rows else {"action":{"agent_id":agent["id"],"action":"rest"},"utility":0,"reason":"fallback"}