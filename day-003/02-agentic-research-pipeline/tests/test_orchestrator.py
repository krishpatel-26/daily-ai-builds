from app.orchestrator import ResearchOrchestrator
from app.models import ResearchRequest
def test_trace_and_evidence():
 r=ResearchOrchestrator().run(ResearchRequest(question='AI agents and RAG retrieval',depth=2)); assert r.plan and r.trace[-1]=='synthesis.completed'; assert all(0<=e.confidence<=1 for e in r.evidence)
