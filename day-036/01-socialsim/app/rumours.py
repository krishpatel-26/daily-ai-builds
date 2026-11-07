from .config import RUMOUR_DECAY,MAX_HOPS
def create(s,d):
 if d.source_id not in s["characters"] or d.subject_id not in s["characters"]:raise ValueError("Unknown rumour participant")
 r={"id":"rumour-"+str(len(s["rumours"])+1),"source":d.source_id,"subject":d.subject_id,"claim":d.claim,"confidence":d.confidence,"audience":list(dict.fromkeys(d.audience)),"hops":0,"tick":s["tick"]};s["rumours"].append(r);return r
def propagate(s):
 out=[]
 for r in list(s["rumours"]):
  if r["hops"]>=MAX_HOPS:continue
  for listener in (r["audience"] or [x for x in s["characters"] if x not in (r["source"],r["subject"])]):
   conf=round(r["confidence"]*RUMOUR_DECAY,3);rid=r["id"]+"-"+listener
   if listener in s["characters"] and conf>=.15 and not any(x["id"]==rid for x in s["rumours"]):out.append({"id":rid,"source":listener,"subject":r["subject"],"claim":r["claim"],"confidence":conf,"audience":[],"hops":r["hops"]+1,"tick":s["tick"]})
 s["rumours"].extend(out);return out