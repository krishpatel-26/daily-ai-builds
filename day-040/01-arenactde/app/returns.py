import numpy as np
def gae(rewards,values,dones,last=0.,gamma=.99,lam=.95):
 adv=np.zeros(len(rewards),dtype=np.float32);g=0.
 for t in reversed(range(len(rewards))):
  nv=last if t==len(rewards)-1 else values[t+1];mask=1-float(dones[t]);delta=rewards[t]+gamma*nv*mask-values[t];g=delta+gamma*lam*mask*g;adv[t]=g
 return adv,adv+np.asarray(values,dtype=np.float32)