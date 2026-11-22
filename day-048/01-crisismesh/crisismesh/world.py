from dataclasses import dataclass, asdict
import random

WIDTH, HEIGHT = 22, 14
BASE = (1, 1)

@dataclass(frozen=True)
class Incident:
    id: str
    x: int
    y: int
    severity: int
    people: int
    kind: str

@dataclass(frozen=True)
class Team:
    id: str
    kind: str
    capacity: int
    max_water: int
    range_units: int
    speed: float

TEAMS = (
    Team('RESCUE-01', 'boat', 14, 4, 45, 1.1),
    Team('RESCUE-02', 'boat', 10, 4, 43, 1.0),
    Team('MEDIC-01', 'ambulance', 4, 1, 52, 1.2),
    Team('UTILITY-01', 'truck', 7, 2, 50, 1.0),
)

def make_scenario(seed=48):
    rng = random.Random(seed)
    water = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    epicenters = [(rng.randrange(6, 19), rng.randrange(3, 12), rng.randint(2, 4)) for _ in range(4)]
    for y in range(HEIGHT):
        for x in range(WIDTH):
            strength = max((depth - max(abs(x-cx), abs(y-cy)) for cx,cy,depth in epicenters), default=0)
            water[y][x] = max(0, min(4, strength + (1 if rng.random() < .09 else 0)))
    for y in range(HEIGHT):
        for x in range(3): water[y][x] = 0
    cells=[]
    for n in range(10):
        for _ in range(100):
            x,y=rng.randrange(3, WIDTH),rng.randrange(HEIGHT)
            if (x,y) != BASE and (x,y) not in cells: break
        cells.append((x,y))
    incidents = [Incident(f'CASE-{n+1:02}', x, y, rng.randint(1,5), rng.randint(2,17), ('medical','evacuation','supplies')[n%3]) for n,(x,y) in enumerate(cells)]
    return {'seed':seed, 'width':WIDTH, 'height':HEIGHT, 'base':list(BASE), 'water':water, 'teams':[asdict(t) for t in TEAMS], 'incidents':[asdict(i) for i in incidents]}