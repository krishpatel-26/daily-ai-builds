import random
from .environment import reset,step
from .agents import act,heuristic,random_action
from .state import observation,state_key
def evaluate(q_tables,episodes=40,seed=101,opponent="heuristic"):
 rng=random.Random(seed);wins={"blue":0,"red":0,"draw":0};rewards={"blue":0.0,"red":0.0};scores={"blue":0,"red":0}
 for _ in range(episodes):
  s=reset();done=False
  while not done:
   a=act(s,"blue",q_tables["blue"],0,rng)
   b=heuristic(s,"red") if opponent=="heuristic" else random_action(rng)
   s,r,done=step(s,{"blue":a,"red":b})
   for t in rewards:rewards[t]+=r[t]
  wins[s["winner"]]+=1
  for t in scores:scores[t]+=s["players"][t].score
 return {"episodes":episodes,"opponent":opponent,"wins":wins,"win_rate":round(wins["blue"]/episodes,3),"mean_reward":{k:round(v/episodes,3) for k,v in rewards.items()},"mean_score":{k:round(v/episodes,3) for k,v in scores.items()},"seed":seed}