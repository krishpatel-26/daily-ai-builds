from dataclasses import dataclass
from .models import Evidence
@dataclass
class LocalKnowledge:
 corpus:dict
 def search(self,topic):
  q=set(topic.lower().split()); rows=[]
  for key,items in self.corpus.items():
   base=len(q & set(key.lower().split()))
   for text,src in items:
    score=base+sum(t in text.lower() for t in q)
    if score: rows.append((score,text,src))
  return sorted(rows,key=lambda x:x[0],reverse=True)
class SpecialistAgent:
 def __init__(self,name,knowledge): self.name=name; self.knowledge=knowledge
 def research(self,subquestion,limit=3): return [Evidence(agent=self.name,claim=t,source=s,confidence=min(.95,.45+.1*score)) for score,t,s in self.knowledge.search(subquestion)[:limit]]
DEFAULT_CORPUS={'ai agents':[('Agent systems combine planning tools memory and execution loops.','local://ai-agents'),('Tool boundaries make agent behavior testable.','local://agent-design')],'rag retrieval':[('RAG retrieves external context before generation.','local://rag'),('Hybrid retrieval combines lexical and semantic signals.','local://retrieval')],'gtm automation':[('Signal pipelines prioritize accounts using behavioral evidence.','local://gtm'),('Automation should expose retries and idempotency.','local://automation')]}
