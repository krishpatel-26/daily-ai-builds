import random
from .config import ACTIONS
def choose_action(q_table,key,epsilon,rng):
 if rng.random()<epsilon:return rng.choice(ACTIONS)
 row=q_table.get(key,{})
 return max(ACTIONS,key=lambda a:(row.get(a,0.0),-ACTIONS.index(a)))
def update(q_table,key,action,reward,next_key,alpha,gamma,done):
 row=q_table.setdefault(key,{a:0.0 for a in ACTIONS});future=0.0 if done else max(q_table.get(next_key,{}).values(),default=0.0)
 old=row.get(action,0.0);row[action]=old+alpha*(reward+gamma*future-old)
 return row[action]