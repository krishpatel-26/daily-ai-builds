import torch
from torch import nn
class Actor(nn.Module):
 def __init__(self):super().__init__();self.net=nn.Sequential(nn.Linear(6,64),nn.Tanh(),nn.Linear(64,64),nn.Tanh(),nn.Linear(64,5))
 def forward(self,x):return self.net(x)
class CentralCritic(nn.Module):
 def __init__(self):super().__init__();self.net=nn.Sequential(nn.Linear(14,96),nn.Tanh(),nn.Linear(96,96),nn.Tanh(),nn.Linear(96,1))
 def forward(self,x):return self.net(x).squeeze(-1)