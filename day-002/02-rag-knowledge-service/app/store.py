import sqlite3
from pathlib import Path
class Store:
    def __init__(self,path='data/rag.db'):
        Path(path).parent.mkdir(parents=True,exist_ok=True); self.db=sqlite3.connect(path,check_same_thread=False)
        self.db.execute('create table if not exists documents(id integer primary key,title text,text text)'); self.db.commit()
    def add(self,title,text):
        cur=self.db.execute('insert into documents(title,text) values(?,?)',(title,text)); self.db.commit(); return cur.lastrowid
    def all(self): return self.db.execute('select id,title,text from documents order by id desc').fetchall()