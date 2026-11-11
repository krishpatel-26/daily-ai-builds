from dataclasses import dataclass
@dataclass
class Player:
 id:str;team:str;pos:int;hp:int=5;energy:int=5;score:int=0;alive:bool=True
def initial_state():
 return {"step":0,"players":{"blue":Player("blue","blue",0),"red":Player("red","red",5)},"resources":{2:1,3:1},"done":False,"winner":None}
def observation(state,team):
 p=state["players"][team];o=state["players"]["red" if team=="blue" else "blue"]
 return (min(2,p.energy//2),min(2,p.hp//2),min(3,abs(p.pos-o.pos)//2),int(p.score>=o.score),int(bool(state["resources"])))
def state_key(obs):return "|".join(map(str,obs))