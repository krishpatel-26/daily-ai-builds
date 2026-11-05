from . import world
from .allowlist import RULES
from .geometry import distance
def reject(code,message,hint="Re-read the current world state and propose a supported action."):return {"valid":False,"reason_code":code,"message":message,"retry_hint":hint}
def validate(p):
 w=world.STATE;a=w["actors"].get(p.actor_id)
 if not a:return reject("ACTOR_NOT_FOUND","Actor is not in authoritative state.")
 if not a["alive"]:return reject("ACTOR_DEAD","Dead actors cannot act.")
 rule=RULES.get(p.action)
 if not rule:return reject("ACTION_NOT_ALLOWED","Action is not in server allowlist.")
 t=w["actors"].get(p.target_id) if p.target_id else None
 if rule["target"] and not t and p.target_id not in w["quests"]:return reject("TARGET_NOT_FOUND","Target is not registered.")
 if t and not t["alive"]:return reject("TARGET_UNAVAILABLE","Target is not active.")
 if t and rule["range"] and distance(a,t)>rule["range"]:return reject("OUT_OF_RANGE","Target exceeds allowed range.","Move closer or select a reachable target.")
 if p.action=="attack" and (not t or t["kind"]!="enemy"):return reject("INVALID_ATTACK_TARGET","Only registered hostile enemies can be attacked.")
 if p.action=="attack" and "rusty_sword" not in a["inventory"]:return reject("WEAPON_MISSING","No authorized weapon in inventory.")
 if p.action=="use_item":
  item=w["items"].get(p.item_id or "")
  if not item:return reject("ITEM_NOT_FOUND","Item is not in item registry.")
  if p.item_id not in a["inventory"]:return reject("ITEM_NOT_OWNED","Actor does not own item.")
  if not item["usable"]:return reject("ITEM_NOT_USABLE","Item cannot be used.")
  if p.item_id=="healing_potion" and a["hp"]>=100:return reject("HEALTH_FULL","Actor is at full health.")
 if p.action=="start_quest":
  q=w["quests"].get(p.target_id or "")
  if not q:return reject("QUEST_NOT_FOUND","Quest is not registered.")
  if not q["available"]:return reject("QUEST_UNAVAILABLE","Quest is unavailable.")
 if p.action=="move":
  dest=w["locations"].get(p.target_id or "")
  if not dest:return reject("DESTINATION_UNKNOWN","Destination is not registered.")
  if distance(a,dest)>12:return reject("DESTINATION_TOO_FAR","Destination exceeds movement limit.")
 return {"valid":True,"reason_code":"VALIDATED","message":"Passed server-side world checks.","retry_hint":None}