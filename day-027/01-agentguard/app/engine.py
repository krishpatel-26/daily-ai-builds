from uuid import uuid4
from .models import ActionProposal, Decision, Risk
from .policies import find_policy

BLOCKED_FIELDS = {"password", "password_hash", "secret", "api_key", "access_token"}
SENSITIVE_ACTIONS = {"delete", "transfer", "refund", "export", "close"}

def evaluate(proposal: ActionProposal) -> Decision:
    reasons: list[str] = []
    policy = find_policy(proposal.role, proposal.resource_type, proposal.action)
    if policy is None:
        return Decision(request_id=str(uuid4()), status="denied", risk=Risk.CRITICAL,
                        reasons=["No policy grants this role the requested action."], requires_approval=False)
    if any(key.lower() in BLOCKED_FIELDS for key in proposal.payload):
        return Decision(request_id=str(uuid4()), status="denied", risk=Risk.CRITICAL,
                        reasons=["Payload contains a restricted field."], requires_approval=False)
    if proposal.expected_state:
        mismatches = [k for k, v in proposal.expected_state.items() if proposal.current_state.get(k) != v]
        if mismatches:
            return Decision(request_id=str(uuid4()), status="denied", risk=Risk.HIGH,
                            reasons=[f"Precondition failed for: {', '.join(mismatches)}."],
                            requires_approval=False)
    approval = policy.approval_required or proposal.action in SENSITIVE_ACTIONS
    reasons.append(f"Policy matched: {proposal.role}/{proposal.resource_type}/{proposal.action}.")
    reasons.append("Human approval required." if approval else "No approval gate required by this policy.")
    return Decision(request_id=str(uuid4()), status="pending_approval" if approval else "allowed",
                    risk=policy.risk, reasons=reasons, requires_approval=approval)
