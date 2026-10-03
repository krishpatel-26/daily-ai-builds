from pydantic import BaseModel,Field
class Case(BaseModel): id:str; prompt:str; expected_keywords:list[str]=Field(min_length=1)
class Evaluation(BaseModel): case_id:str; output:str; score:float
class RunSummary(BaseModel): passed:bool; mean_score:float; evaluations:list[Evaluation]