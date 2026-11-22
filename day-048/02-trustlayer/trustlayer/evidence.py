from .models import Evidence

def matching_evidence(proposal, evidences, now, sources):
    index={e.id:e for e in evidences}
    if not proposal.evidence_ids:return [],'MISSING_EVIDENCE'
    selected=[]
    for evidence_id in proposal.evidence_ids:
        e=index.get(evidence_id)
        if e is None:return [],'EVIDENCE_NOT_FOUND'
        if e.source not in sources:return [],'UNTRUSTED_SOURCE'
        if e.observed_at>now or e.observed_at+e.ttl<now:return [],'EXPIRED_EVIDENCE'
        if e.resource!=proposal.resource or e.action!=proposal.action:return [],'EVIDENCE_SCOPE_MISMATCH'
        selected.append(e.id)
    return selected,None