import numpy as np,torch
from .environment import CorridorEnv
from .graph import build_adjacency,edge_count
def evaluate(actor,episodes=30,seed=100,communicate=True):
 successes=0; returns=[]; lengths=[]; edges=[]
 for ep in range(episodes):
  env=CorridorEnv(seed+ep); obs=env.reset(); total=0.; done=False; steps=0
  while not done:
   adj=build_adjacency(obs)
   with torch.no_grad(): logits,_=actor(torch.tensor(obs),torch.tensor(adj),communicate); acts=logits.argmax(-1).numpy()
   obs,r,done,info=env.step(acts); total+=float(np.mean(r)); steps+=1; edges.append(edge_count(adj))
  successes+=int(info["success"]); returns.append(total); lengths.append(steps)
 return {"episodes":episodes,"success_rate":successes/episodes,"mean_return":float(np.mean(returns)),"mean_steps":float(np.mean(lengths)),"mean_communication_edges":float(np.mean(edges)) if communicate else 0.,"communication_enabled":communicate,"seed":seed}