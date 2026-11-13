import numpy as np
from .environment import CoopGrid
from .agent import Agent
def collect(actor,critic,seed=7,steps=32):
 e=CoopGrid(seed);obs,state=e.reset();buf={k:[] for k in ("obs","states","actions","logp","rewards","dones","values")};a=Agent(actor,critic)
 for _ in range(steps):
  acts,lp,v=a.act(obs,state);no,ns,r,done,info=e.step(acts)
  for k,x in zip(buf,(obs.copy(),state.copy(),acts.copy(),lp.copy(),float(r.mean()),done,v)):buf[k].append(x)
  obs,state=no,ns
  if done:obs,state=e.reset()
 return buf