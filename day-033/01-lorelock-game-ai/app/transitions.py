from . import world
def apply(p):
 w=world.STATE;a=w["actors"][p.actor_id];t=w["actors"].get(p.target_id) if p.target_id else None;effect="interaction recorded"
 if p.action=="move":
  d=w["locations"][p.target_id];a["x"],a["y"]=d["x"],d["y"];effect="moved to registered location"
 elif p.action=="attack":
  damage=w["items"]["rusty_sword"]["damage"];t["hp"]=max(0,t["hp"]-damage)
  if t["hp"]==0:t["alive"]=False
  effect=f"server applied {damage} damage"
 elif p.action=="use_item":
  item=w["items"][p.item_id];a["hp"]=min(100,a["hp"]+item["heal"]);a["inventory"].remove(p.item_id);effect="server applied healing"
 elif p.action=="start_quest":a["quest_flags"].append(p.target_id);effect="quest flag recorded"
 event={"tick":w["tick"],"request_id":p.request_id,"actor_id":p.actor_id,"action":p.action,"target_id":p.target_id,"effect":effect}
 w["event_log"].append(event);w["tick"]+=1
 return {"event":event,"world":world.snapshot()}