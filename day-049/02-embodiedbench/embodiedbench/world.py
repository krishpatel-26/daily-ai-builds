"""A discrete warehouse manipulation environment with explicit physical constraints."""
from dataclasses import dataclass, field

WIDTH, HEIGHT = 16, 11
WALLS = {(5,y) for y in range(0,9) if y not in (3,7)} | {(10,y) for y in range(2,11) if y not in (5,8)}
ITEMS = {'red_cube':(3,2),'blue_cylinder':(13,3),'green_box':(7,9)}
ZONES = {'zone_a':(2,9),'zone_b':(14,8),'zone_c':(12,1)}
START = (1,1)


def valid(cell, obstacles=WALLS):
    return 0<=cell[0]<WIDTH and 0<=cell[1]<HEIGHT and cell not in obstacles


@dataclass
class State:
    position:tuple[int,int]=START
    carrying:str|None=None
    objects:dict[str,tuple[int,int]]=field(default_factory=lambda:dict(ITEMS))
    completed:list[str]=field(default_factory=list)
    battery:int=220
    tick:int=0
    dynamic_obstacles:set[tuple[int,int]]=field(default_factory=set)

    def public(self):
        return {'position':list(self.position),'carrying':self.carrying,
                'objects':{k:list(v) for k,v in self.objects.items()},
                'completed':list(self.completed),'battery':self.battery,'tick':self.tick,
                'dynamic_obstacles':[list(x) for x in sorted(self.dynamic_obstacles)]}
