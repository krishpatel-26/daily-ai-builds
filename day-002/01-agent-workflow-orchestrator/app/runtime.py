import uuid
from .agents import AGENTS
from .models import WorkflowResult
from .planner import build_plan

def execute(request):
    plan=build_plan(request.request); results=[]
    for step in plan.steps:
        try: results.append({'step_id':step.id,'agent':step.agent,'output':AGENTS[step.agent].run(step.objective),'status':'completed'})
        except Exception: results.append({'step_id':step.id,'agent':step.agent,'output':'step failed','status':'failed'})
    status='completed' if all(x['status']=='completed' for x in results) else 'partial'
    return WorkflowResult(workflow_id=str(uuid.uuid4()),plan=plan,results=results,status=status)