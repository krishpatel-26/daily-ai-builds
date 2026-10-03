import sqlite3
from datetime import datetime,timezone
from pathlib import Path
class MemoryStore:
 def __init__(self,path):
  self.path=Path(path); self.path.parent.mkdir(parents=True,exist_ok=True)
  with self._connect() as db:
   db.execute('CREATE TABLE IF NOT EXISTS memories (id INTEGER PRIMARY KEY AUTOINCREMENT,user_id TEXT NOT NULL,agent_id TEXT NOT NULL,content TEXT NOT NULL,kind TEXT NOT NULL,importance REAL NOT NULL,created_at TEXT NOT NULL,UNIQUE(user_id,agent_id,content))')
   db.execute('CREATE INDEX IF NOT EXISTS idx_memory_scope ON memories(user_id,agent_id)')
 def _connect(self):
  db=sqlite3.connect(self.path); db.row_factory=sqlite3.Row; return db
 def add(self,data):
  now=datetime.now(timezone.utc).isoformat()
  with self._connect() as db:
   db.execute('INSERT OR IGNORE INTO memories(user_id,agent_id,content,kind,importance,created_at) VALUES(?,?,?,?,?,?)',(data.user_id,data.agent_id,data.content,data.kind,data.importance,now))
   row=db.execute('SELECT * FROM memories WHERE user_id=? AND agent_id=? AND content=?',(data.user_id,data.agent_id,data.content)).fetchone()
  return dict(row)
 def list(self,user_id,agent_id):
  with self._connect() as db: rows=db.execute('SELECT * FROM memories WHERE user_id=? AND agent_id=? ORDER BY created_at DESC',(user_id,agent_id)).fetchall()
  return [dict(r) for r in rows]
 def search(self,user_id,agent_id,query,limit):
  terms={t.lower() for t in query.split() if len(t)>2}; rows=self.list(user_id,agent_id); now=datetime.now(timezone.utc)
  def score(r):
   hits=sum(t in r['content'].lower() for t in terms); age=max((now-datetime.fromisoformat(r['created_at'])).total_seconds(),0); return hits*3+r['importance']*2+1/(1+age/86400)
  return sorted(rows,key=score,reverse=True)[:limit]
