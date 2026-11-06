from . import world
def activate(q):
 w=world.WORLD
 if any(x["quest_id"]==q["quest_id"] for x in w["active_quests"]) or q["quest_id"] in w["completed_quests"]:return {"ok":False,"reason":"QUEST_ALREADY_EXISTS"}
 w["active_quests"].append(q);w["event_log"].append({"tick":w["tick"],"type":"quest_activated","quest_id":q["quest_id"]});w["tick"]+=1
 return {"ok":True,"quest":q}
def complete(quest_id):
 w=world.WORLD;q=next((x for x in w["active_quests"] if x["quest_id"]==quest_id),None)
 if not q:return {"ok":False,"reason":"ACTIVE_QUEST_NOT_FOUND"}
 w["active_quests"].remove(q);w["completed_quests"].append(quest_id)
 w["event_log"].append({"tick":w["tick"],"type":"quest_completed","quest_id":quest_id});w["tick"]+=1
 return {"ok":True,"quest_id":quest_id,"reward_xp":q["reward_xp"]}