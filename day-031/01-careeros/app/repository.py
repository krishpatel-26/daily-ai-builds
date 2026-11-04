"""Persistence operations; SQL stays isolated from domain logic."""
import json
from .database import connection

def get_profile():
    with connection() as db:
        row = db.execute("SELECT * FROM profile WHERE id=1").fetchone()
    if not row:
        return {"name":"Your name","target_role":"AI Engineer","experience_level":"Entry level","location":"","resume_text":"","skills":[]}
    data = dict(row)
    data["skills"] = json.loads(data.pop("skills_json"))
    return data

def save_profile(data):
    with connection() as db:
        db.execute("""INSERT INTO profile(id,name,target_role,experience_level,location,resume_text,skills_json,updated_at)
        VALUES(1,?,?,?,?,?,?,CURRENT_TIMESTAMP) ON CONFLICT(id) DO UPDATE SET
        name=excluded.name,target_role=excluded.target_role,experience_level=excluded.experience_level,
        location=excluded.location,resume_text=excluded.resume_text,skills_json=excluded.skills_json,updated_at=CURRENT_TIMESTAMP""",
        (data["name"],data["target_role"],data["experience_level"],data["location"],data["resume_text"],json.dumps(data["skills"])))
    return get_profile()

def list_roadmap():
    with connection() as db:
        return [dict(r) for r in db.execute("SELECT * FROM roadmap ORDER BY sort_order,id")]

def replace_roadmap(items):
    with connection() as db:
        db.execute("DELETE FROM roadmap")
        for i, item in enumerate(items):
            db.execute("INSERT INTO roadmap(title,category,description,skill,duration,status,sort_order) VALUES(?,?,?,?,?,?,?)",
                (item["title"],item["category"],item["description"],item["skill"],item["duration"],"todo",i))
    return list_roadmap()

def update_roadmap(item_id, status):
    with connection() as db:
        cur = db.execute("UPDATE roadmap SET status=? WHERE id=?", (status,item_id))
        if cur.rowcount == 0:
            return None
        return dict(db.execute("SELECT * FROM roadmap WHERE id=?", (item_id,)).fetchone())

def list_applications():
    with connection() as db:
        return [dict(r) for r in db.execute("SELECT * FROM applications ORDER BY created_at DESC,id DESC")]

def add_application(item):
    with connection() as db:
        cur = db.execute("""INSERT INTO applications(company,role,location,stage,url,follow_up_date,notes)
        VALUES(?,?,?,?,?,?,?)""", tuple(item[k] for k in ("company","role","location","stage","url","follow_up_date","notes")))
        return dict(db.execute("SELECT * FROM applications WHERE id=?", (cur.lastrowid,)).fetchone())

def update_application(item_id, changes):
    allowed = {k:v for k,v in changes.items() if v is not None}
    if not allowed:
        return None
    fields = ", ".join(f"{k}=?" for k in allowed)
    with connection() as db:
        cur = db.execute(f"UPDATE applications SET {fields} WHERE id=?", (*allowed.values(),item_id))
        if cur.rowcount == 0:
            return None
        return dict(db.execute("SELECT * FROM applications WHERE id=?", (item_id,)).fetchone())
