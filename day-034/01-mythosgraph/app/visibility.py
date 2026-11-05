from .database import connect
def can_know(cid,eid):
 with connect() as c:
  r=c.execute("SELECT visibility,actor_id FROM events WHERE id=?",(eid,)).fetchone()
  if not r:return False
  if r["visibility"]=="public" or r["actor_id"]==cid:return True
  return c.execute("SELECT 1 FROM witnesses WHERE event_id=? AND character_id=?",(eid,cid)).fetchone() is not None