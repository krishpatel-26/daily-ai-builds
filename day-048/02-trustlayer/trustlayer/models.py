from dataclasses import dataclass,asdict

@dataclass(frozen=True)
class Evidence:
    id:str
    source:str
    resource:str
    action:str
    observed_at:int
    ttl:int
    claim:str

@dataclass(frozen=True)
class Proposal:
    id:str
    agent:str
    action:str
    resource:str
    evidence_ids:tuple[str,...]
    payload:str=''

@dataclass(frozen=True)
class Decision:
    proposal_id:str
    accepted:bool
    code:str
    reason:str
    evidence_used:tuple[str,...]=()
    def to_dict(self):return asdict(self)