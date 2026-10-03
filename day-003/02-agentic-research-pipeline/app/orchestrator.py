import logging
from .agents import SpecialistAgent,LocalKnowledge,DEFAULT_CORPUS
from .models import ResearchRequest,ResearchReport
log=logging.getLogger(__name__)
class Planner:
 def plan(self,q,depth): return [f'Define scope: {q}',f'Find implementation evidence for: {q}',f'Identify trade-offs and risks for: {q}'][:depth+1]
class ResearchOrchestrator:
 def __init__(self):
  k=LocalKnowledge(DEFAULT_CORPUS); self.agents=[SpecialistAgent('architecture',k),SpecialistAgent('implementation',k),SpecialistAgent('operations',k)]; self.planner=Planner()
 def run(self,request):
  plan=self.planner.plan(request.question,request.depth); trace=['plan.created']; evidence=[]
  for i,sub in enumerate(plan):
   agent=self.agents[i%len(self.agents)]; evidence.extend(agent.research(sub,request.depth)); trace.append(f'{agent.name}.completed')
  evidence=sorted(evidence,key=lambda e:e.confidence,reverse=True)[:request.depth*3]; answer=' '.join(f'[{e.source}] {e.claim}' for e in evidence) or 'No local evidence matched.'; trace.append('synthesis.completed'); log.info('research_completed evidence=%d',len(evidence)); return ResearchReport(question=request.question,plan=plan,evidence=evidence,answer=answer,trace=trace)
