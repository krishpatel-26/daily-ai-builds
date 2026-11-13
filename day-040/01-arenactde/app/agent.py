import torch
from torch.distributions import Categorical
class Agent:
 def __init__(self,actor,critic):self.actor=actor;self.critic=critic
 @torch.no_grad()
 def act(self,obs,state,greedy=False):
  d=Categorical(logits=self.actor(torch.as_tensor(obs,dtype=torch.float32)));a=d.probs.argmax(-1) if greedy else d.sample();return a.numpy(),d.log_prob(a).numpy(),float(self.critic(torch.as_tensor(state,dtype=torch.float32)))