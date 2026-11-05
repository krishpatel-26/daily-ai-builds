import re
from . import world
def retrieve(question):
 words=set(re.findall(r"[a-z0-9_]+",question.lower()));hits=[]
 for d in world.STATE["lore"]:
  terms=set(re.findall(r"[a-z0-9_]+",(d["text"]+" "+" ".join(d["tags"])).lower()))
  score=len(words&terms)/max(1,len(words|terms))
  if score:hits.append({"source_id":d["id"],"text":d["text"],"score":round(score,3)})
 return sorted(hits,key=lambda x:x["score"],reverse=True)
def ground(question):
 hits=[h for h in retrieve(question) if h["score"]>=0.18]
 if not hits:return {"grounded":False,"answer":"I don't have reliable world knowledge for that. Ask the game master or explore to discover it.","sources":[],"confidence":0}
 return {"grounded":True,"answer":hits[0]["text"],"sources":[h["source_id"] for h in hits],"confidence":hits[0]["score"]}