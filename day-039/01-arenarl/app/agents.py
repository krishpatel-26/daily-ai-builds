import random
from .policy import choose_action
from .state import observation,state_key
from .config import ACTIONS
def act(state,team,q_table,epsilon,rng):return choose_action(q_table,state_key(observation(state,team)),epsilon,rng)
def heuristic(state,team):
 p=state["players"][team];opp=state["players"]["red" if team=="blue" else "blue"]
 if abs(p.pos-opp.pos)<=1 and p.energy>=2:return "attack"
 if state["resources"] and min(abs(p.pos-x) for x in state["resources"])<=1:return "gather"
 if p.energy<2:return "rest"
 return "approach"
def random_action(rng):return rng.choice(ACTIONS)