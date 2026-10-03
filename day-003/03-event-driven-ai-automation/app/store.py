import sqlite3
from datetime import datetime,timezone
class EventStore:
 def __init__(self,path='automation.db'):
  self.db=path
  with sqlite3.connect(path) as c:
   c.execute('CREATE TABLE IF NOT EXISTS processed(k TEXT PRIMARY KEY,event_id TEXT,created_at TEXT)'); c.execute('CREATE TABLE IF NOT EXISTS audit(event_id TEXT,action TEXT,status TEXT,detail TEXT,created_at TEXT)')
 def seen(self,key):
  with sqlite3.connect(self.db) as c:return c.execute('SELECT 1 FROM processed WHERE k=?',(key,)).fetchone() is not None
 def mark(self,key,eid):
  with sqlite3.connect(self.db) as c:c.execute('INSERT OR IGNORE INTO processed VALUES(?,?,?)',(key,eid,datetime.now(timezone.utc).isoformat()))
 def audit(self,eid,action,status,detail=''):
  with sqlite3.connect(self.db) as c:c.execute('INSERT INTO audit VALUES(?,?,?,?,?)',(eid,action,status,detail,datetime.now(timezone.utc).isoformat()))
