from pydantic import BaseModel,Field
class CompletionRequest(BaseModel):
 prompt:str=Field(min_length=1,max_length=12000); task:str=Field(default='general',pattern='^(general|reasoning|extraction|creative)$'); max_tokens:int=Field(default=256,ge=1,le=2048)
class CompletionResponse(BaseModel):
 provider:str; model:str; text:str; input_tokens:int; output_tokens:int; estimated_cost:float; blocked:bool=False
