from .templates import TEMPLATES
from .scoring import score
from .branches import choose
from .validator import validate_template
def plan(state,completed=None,limit=5):
 completed=set(completed or []);ranked=[]
 for t in TEMPLATES:
  if t["id"] in completed:continue
  valid,errors=validate_template(t)
  if not valid:continue
  value,reasons=score(t,state);branch=choose(t,state)
  ranked.append({"quest_id":t["id"],"title":t["title"],"theme":t["theme"],"description":t["description"],"score":value,"reasons":reasons,"objectives":t["objectives"],"selected_route":branch[0] if branch else None,"status":"recommended" if value>=t["priority"] else "conditional"})
 ranked.sort(key=lambda x:(-x["score"],x["quest_id"]))
 return {"recommendations":ranked[:limit],"evaluated_templates":len(TEMPLATES),"excluded_completed":len(completed)}