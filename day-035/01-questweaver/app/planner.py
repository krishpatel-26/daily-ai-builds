from .catalog import TEMPLATES
from .schemas import QuestProposal,Objective
from .validation import validate
def generate(w,tone="mystery",limit=3):
 candidates=[]
 for t in TEMPLATES:
  if not w["flags"].get(t["condition"],False):continue
  if tone!="mystery" and t["tone"]!=tone:continue
  q=QuestProposal(quest_id=t["id"],title=t["title"],giver_id=t["giver"],summary=t["summary"],objectives=[Objective(objective_id=t["id"]+"_obj",**t["objective"])],reward_xp=t["reward_xp"],narrative_reason="Triggered by world flag: "+t["condition"])
  verdict=validate(q,w)
  if verdict["valid"]:
   score=.55+min(q.reward_xp,100)/500+.1
   candidates.append({"quest":q.model_dump(),"validation":verdict,"score":round(score,3),"reason":"World condition is active and all referenced entities exist."})
 candidates.sort(key=lambda x:x["score"],reverse=True)
 return candidates[:limit]