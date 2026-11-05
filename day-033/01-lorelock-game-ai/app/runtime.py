from .validation import validate
from .transitions import apply
_SEEN={}
def execute(p):
 if p.request_id in _SEEN:return {**_SEEN[p.request_id],"idempotent_replay":True}
 verdict=validate(p)
 if not verdict["valid"]:return {"executed":False,"validation":verdict,"idempotent_replay":False}
 out={"executed":True,"validation":verdict,"result":apply(p),"idempotent_replay":False};_SEEN[p.request_id]=out;return out
def clear():_SEEN.clear()