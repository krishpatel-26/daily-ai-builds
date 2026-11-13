import torch
from torch import nn
class GraphAttention(nn.Module):
 def __init__(self,obs_dim=6,hidden=64):
  super().__init__(); self.proj=nn.Linear(obs_dim,hidden,bias=False); self.score=nn.Linear(hidden*2,1,bias=False); self.leaky=nn.LeakyReLU(.2)
 def forward(self,x,adj):
  h=self.proj(x); n=h.shape[0]; hi=h[:,None,:].expand(n,n,-1); hj=h[None,:,:].expand(n,n,-1); logits=self.leaky(self.score(torch.cat([hi,hj],dim=-1)).squeeze(-1)); logits=logits.masked_fill(adj<=0,-1e9); weights=torch.softmax(logits,dim=-1); return torch.relu(weights@h),weights
class Actor(nn.Module):
 def __init__(self):
  super().__init__(); self.gat=GraphAttention(); self.net=nn.Sequential(nn.Linear(128,96),nn.Tanh(),nn.Linear(96,64),nn.Tanh(),nn.Linear(64,3))
 def forward(self,obs,adj,communicate=True):
  msg,weights=self.gat(obs,adj)
  if not communicate: msg=torch.zeros_like(msg)
  return self.net(torch.cat([obs,msg],dim=-1)),weights
class Critic(nn.Module):
 def __init__(self): super().__init__(); self.net=nn.Sequential(nn.Linear(24,128),nn.Tanh(),nn.Linear(128,96),nn.Tanh(),nn.Linear(96,1))
 def forward(self,state): return self.net(state.reshape(-1)).squeeze(-1)