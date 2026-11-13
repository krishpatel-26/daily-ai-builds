import numpy as np
class CoopGrid:
 def __init__(self,seed=7):self.rng=np.random.default_rng(seed);self.reset()
 def reset(self):self.pos=np.array([0,4]);self.energy=np.array([5,5]);self.goal=2;self.t=0;return self.obs(),self.joint()
 def obs(self):return np.array([[self.pos[i]/4,self.energy[i]/5,abs(self.goal-self.pos[i])/4,self.pos[1-i]/4,float(self.pos[i]==self.goal),self.t/32] for i in range(2)],dtype=np.float32)
 def joint(self):return np.r_[self.obs().flatten(),self.goal/4,self.t/32].astype(np.float32)
 def step(self,acts):
  r=np.full(2,-.02,dtype=np.float32)
  for i,a in enumerate(acts):
   if a==0:self.pos[i]=min(4,self.pos[i]+1);self.energy[i]=max(0,self.energy[i]-1)
   elif a==1:self.pos[i]=max(0,self.pos[i]-1);self.energy[i]=max(0,self.energy[i]-1)
   elif a==2:self.energy[i]=min(5,self.energy[i]+2)
   elif a==3 and self.pos[i]==self.goal:r[i]+=.2
   elif a==4 and self.energy[i]>0:self.energy[i]-=1
  self.t+=1;success=bool(np.all(self.pos==self.goal));done=success or self.t>=32
  if success:r+=1.0
  return self.obs(),self.joint(),r,done,{"success":success,"positions":self.pos.tolist()}