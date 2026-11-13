import numpy as np,torch
from .environment import CoopGrid
def evaluate(actor,episodes=30,seed=100):
 success=0;returns=[];lengths=[]
 for ep in range(episodes):
  e=CoopGrid(seed+ep);obs,state=e.reset();total=0
  for t in range(32):
   with torch.no_grad():acts=actor(torch.as_tensor(obs,dtype=torch.float32)).argmax(-1).numpy()
   obs,state,r,done,info=e.step(acts);total+=float(r.mean())
   if done:break
  success+=int(info["success"]);returns.append(total);lengths.append(t+1)
 return {"episodes":episodes,"success_rate":success/episodes,"mean_return":float(np.mean(returns)),"mean_steps":float(np.mean(lengths)),"seed":seed}