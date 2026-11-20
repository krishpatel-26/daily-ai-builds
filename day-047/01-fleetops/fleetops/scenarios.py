import random
from .models import Robot, Task
from .grid import valid

def default_scenario(seed=47):
    rng=random.Random(seed)
    robots=[Robot('AMR-01',(1,0),83),Robot('AMR-02',(14,0),78),Robot('AMR-03',(1,11),89),Robot('AMR-04',(14,11),75)]
    goals=[(2,2),(7,2),(13,3),(2,9),(8,10),(14,8),(7,5),(8,6),(3,4),(12,9),(2,6),(13,6)]
    rng.shuffle(goals)
    tasks=[Task(f'JOB-{i+1:03}',goal,1+(i%3),35+i*9) for i,goal in enumerate(goals)]
    assert all(valid(t.goal) for t in tasks)
    return robots,tasks
