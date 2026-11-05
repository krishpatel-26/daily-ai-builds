from .database import connect
def add(f):
 with connect() as c:c.execute("INSERT INTO facts(id,subject,predicate,object,source,confidence) VALUES(?,?,?,?,?,?)",(f.fact_id,f.subject,f.predicate,f.object,f.source,f.confidence))
 return {"fact_id":f.fact_id,"status":"stored"}
def all_facts():
 with connect() as c:return [dict(r) for r in c.execute("SELECT * FROM facts ORDER BY subject")]
def conflicts(subject,predicate,obj):
 with connect() as c:rows=[dict(r) for r in c.execute("SELECT * FROM facts WHERE lower(subject)=lower(?) AND lower(predicate)=lower(?)",(subject,predicate))]
 return [r for r in rows if r["object"].lower()!=obj.lower()]