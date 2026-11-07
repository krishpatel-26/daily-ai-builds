from . import world,actions,rumours,rules
def tick(steps=1):
 s=world.STATE;out=[]
 for _ in range(steps):
  s["tick"]+=1;p=rumours.propagate(s);e=rules.evaluate(s);rec={"tick":s["tick"],"rumours_propagated":len(p),"emergent_events":e};s["events"].append({"type":"simulation_tick",**rec});out.append(rec)
 return out
def act(a):
 r=actions.process(world.STATE,a);r["emergent_events"]=rules.evaluate(world.STATE);return r
def status():
 s=world.STATE;return {"tick":s["tick"],"characters":list(s["characters"].values()),"relationships":list(s["relationships"].values()),"rumour_count":len(s["rumours"]),"event_count":len(s["events"]),"emergent_events":rules.evaluate(s)}