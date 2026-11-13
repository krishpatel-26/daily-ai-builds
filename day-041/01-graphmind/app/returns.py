import numpy as np
def compute_gae(rewards,values,dones,last_value=0.,gamma=.99,lam=.95):
 adv=np.zeros(len(rewards),dtype=np.float32); running=0.
 for t in reversed(range(len(rewards))):
  nxt=last_value if t==len(rewards)-1 else values[t+1]; mask=1.-float(dones[t]); delta=float(rewards[t])+gamma*nxt*mask-float(values[t]); running=delta+gamma*lam*mask*running; adv[t]=running
 return adv,adv+np.asarray(values,dtype=np.float32)