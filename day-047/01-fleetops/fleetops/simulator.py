from .models import Robot, Task
from .grid import WIDTH,HEIGHT,SHELVES,CHARGERS,astar
from .scenarios import default_scenario
from .dispatcher import nearest_charger,choose_assignment

class FleetSimulation:
    def __init__(self,seed=47,ticks=110,faults=True):
        if not 1 <= ticks <= 1000:
            raise ValueError('ticks must be 1..1000')
        self.seed=seed;self.max_ticks=ticks;self.faults_enabled=faults
        self.robots,self.tasks=default_scenario(seed);self.tick=0
        self.events=[];self.frames=[];self.collisions_prevented=0;self.assignment_count=0
        self.snapshot()

    def record(self,event,**details):
        self.events.append({'tick':self.tick,'event':event,**details})

    def snapshot(self):
        self.frames.append({'tick':self.tick,'robots':[{'id':r.id,'position':list(r.position),'battery':round(r.battery,1),'status':r.status,'task_id':r.task_id} for r in self.robots],'completed':sum(t.status=='completed' for t in self.tasks)})

    def release(self,r,reason):
        if r.task_id:
            t=next(t for t in self.tasks if t.id==r.task_id)
            if t.status!='completed':
                t.status='queued';t.robot_id=None;t.assigned_at=None
                self.record('requeued',task=t.id,robot=r.id,reason=reason)
        r.task_id=None;r.route=[]

    def update_status(self):
        for r in self.robots:
            if self.faults_enabled and self.tick==12 and r.id=='AMR-02':
                self.release(r,'injected motor fault');r.status='fault';r.fault_until=27;r.faults+=1
                self.record('fault',robot=r.id,until=r.fault_until)
            if r.status=='fault' and self.tick>=r.fault_until:
                r.status='idle';self.record('recovered',robot=r.id)
            if r.status=='charging':
                if r.position in CHARGERS:r.battery=min(100,r.battery+9)
                if r.battery>=85:r.status='idle';r.route=[];self.record('charged',robot=r.id)
            if r.status=='idle' and r.battery < 28:
                r.route=nearest_charger(r.position)[1:];r.status='to_charge';self.record('charge_requested',robot=r.id)
            if r.status=='idle':
                result=choose_assignment(r,self.tasks,self.tick)
                if result:
                    task,path=result;task.status='assigned';task.robot_id=r.id;task.assigned_at=self.tick
                    r.task_id=task.id;r.route=path[1:];r.status='working';self.assignment_count+=1
                    self.record('assigned',robot=r.id,task=task.id,priority=task.priority)

    def move(self):
        occupied={r.position for r in self.robots}
        claimed=set();moves={}
        for r in sorted(self.robots,key=lambda x:x.id):
            if r.status not in ('working','to_charge') or not r.route:continue
            target=r.route[0]
            if target in occupied or target in claimed:
                r.blocked_steps+=1;self.collisions_prevented+=1;continue
            moves[r.id]=target;claimed.add(target)
        for r in self.robots:
            if r.id not in moves:continue
            r.position=moves[r.id];r.route.pop(0);r.distance+=1;r.battery=max(0,r.battery-1.0)
        for r in self.robots:
            if r.status=='to_charge' and not r.route:
                r.status='charging'
            if r.status=='working' and not r.route and r.task_id:
                task=next(t for t in self.tasks if t.id==r.task_id)
                if r.position==task.goal:
                    task.status='completed';task.completed_at=self.tick;r.completed+=1
                    self.record('completed',robot=r.id,task=task.id,late=self.tick>task.due)
                    r.task_id=None;r.status='idle'

    def step(self):
        self.tick+=1;self.update_status();self.move();self.snapshot()

    def run(self):
        for _ in range(self.max_ticks):self.step()
        completed=[t for t in self.tasks if t.status=='completed']
        return {'project':'FleetOps','scenario':{'seed':self.seed,'ticks':self.max_ticks,'fault_injection':self.faults_enabled,'grid':[WIDTH,HEIGHT],'obstacles':[list(x) for x in sorted(SHELVES)],'chargers':[list(x) for x in CHARGERS]},'metrics':{'tasks_total':len(self.tasks),'tasks_completed':len(completed),'completion_rate':round(len(completed)/len(self.tasks),3),'late_tasks':sum(t.completed_at>t.due for t in completed),'distance':sum(r.distance for r in self.robots),'blocked_steps':sum(r.blocked_steps for r in self.robots),'collisions_prevented':self.collisions_prevented,'faults':sum(r.faults for r in self.robots),'assignments':self.assignment_count},'robots':[{'id':r.id,'status':r.status,'completed':r.completed,'distance':r.distance,'battery':round(r.battery,1),'faults':r.faults} for r in self.robots],'tasks':[{'id':t.id,'priority':t.priority,'goal':list(t.goal),'status':t.status,'robot_id':t.robot_id,'due':t.due,'completed_at':t.completed_at} for t in self.tasks],'events':self.events,'frames':self.frames}
