import numpy as np,torch
from torch.distributions import Categorical
from .environment import CorridorEnv
from .graph import build_adjacency,edge_count
def collect(actor,critic,seed=7,communicate=True):
 env=CorridorEnv(seed); obs=env.reset(); data={k:[] for k in ("obs","adj","actions","logp","values","rewards","dones","edges")}; done=False
 while not done:
  adj=build_adjacency(obs); x=torch.tensor(obs); a=torch.tensor(adj)
  with torch.no_grad(): logits,_=actor(x,a,communicate); dist=Categorical(logits=logits); acts=dist.sample(); logp=dist.log_prob(acts); value=critic(x)
  nxt,reward,done,info=env.step(acts.numpy())
  for k,v in zip(data,(obs.copy(),adj.copy(),acts.numpy(),logp.numpy(),float(value),float(np.mean(reward)),done,edge_count(adj))): data[k].append(v)
  obs=nxt
 return data,info