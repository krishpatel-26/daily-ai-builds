from .models import PlanStep, WorkflowPlan
KEYWORDS={'research':('research','competitor','market'),'data':('data','metric','dataset'),'gtm':('lead','sales','icp','outreach'),'api':('api','webhook','endpoint')}
def build_plan(request):
    text=request.lower(); selected=[a for a,w in KEYWORDS.items() if any(x in text for x in w)] or ['research']
    return WorkflowPlan(steps=[PlanStep(id='step-'+str(i+1),agent=a,objective='Handle '+a+' workstream for: '+request) for i,a in enumerate(dict.fromkeys(selected))])