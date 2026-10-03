from pydantic import BaseModel,Field
class ResearchRequest(BaseModel):
 question:str=Field(min_length=10,max_length=2000); depth:int=Field(default=2,ge=1,le=4)
class Evidence(BaseModel):
 agent:str; claim:str; source:str; confidence:float=Field(ge=0,le=1)
class ResearchReport(BaseModel):
 question:str; plan:list[str]; evidence:list[Evidence]; answer:str; trace:list[str]
