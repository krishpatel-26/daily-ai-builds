"""Deterministic task execution with online replanning on a dynamic obstacle."""
from .world import State,WIDTH,HEIGHT,WALLS,ZONES,ITEMS
from .intent import sample_tasks
from .planner import choose_task,route_to
from .executor import execute


class Simulator:
    def __init__(self,policy='nearest',fault=True,limit=200):
        if policy not in ('nearest','ordered'):raise ValueError('Unknown planning policy')
        if not 1<=limit<=1000:raise ValueError('Time limit must be 1..1000')
        self.policy=policy;self.fault=fault;self.limit=limit
        self.state=State();self.pending=sample_tasks();self.current=None;self.stage='idle'
        self.route=[];self.target=None;self.replans=0;self.distance=0
        self.rejections=0;self.events=[];self.frames=[];self.injected=False
        self.snapshot()

    def event(self,kind,**details):self.events.append({'tick':self.state.tick,'event':kind,**details})

    def snapshot(self):
        self.frames.append({'tick':self.state.tick,'state':self.state.public(),
                            'current_task':self.current.id() if self.current else None,
                            'stage':self.stage})

    def task_goal(self):
        if self.current is None:return None
        if self.stage=='pickup':return self.state.objects[self.current.item]
        return ZONES[self.current.zone]

    def new_task(self):
        option=choose_task(self.state,self.pending,self.policy)
        if option is None:return False
        self.current,pick,_=option;self.stage='pickup';self.target=self.state.objects[self.current.item]
        self.route=pick[1:];self.event('task_selected',task=self.current.id(),policy=self.policy)
        return True

    def inject_obstacle(self):
        if self.injected or not self.fault or self.state.tick!=6:return
        self.injected=True
        # Place a temporary crate in the planned path (not in an object or goal cell).
        forbidden=set(ITEMS.values())|set(ZONES.values())|{self.state.position}
        options=[p for p in self.route[:3] if p not in forbidden and p not in WALLS]
        if options:
            obstacle=options[0];self.state.dynamic_obstacles.add(obstacle)
            self.event('new_obstacle',cell=list(obstacle))

    def step(self):
        self.state.tick+=1
        if not self.current and self.pending:self.new_task()
        self.inject_obstacle()
        if self.current:
            goal=self.task_goal()
            if goal is not None:
                if self.route and (self.route[0] in self.state.dynamic_obstacles):
                    new_route=route_to(self.state,goal)
                    if new_route is None:self.event('route_unavailable',task=self.current.id())
                    else:
                        self.route=new_route[1:];self.replans+=1
                        self.event('replanned',task=self.current.id(),route_steps=len(self.route))
                if self.route:
                    step=self.route[0]
                    result=execute(self.state,'move',step)
                    if result['ok']:
                        self.route.pop(0);self.distance+=1
                    else:self.rejections+=1;self.event('rejected',code=result['code'])
                elif self.state.position==goal:
                    if self.stage=='pickup':
                        result=execute(self.state,'pick',self.current.item)
                        if result['ok']:
                            self.stage='drop';self.target=ZONES[self.current.zone]
                            route=route_to(self.state,self.target);self.route=route[1:] if route else []
                            self.event('picked',item=self.current.item)
                    elif self.stage=='drop':
                        result=execute(self.state,'place',self.current.zone)
                        if result['ok']:
                            self.event('delivered',task=self.current.id(),zone=self.current.zone)
                            self.pending.remove(self.current);self.current=None;self.stage='idle';self.route=[]
        self.snapshot()

    def run(self):
        for _ in range(self.limit):
            if not self.pending and not self.current:break
            self.step()
        return {'project':'EmbodiedBench','policy':self.policy,'fault_injection':self.fault,
                'world':{'width':WIDTH,'height':HEIGHT,'static_obstacles':[list(p) for p in sorted(WALLS)],
                         'initial_objects':{k:list(v) for k,v in ITEMS.items()},
                         'zones':{k:list(v) for k,v in ZONES.items()}},
                'metrics':{'total_tasks':3,'completed_tasks':3-len(self.pending),
                           'success_rate':round((3-len(self.pending))/3,3),
                           'ticks':self.state.tick,'distance':self.distance,
                           'replans':self.replans,'rejected_actions':self.rejections,
                           'battery_remaining':self.state.battery},
                'events':self.events,'frames':self.frames,
                'limitations':'Discrete symbolic manipulation with exact object state, not a physics engine, VLA model or real robot.'}
