import logging
from .agents import AGENTS
from .models import Action, IncidentPlan, IncidentRequest
from .runbooks import retrieve_runbooks

log = logging.getLogger(__name__)

class IncidentEngine:
    def score(self, req: IncidentRequest) -> int:
        score = 20 * len(req.alerts)
        for a in req.alerts:
            if a.value > a.threshold * 2: score += 20
            elif a.value > a.threshold: score += 10
        if req.recent_deploy: score += 15
        return min(score, 100)

    def analyze(self, req: IncidentRequest) -> IncidentPlan:
        score = self.score(req)
        severity = 'critical' if score >= 80 else 'high' if score >= 60 else 'medium' if score >= 35 else 'low'
        evidence = [agent.analyze(req.alerts, req.recent_deploy) for agent in AGENTS]
        runbooks = retrieve_runbooks(req.alerts)
        actions = [Action(priority=1, action='Confirm blast radius and affected dependencies', reason='Prevent remediation from amplifying impact.'), Action(priority=2, action='Compare alert onset with recent changes', reason='Establish change correlation before rollback.')]
        if runbooks: actions.append(Action(priority=3, action='Open the matched runbook and execute only after approval', reason=runbooks[0]))
        log.info('incident_plan_created', extra={'severity': severity, 'score': score, 'evidence': len(evidence)})
        return IncidentPlan(title=req.title, severity=severity, score=score, evidence=evidence, actions=actions, rationale='Severity combines alert volume, threshold deviation, and deployment correlation.')
