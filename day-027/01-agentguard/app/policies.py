from dataclasses import dataclass
from .models import Risk

@dataclass(frozen=True)
class Policy:
    role: str
    resource_type: str
    actions: frozenset[str]
    risk: Risk
    approval_required: bool = False

POLICIES = (
    Policy("support_agent", "ticket", frozenset({"read", "tag", "assign"}), Risk.LOW),
    Policy("support_agent", "customer", frozenset({"read", "update_contact"}), Risk.MEDIUM, True),
    Policy("finance_agent", "invoice", frozenset({"read", "draft"}), Risk.MEDIUM, True),
    Policy("admin", "ticket", frozenset({"read", "tag", "assign", "close"}), Risk.HIGH, True),
    Policy("admin", "customer", frozenset({"read", "update_contact", "export"}), Risk.HIGH, True),
)

def find_policy(role: str, resource_type: str, action: str) -> Policy | None:
    for policy in POLICIES:
        if policy.role == role and policy.resource_type == resource_type and action in policy.actions:
            return policy
    return None
