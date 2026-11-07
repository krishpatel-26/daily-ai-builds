from .relationship import get
def evaluate(s):
 out=[]
 for cid in s["characters"]:
  if cid=="player":continue
  r=get(s,cid,"player")
  for axis,limit,event,op in [("trust",-20,"npc_refuses_personal_request","low"),("fear",30,"npc_avoids_player","high"),("loyalty",30,"npc_offers_support","high"),("rivalry",30,"npc_challenges_player","high")]:
   if (r[axis]<=limit if op=="low" else r[axis]>=limit):out.append({"rule":axis,"character":cid,"event":event,"reason":f"{axis} is {r[axis]}"})
 return out