from . import world,planner,scheduler,actions
from .validation import validate
def run_turn():
 s=world.STATE;s["turn"]+=1;proposals=scheduler.schedule(s);accepted=scheduler.resolve_conflicts(proposals,s);events=[]
 for p in accepted:
  ok,reason=validate(p["action"],s)
  if not ok:events.append({"type":"rejected","reason":reason,"proposal":p});continue
  result=actions.apply(p["action"],s);event={"type":"action_resolved","turn":s["turn"],"utility":p["utility"],**result};s["log"].append(event);events.append(event)
 return {"turn":s["turn"],"proposals":proposals,"events":events,"state":world.snapshot()}
def run(steps=1):return [run_turn() for _ in range(steps)]
def replay():return list(world.STATE["log"])