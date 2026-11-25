"""Shared tabular Q learner, trained from scratch on seeded traffic episodes."""
import random
from .environment import Corridor
from .policies import QPolicy

def train(episodes=160,horizon=135,seed=51,alpha=.13,gamma=.91):
    if not 1<=episodes<=3000:raise ValueError('episodes outside bounds')
    rng=random.Random(seed)
    table={}
    outcomes=[]
    for ep in range(episodes):
        env=Corridor(seed=seed*1000+ep)
        eps=.35*(1-ep/episodes)+.04
        for t in range(horizon):
            states=env.observe()
            actions=[]
            for state in states:
                v=table.setdefault(tuple(state),[0.,0.])
                actions.append(rng.randrange(2) if rng.random()<eps else int(v[1]>v[0]))
            rewards=env.step(actions)
            next_states=env.observe()
            for state,action,reward,after in zip(states,actions,rewards,next_states):
                v=table.setdefault(tuple(state),[0.,0.])
                future=max(table.setdefault(tuple(after),[0.,0.]))
                v[action]+=alpha*(reward+gamma*future-v[action])
        outcomes.append(env.report()['metrics']['mean_queue'])
    return QPolicy(table),{'episodes':episodes,'states_learned':len(table),
                           'first_20_episode_mean_queue':round(sum(outcomes[:20])/min(20,episodes),2),
                           'last_20_episode_mean_queue':round(sum(outcomes[-20:])/min(20,episodes),2)}
