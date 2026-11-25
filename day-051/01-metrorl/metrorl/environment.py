"""Tiny corridor traffic digital twin, intentionally not a traffic-engineering model."""
from dataclasses import dataclass
import random
from .config import Config

AXES = ('NS', 'EW')

@dataclass
class Intersection:
    ns: int = 0
    ew: int = 0
    phase: int = 0
    emergency_axis: int = -1
    emergency_age: int = 0

class Corridor:
    def __init__(self, seed=51, config=None):
        self.config = (config or Config()).validate()
        self.seed = seed
        self.rng = random.Random(seed)
        self.junctions = [Intersection() for _ in range(self.config.junctions)]
        self.tick = 0
        self.injected_at = -1
        self.stats = dict(arrivals=0, exits=0, dropped=0, transferred=0, switches=0,
                          waiting_sum=0, served=0, emergencies=0, emergencies_served=0,
                          emergency_wait=0)
        self.trace = []

    def _inject(self):
        if self.injected_at == self.tick:
            return
        self.injected_at = self.tick
        if self.tick in self.config.emergency_ticks:
            i = self.config.emergency_ticks.index(self.tick) % len(self.junctions)
            j = self.junctions[i]
            if j.emergency_axis == -1:
                j.emergency_axis = (self.tick // 30) % 2
                j.emergency_age = 0
                self.stats['emergencies'] += 1
                if j.emergency_axis == 0:
                    if j.ns < self.config.capacity: j.ns += 1
                    else: self.stats['dropped'] += 1
                else:
                    if j.ew < self.config.capacity: j.ew += 1
                    else: self.stats['dropped'] += 1
                self.stats['arrivals'] += 1

    def observe(self):
        self._inject()
        return [(min(3, j.ns//5), min(3, j.ew//5), j.phase,
                 j.emergency_axis + 1) for j in self.junctions]

    def arrivals(self):
        c = self.config
        local_drops=[0]*len(self.junctions)
        for i, j in enumerate(self.junctions):
            for axis in (0, 1):
                # Exogenous arrivals are reproducible under a given seed.
                peak = 1.5 if (self.tick//40)%2 == axis else 0.75
                expected = c.base_arrival * peak * (1 + .10 * i)
                incoming = int(expected) + int(self.rng.random() < expected%1)
                current = j.ns if axis == 0 else j.ew
                admitted = min(incoming, max(0, c.capacity-current))
                self.stats['arrivals'] += incoming
                self.stats['dropped'] += incoming-admitted
                local_drops[i] += incoming-admitted
                if axis == 0: j.ns += admitted
                else: j.ew += admitted
        return local_drops

    def step(self, actions):
        self._inject()
        c = self.config
        if len(actions) != len(self.junctions) or any(a not in (0,1) for a in actions):
            raise ValueError('One NS/EW phase choice required per intersection')
        local_drops=self.arrivals()
        transfers = [0]*len(self.junctions)
        rewards = []
        for i,(j,action) in enumerate(zip(self.junctions,actions)):
            switched = action != j.phase
            if switched: self.stats['switches'] += 1
            j.phase = action
            service = 0 if switched and c.switch_lost_time else c.service
            served = min(service, j.ns if action == 0 else j.ew)
            if action == 0: j.ns -= served
            else: j.ew -= served
            self.stats['served'] += served
            # Fixed transfer fraction for EW corridor travel; remainder leaves network.
            forwarded = min(served, round(served*c.transfer_fraction)) if action == 1 and i < len(self.junctions)-1 else 0
            if forwarded: transfers[i+1] += forwarded
            self.stats['transferred'] += forwarded
            self.stats['exits'] += served-forwarded
            emergency_completed = j.emergency_axis == action and served > 0
            if j.emergency_axis != -1:
                if emergency_completed:
                    self.stats['emergencies_served'] += 1
                    self.stats['emergency_wait'] += j.emergency_age
                    j.emergency_axis = -1
                else:
                    j.emergency_age += 1
            rewards.append(2.0*served - .13*(j.ns+j.ew) - 5*local_drops[i] - (1.4 if switched else 0) - (14 if j.emergency_axis!=-1 else 0))
        for i, amount in enumerate(transfers):
            if not amount: continue
            j=self.junctions[i]
            accepted=min(amount,max(0,c.capacity-j.ew))
            j.ew += accepted
            self.stats['dropped'] += amount-accepted
            rewards[i] -= 5*(amount-accepted)
        self.tick += 1
        total=sum(j.ns+j.ew for j in self.junctions)
        self.stats['waiting_sum']+=total
        if self.tick%4==0 or self.tick == c.ticks:
            self.trace.append({'tick':self.tick,'queues':[[j.ns,j.ew] for j in self.junctions],
                               'total_queue':total,'exits':self.stats['exits'],'dropped':self.stats['dropped'],
                               'phases':[AXES[j.phase] for j in self.junctions]})
        return rewards

    def run(self, policy):
        for t in range(self.config.ticks):
            states=self.observe()
            actions=policy(states,t)
            self.step(actions)
        return self.report()

    def report(self):
        s=self.stats
        last=sum(j.ns+j.ew for j in self.junctions)
        # Demand conservation: injected exogenous arrivals = exits + dropped + remaining.
        return {'seed':self.seed,'ticks':self.tick,'stats':dict(s),
                'metrics':{'exits':s['exits'],'mean_queue':round(s['waiting_sum']/max(1,self.tick),2),
                           'dropped':s['dropped'],'switches':s['switches'],
                           'emergencies_served':s['emergencies_served'],
                           'emergencies':s['emergencies'],
                           'mean_emergency_delay':round(s['emergency_wait']/max(1,s['emergencies_served']),2),
                           'conservation_error':s['arrivals']-s['exits']-s['dropped']-last},
                'final_queues':[[j.ns,j.ew] for j in self.junctions], 'trace':self.trace}
