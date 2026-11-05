from .database import connect
def sentiment(s):return "hostile" if s<=-50 else "wary" if s<0 else "friendly" if s>=50 else "warm" if s>0 else "neutral"
def update(a,b,delta,reason):
 with connect() as c:
  c.execute("INSERT INTO relationships(source_id,target_id,score) VALUES(?,?,?) ON CONFLICT(source_id,target_id) DO UPDATE SET score=MAX(-100,MIN(100,score+excluded.score)),updated_at=CURRENT_TIMESTAMP",(a,b,delta))
  c.execute("INSERT INTO relationship_events(source_id,target_id,delta,reason) VALUES(?,?,?,?)",(a,b,delta,reason))
  r=c.execute("SELECT score FROM relationships WHERE source_id=? AND target_id=?",(a,b)).fetchone()
 return {"source_id":a,"target_id":b,"score":r["score"],"sentiment":sentiment(r["score"])}
def all_relationships():
 with connect() as c:return [dict(r) for r in c.execute("SELECT * FROM relationships ORDER BY score DESC")]