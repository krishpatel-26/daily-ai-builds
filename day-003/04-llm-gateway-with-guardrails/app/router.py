from .providers import LocalProvider,ReasoningProvider
class ModelRouter:
 def __init__(self): self.providers={'general':LocalProvider(),'extraction':LocalProvider(),'creative':LocalProvider(),'reasoning':ReasoningProvider()}
 def route(self,task): return self.providers[task]
