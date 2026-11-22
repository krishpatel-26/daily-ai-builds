class ApprovalRegistry:
    """In-memory simulation of approval grants. No user-facing grant endpoint.

    Production would require verified identities, roles, durable approval workflows,
    and binding to immutable action payload hashes.
    """
    def __init__(self):self._grants={}
    def grant(self,proposal_id,approver,expires_at):
        if not approver or not proposal_id:raise ValueError('approver and proposal_id required')
        self._grants[proposal_id]=(approver,expires_at)
    def valid(self,proposal_id,now):
        record=self._grants.get(proposal_id)
        return bool(record and record[1]>=now)