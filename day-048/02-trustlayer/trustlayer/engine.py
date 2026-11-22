from .models import Decision
from .policy import DENIED,policy_for
from .taint import inspect_text
from .evidence import matching_evidence
from .approvals import ApprovalRegistry

class Engine:
    def __init__(self,approvals=None):self.approvals=approvals or ApprovalRegistry()
    def evaluate(self,proposal,evidences,now=1000):
        def reject(code,reason):return Decision(proposal.id,False,code,reason)
        if proposal.action in DENIED:return reject('ACTION_FORBIDDEN','Sensitive operation is denied regardless of evidence.')
        policy=policy_for(proposal.action)
        if policy is None:return reject('ACTION_NOT_ALLOWED','Action is absent from the server allowlist.')
        if not proposal.resource.startswith(policy['prefix']):return reject('INVALID_RESOURCE_SCOPE','Resource does not match the action namespace.')
        if inspect_text(proposal.payload):return reject('INJECTION_INDICATOR','Proposal payload contains a known prompt-injection indicator.')
        ids,error=matching_evidence(proposal,evidences,now,policy['sources'])
        if error:return reject(error,'Evidence is absent, stale, untrusted, or outside the proposed action scope.')
        if policy['approval'] and not self.approvals.valid(proposal.id,now):return reject('APPROVAL_REQUIRED','A verified approval grant is required before execution.')
        return Decision(proposal.id,True,'VALIDATED','Proposal passes this prototype policy and provenance checks.',tuple(ids))