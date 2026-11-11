from .state import initial_state,observation
from .config import MAX_STEPS
def distance(a,b):return abs(a-b)
def step(state,actions):
 if state["done"]:return state,{"blue":0.0,"red":0.0},True
 rewards={"blue":-.02,"red":-.02};events=[]
 for team in ("blue","red"):
  p=state["players"][team];opp=state["players"]["red" if team=="blue" else "blue"];act=actions.get(team,"rest")
  if not p.alive:continue
  if act=="gather":
   node=min(state["resources"],key=lambda x:distance(p.pos,x)) if state["resources"] else None
   if node is not None and distance(p.pos,node)<=1:
    state["resources"].pop(node);p.score+=2;p.energy=max(0,p.energy-1);rewards[team]+=1.0;events.append(team+" gathered a resource")
   else:rewards[team]-=.08
  elif act=="approach":
   p.pos+=1 if opp.pos>p.pos else -1 if opp.pos<p.pos else 0;p.energy=max(0,p.energy-1);rewards[team]+=.02
  elif act=="attack":
   if distance(p.pos,opp.pos)<=1 and p.energy>=2:
    opp.hp=max(0,opp.hp-1);p.energy-=2;rewards[team]+=.35;rewards["red" if team=="blue" else "blue"]-=.25
    if opp.hp==0:opp.alive=False;rewards[team]+=1.0;events.append(team+" eliminated opponent")
   else:rewards[team]-=.12
  elif act=="rest":p.energy=min(5,p.energy+2);p.hp=min(5,p.hp+1);rewards[team]+=.04
  elif act=="guard":p.energy=min(5,p.energy+1);rewards[team]+=.01
 state["step"]+=1
 if not state["resources"] or state["step"]>=MAX_STEPS or not all(p.alive for p in state["players"].values()):
  state["done"]=True
  b=state["players"]["blue"];r=state["players"]["red"]
  state["winner"]="blue" if (b.score,b.hp)>(r.score,r.hp) else "red" if (r.score,r.hp)>(b.score,b.hp) else "draw"
  rewards[state["winner"]]+=1.0 if state["winner"]!="draw" else 0
 return state,rewards,state["done"]
def reset():return initial_state()