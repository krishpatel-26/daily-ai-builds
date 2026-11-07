from .relationship import apply_delta
DELTAS={"help":{"trust":8,"loyalty":4,"fear":-1},"gift":{"trust":5,"loyalty":3},"keep_promise":{"trust":12,"loyalty":8},"lie":{"trust":-10,"rivalry":4},"betray":{"trust":-25,"loyalty":-18,"rivalry":20},"threaten":{"fear":15,"trust":-5,"rivalry":8},"insult":{"trust":-8,"rivalry":10},"defend":{"trust":10,"loyalty":8,"fear":-2}}
def process(s,a):
 if a.actor_id not in s["characters"] or a.target_id not in s["characters"]:raise ValueError("Unknown actor or target")
 if a.actor_id==a.target_id:raise ValueError("Self-directed actions unsupported")
 d={k:v*a.intensity for k,v in DELTAS[a.action].items()};r=apply_delta(s,a.actor_id,a.target_id,d);rev=apply_delta(s,a.target_id,a.actor_id,{"trust":max(-3,min(3,d.get("trust",0)//4))})
 e={"type":"social_action","actor":a.actor_id,"target":a.target_id,"action":a.action,"context":a.context,"relationship":r,"tick":s["tick"]};s["events"].append(e)
 return {"event":e,"updated":r,"reverse_effect":rev,"reasons":[f"{k} changed by {v}" for k,v in d.items()]}