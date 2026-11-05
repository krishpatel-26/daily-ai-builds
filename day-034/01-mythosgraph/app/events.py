from .database import connect
def record_event(e):
 with connect() as c:
  c.execute("INSERT INTO events(id,event_type,actor_id,target_id,summary,importance,location,visibility) VALUES(?,?,?,?,?,?,?,?)",(e.event_id,e.event_type,e.actor_id,e.target_id,e.summary,e.importance,e.location,e.visibility))
  witnesses=set(e.witnesses)|{e.actor_id}
  c.executemany("INSERT INTO witnesses(event_id,character_id) VALUES(?,?)",[(e.event_id,w) for w in witnesses])
  ids=witnesses
  if e.visibility=="public":ids|={r["id"] for r in c.execute("SELECT id FROM characters")}
  c.executemany("INSERT OR IGNORE INTO memories(character_id,event_id,summary,importance,source_type) VALUES(?,?,?,?,?)",[(cid,e.event_id,e.summary,e.importance,"witnessed" if cid in witnesses else "public") for cid in ids])
 return {"event_id":e.event_id,"memories_created":len(ids),"status":"recorded"}
def timeline(limit=50):
 with connect() as c:return [dict(r) for r in c.execute("SELECT * FROM events ORDER BY created_at DESC,id DESC LIMIT ?",(limit,))]