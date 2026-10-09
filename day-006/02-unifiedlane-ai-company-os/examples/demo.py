from company_os.models import Action, AgentRole, Task
from company_os.orchestrator import Orchestrator

os = Orchestrator()

tasks = [
    Task("task-001", "Research competitors", AgentRole.RESEARCH, Action.READ_RESEARCH),
    Task("task-002", "Draft a campaign post", AgentRole.CONTENT, Action.WRITE_CONTENT),
    Task(
        "task-003",
        "Send prospect outreach",
        AgentRole.OUTREACH,
        Action.SEND_OUTREACH,
        risk="medium",
        requires_external_side_effect=True,
    ),
    Task("task-004", "Edit CRM", AgentRole.ANALYTICS, Action.UPDATE_CRM),
]

for task in tasks:
    print(os.evaluate(task))
