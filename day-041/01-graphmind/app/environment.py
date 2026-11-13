import numpy as np
from .config import N_AGENTS,HORIZON
class CorridorEnv:
 def __init__(self,seed=7): self.rng=np.random.default_rng(seed); self.goals=np.array([1,3,6,8]); self.reset()
 def reset(self):
  self.pos=np.array([0,9,2,7],dtype=np.int64); self.t=0; return self.observe()
 def observe(self):
  out=[]
  for i in range(N_AGENTS):
   d=self.goals[i]-self.pos[i]; nearest=min(abs(self.pos[i]-self.pos[j]) for j in range(N_AGENTS) if j!=i)
   out.append([self.pos[i]/9,self.goals[i]/9,d/9,abs(d)/9,nearest/9,self.t/HORIZON])
  return np.asarray(out,dtype=np.float32)
 def step(self,actions):
  old=np.abs(self.goals-self.pos); delta=np.asarray(actions,dtype=np.int64)-1; self.pos=np.clip(self.pos+delta,0,9); self.t+=1
  new=np.abs(self.goals-self.pos); progress=(old-new)*.12; collision=np.zeros(N_AGENTS,dtype=np.float32)
  for i in range(N_AGENTS):
   for j in range(i+1,N_AGENTS):
    if self.pos[i]==self.pos[j]: collision[i]-=.25;collision[j]-=.25
  reached=(self.pos==self.goals); reward=progress.astype(np.float32)+collision-.025
  reward+=reached.astype(np.float32)*.25
  done=bool(reached.all() or self.t>=HORIZON)
  if reached.all(): reward+=.75
  return self.observe(),reward,done,{"success":bool(reached.all()),"positions":self.pos.tolist(),"reached":reached.tolist()}