from pydantic import BaseModel, Field
class DocumentIn(BaseModel):
    title:str=Field(min_length=1,max_length=200)
    text:str=Field(min_length=20,max_length=100000)
class Hit(BaseModel):
    document_id:int
    title:str
    text:str
    score:float