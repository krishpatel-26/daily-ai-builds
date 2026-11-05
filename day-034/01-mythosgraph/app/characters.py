from .database import connect
def list_characters():
 with connect() as c:return [dict(r) for r in c.execute("SELECT id,name,role FROM characters ORDER BY name")]
def get_character(cid):
 with connect() as c:r=c.execute("SELECT id,name,role FROM characters WHERE id=?",(cid,)).fetchone()
 return dict(r) if r else None