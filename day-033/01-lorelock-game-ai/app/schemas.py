from typing import Literal,Optional
from pydantic import BaseModel,Field,ConfigDict
class ActionProposal(BaseModel):
 model_config=ConfigDict(extra="forbid")
 request_id:str=Field(min_length=4,max_length=80)
 actor_id:str=Field(min_length=1,max_length=60)
 action:Literal["move","interact","attack","use_item","start_quest","talk"]
 target_id:Optional[str]=Field(default=None,max_length=60)
 item_id:Optional[str]=Field(default=None,max_length=60)
 rationale:Optional[str]=Field(default=None,max_length=500)
class DialogueRequest(BaseModel):
 actor_id:str
 question:str=Field(min_length=2,max_length=500)