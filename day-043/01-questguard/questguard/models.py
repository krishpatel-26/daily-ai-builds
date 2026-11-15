from enum import Enum; from pydantic import BaseModel,Field
class Action(str,Enum): MOVE="move"; TALK="talk"; ATTACK="attack"; OPEN_DOOR="open_door"; GIVE_ITEM="give_item"; ACCEPT_QUEST="accept_quest"; COMPLETE_QUEST="complete_quest"; WAIT="wait"
class WorldState(BaseModel): location:str="village_square"; health:int=100; stamina:int=100; inventory:list[str]=[]; visible_entities:list[str]=[]; locked_doors:list[str]=[]; active_quests:list[str]=[]; completed_quests:list[str]=[]; flags:dict[str,bool]={}; tick:int=0
class ProposedAction(BaseModel): action:Action; target:str|None=None; item:str|None=None; destination:str|None=None; confidence:float=Field(.5,ge=0,le=1); evidence:list[str]=[]
class TurnRequest(BaseModel): state:WorldState; proposal:ProposedAction