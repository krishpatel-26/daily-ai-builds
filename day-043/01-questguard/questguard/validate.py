from questguard.policy import *; from questguard.grounding import grounded
def validate(s,p):
 n=p.action.value
 if n not in ALLOWED:return "ACTION_NOT_ALLOWED","Action is not allowlisted."
 if n in TARGET_REQUIRED and not p.target:return "TARGET_REQUIRED","Action requires a target."
 if not grounded(s,p):return "UNGROUNDED_PROPOSAL","Evidence is absent or unsupported."
 if p.target and p.target not in s.visible_entities and n!="complete_quest":return "TARGET_NOT_VISIBLE","Target is not visible."
 if n=="move" and p.destination not in DESTINATIONS:return "DESTINATION_INVALID","Destination is not navigable."
 if n=="open_door" and p.target not in s.locked_doors:return "DOOR_STATE_MISMATCH","Door is not locked."
 if n=="attack" and s.stamina<10:return "INSUFFICIENT_STAMINA","Insufficient stamina."
 if n=="give_item" and p.item not in s.inventory:return "ITEM_NOT_OWNED","Item not in inventory."
 if n=="complete_quest" and p.target not in s.active_quests:return "QUEST_NOT_ACTIVE","Quest is not active."
 return "ACCEPTED","All checks passed."