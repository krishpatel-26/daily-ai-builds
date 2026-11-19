from dataclasses import dataclass
@dataclass(frozen=True)
class Task:
 id:str;goal:tuple[int,int]
@dataclass
class Robot:
 id:str;position:tuple[int,int];completed:int=0;distance:int=0
