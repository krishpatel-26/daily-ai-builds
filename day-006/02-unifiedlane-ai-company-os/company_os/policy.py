from .models import Action, AgentRole, Decision, Task

ROLE_PERMISSIONS: dict[AgentRole, set[Action]] = {
    AgentRole.RESEARCH: {Action.READ_RESEARCH},
    AgentRole.STRATEGY: {Action.READ_RESEARCH, Action.READ_ANALYTICS},
    AgentRole.CONTENT: {Action.READ_RESEARCH, Action.WRITE_CONTENT},
    AgentRole.OPERATIONS: {Action.RUN_WORKFLOW, Action.READ_ANALYTICS},
    AgentRole.OUTREACH: {Action.READ_RESEARCH, Action.UPDATE_CRM, Action.SEND_OUTREACH},
    AgentRole.ANALYTICS: {Action.READ_ANALYTICS, Action.READ_RESEARCH},
}

SENSITIVE_ACTIONS = {Action.UPDATE_CRM, Action.SEND_OUTREACH, Action.RUN_WORKFLOW}


def authorize(task: Task) -> Decision:
    permissions = ROLE_PERMISSIONS.get(task.role, set())
    if task.action not in permissions:
        return Decision(False, False, "role_permission_denied", task.task_id, task.role, task.action)

    approval_needed = (
        task.requires_external_side_effect
        or task.action in SENSITIVE_ACTIONS
        or task.risk.lower() in {"high", "critical"}
    )
    return Decision(
        allowed=True,
        requires_approval=approval_needed,
        reason="approval_required" if approval_needed else "policy_allowed",
        task_id=task.task_id,
        role=task.role,
        action=task.action,
    )
