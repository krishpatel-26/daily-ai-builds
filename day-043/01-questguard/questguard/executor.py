from questguard.guard import inspect
def execute(s,p):
 r=inspect(s,p)
 if not r["accepted"]:return {"executed":False,"validation":r,"state":s.model_dump()}
 t=s.model_copy(deep=True);n=p.action.value
 if n=="move":t.location=p.destination
 elif n=="attack":t.stamina=max(0,t.stamina-10)
 elif n=="open_door":t.locked_doors.remove(p.target)
 elif n=="give_item":t.inventory.remove(p.item)
 elif n=="accept_quest":t.active_quests.append(p.target)
 elif n=="complete_quest":t.active_quests.remove(p.target);t.completed_quests.append(p.target)
 t.tick+=1;return {"executed":True,"validation":r,"state":t.model_dump()}