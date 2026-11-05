from .facts import conflicts
from .memory import recall
def check(subject,predicate,obj):
 found=conflicts(subject,predicate,obj)
 return {"consistent":not bool(found),"status":"conflict" if found else "no_known_conflict","proposed":{"subject":subject,"predicate":predicate,"object":obj},"conflicts":found,"guidance":"Do not state this as fact; resolve canon first." if found else "No matching contradiction found in stored canon."}
def context(cid,query):
 return {"character_id":cid,"query":query,"memories":recall(cid,query),"instruction":"Use only these memories and verified canon. If evidence is absent, ask or say you do not remember."}