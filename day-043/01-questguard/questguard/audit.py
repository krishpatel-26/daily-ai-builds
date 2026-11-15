from collections import deque
class AuditLog:
 def __init__(self,limit=1000):self.rows=deque(maxlen=limit)
 def append(self,x):self.rows.append(x)
 def list(self,n=50):return list(self.rows)[-max(1,min(n,200)): ]