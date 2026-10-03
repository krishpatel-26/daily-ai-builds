import sqlite3
from pathlib import Path
class Store:
    def __init__(self,path='data/gtm.db'):
        Path(path).parent.mkdir(parents=True,exist_ok=True); self.db=sqlite3.connect(path,check_same_thread=False)
        self.db.execute('create table if not exists lead_scores(lead_id text primary key,score real,tier text,action text,updated_at text)'); self.db.commit()
    def save(self,r): self.db.execute('insert or replace into lead_scores values(?,?,?,?,?)',(r.lead_id,r.score,r.tier,r.recommended_action,r.updated_at.isoformat())); self.db.commit()
    def get(self,lead_id): return self.db.execute('select * from lead_scores where lead_id=?',(lead_id,)).fetchone()