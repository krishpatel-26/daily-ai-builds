from .database import connect
from .text import similarity
from .config import MEMORY_LIMIT,MIN_RELEVANCE
def recall(cid,query,limit=8):
 with connect() as c:rows=c.execute("SELECT m.*,e.event_type,e.location,e.created_at AS event_time FROM memories m JOIN events e ON e.id=m.event_id WHERE m.character_id=? ORDER BY e.created_at DESC",(cid,)).fetchall()
 out=[]
 for r in rows:
  d=dict(r);rel=similarity(query,d["summary"]);score=.65*rel+.25*d["importance"]/10+.10
  if score>=MIN_RELEVANCE:d.update(relevance=round(rel,3),score=round(score,3));out.append(d)
 out.sort(key=lambda x:(x["score"],x["event_time"]),reverse=True)
 return out[:min(limit,MEMORY_LIMIT)]
def stats():
 with connect() as c:return {"events":c.execute("SELECT COUNT(*) FROM events").fetchone()[0],"memories":c.execute("SELECT COUNT(*) FROM memories").fetchone()[0],"characters":c.execute("SELECT COUNT(*) FROM characters").fetchone()[0]}