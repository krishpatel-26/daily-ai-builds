from collections import deque
class EventMemory:
 def __init__(self,limit=100):self.events=deque(maxlen=limit)
 def add(self,tick,event):self.events.append({"tick":tick,"event":event})
 def recent(self,n=10):return list(self.events)[-n:]