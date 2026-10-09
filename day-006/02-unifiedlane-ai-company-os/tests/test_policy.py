from company_os.models import Action, AgentRole, Task
from company_os.orchestrator import Orchestrator, route_goal
from company_os.policy import authorize


def test_research_agent_can_read_research():
    decision = authorize(Task("1", "Research market", AgentRole.RESEARCH, Action.READ_RESEARCH))
    assert decision.allowed
    assert not decision.requires_approval


def test_analytics_cannot_update_crm():
    decision = authorize(Task("2", "Edit CRM", AgentRole.ANALYTICS, Action.UPDATE_CRM))
    assert not decision.allowed
    assert decision.reason == "role_permission_denied"


def test_external_outreach_requires_approval():
    task = Task("3", "Send email", AgentRole.OUTREACH, Action.SEND_OUTREACH,
                requires_external_side_effect=True)
    result = Orchestrator().evaluate(task)
    assert result["status"] == "pending_approval"


def test_high_risk_requires_approval():
    decision = authorize(Task("4", "Run workflow", AgentRole.OPERATIONS,
                              Action.RUN_WORKFLOW, risk="high"))
    assert decision.allowed
    assert decision.requires_approval


def test_route_goal():
    assert route_goal("research competitors") == AgentRole.RESEARCH
    assert route_goal("analyze performance metrics") == AgentRole.ANALYTICS
