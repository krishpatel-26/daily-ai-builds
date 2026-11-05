from .database import connect
CHARACTERS=[("player","The Adventurer","player"),("elder","Village Elder","npc"),("mira","Mira the Healer","npc"),("rowan","Rowan the Scout","npc"),("goblin","Cave Goblin","enemy")]
EVENTS=[("evt-001","discovery","player","elder","The adventurer discovered an ancient map beneath the village well.",8,"village","public",["elder","mira"]),("evt-002","conversation","player","mira","The adventurer promised Mira to return the silver herb before sunset.",7,"healer_hut","witnesses",["mira"]),("evt-003","combat","player","goblin","The adventurer defended the eastern path from a cave goblin.",9,"east_path","witnesses",["rowan"]),("evt-004","trade","player","elder","The adventurer traded three iron coins for a lantern.",4,"village","public",["elder"])]
FACTS=[("fact-001","silver herb","location","moonlit marsh","canon",1.0),("fact-002","ancient map","origin","beneath the village well","canon",1.0),("fact-003","eastern path","threat","goblin sightings","canon",0.95)]
def seed():
 with connect() as c:
  if c.execute("SELECT COUNT(*) FROM characters").fetchone()[0]:return
  c.executemany("INSERT INTO characters(id,name,role) VALUES(?,?,?)",CHARACTERS)
  for e in EVENTS:
   c.execute("INSERT INTO events(id,event_type,actor_id,target_id,summary,importance,location,visibility) VALUES(?,?,?,?,?,?,?,?)",e[:8])
   c.executemany("INSERT INTO witnesses(event_id,character_id) VALUES(?,?)",[(e[0],w) for w in e[8]])
  c.executemany("INSERT INTO facts(id,subject,predicate,object,source,confidence) VALUES(?,?,?,?,?,?)",FACTS)
  c.execute("INSERT INTO relationships(source_id,target_id,score) VALUES('mira','player',18)")
  c.execute("INSERT INTO relationships(source_id,target_id,score) VALUES('rowan','player',-8)")