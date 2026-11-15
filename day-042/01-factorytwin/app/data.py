import math,random
from app.schemas import SensorPoint
MACHINES=["CNC-01","PRESS-02","ROBOT-03","CONVEYOR-04","PUMP-05"]
def generate(seed=11,steps=96):
 r=random.Random(seed);out=[]
 for j,m in enumerate(MACHINES):
  for t in range(steps):
   fault=(j==1 and t>65) or (j==4 and 42<t<57);d=t/steps
   out.append(SensorPoint(machine_id=m,timestamp=t,temperature=round(55+4*math.sin(t/9)+r.gauss(0,1.4)+(13*d if fault else 0),2),vibration=round(1.2+r.random()*.25+(1.3*d if fault else 0),3),current=round(8+r.gauss(0,.35)+(1.5*d if fault else 0),2),pressure=round(5.2+r.gauss(0,.12)-(.6*d if fault else 0),2),throughput=round(100-r.random()*4-(18*d if fault else 0),2)))
 return out