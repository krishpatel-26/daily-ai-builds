from copy import deepcopy
SEED={"tick":1,"actors":{"player":{"id":"player","name":"Adventurer","kind":"player","alive":True,"x":0,"y":0,"flags":[]},"elder":{"id":"elder","name":"Village Elder","kind":"npc","alive":True,"x":0,"y":1,"flags":[]},"mira":{"id":"mira","name":"Mira the Healer","kind":"npc","alive":True,"x":2,"y":1,"flags":[]},"rowan":{"id":"rowan","name":"Rowan the Scout","kind":"npc","alive":True,"x":4,"y":0,"flags":[]},"goblin":{"id":"goblin","name":"Cave Goblin","kind":"enemy","alive":True,"x":8,"y":0,"flags":[]}},"locations":{"village":{"id":"village","name":"Village Square","x":0,"y":0},"marsh":{"id":"marsh","name":"Moonlit Marsh","x":6,"y":2},"cave":{"id":"cave","name":"Eastern Cave","x":8,"y":0}},"items":{"silver_herb":{"id":"silver_herb","name":"Silver Herb","available":True},"lantern":{"id":"lantern","name":"Lantern","available":True},"iron_sword":{"id":"iron_sword","name":"Iron Sword","available":True}},"flags":{"goblin_threat":True,"bridge_repaired":False,"herb_shortage":True},"active_quests":[],"completed_quests":[],"event_log":[]}
WORLD=deepcopy(SEED)
def snapshot():return deepcopy(WORLD)
def reset():
 global WORLD
 WORLD=deepcopy(SEED);return snapshot()