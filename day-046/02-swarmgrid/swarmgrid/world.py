from .models import Robot,Task
WIDTH=14;HEIGHT=10
OBSTACLES={(5,y) for y in range(2,8)}|{(9,y) for y in range(0,6)}
def valid(p):return 0<=p[0]<WIDTH and 0<=p[1]<HEIGHT and p not in OBSTACLES
def neighbors(p):return [q for q in ((p[0]+1,p[1]),(p[0]-1,p[1]),(p[0],p[1]+1),(p[0],p[1]-1)) if valid(q)]
def demo():
 robots=[Robot("AMR-01",(0,0)),Robot("AMR-02",(0,9)),Robot("AMR-03",(13,9)),Robot("AMR-04",(13,0))]
 tasks=[Task("PICK-01",(3,3)),Task("PICK-02",(7,8)),Task("PICK-03",(12,6)),Task("PICK-04",(1,6)),Task("PICK-05",(11,8)),Task("PICK-06",(3,1))]
 return robots,tasks
