from .corpus import fixtures
from .engine import Engine
from .ledger import Ledger

def demo(now=1000):
    facts,proposals=fixtures(now);engine=Engine();ledger=Ledger();out=[]
    for p in proposals:
        r=engine.evaluate(p,facts,now)
        event={'proposal_id':p.id,'action':p.action,'resource':p.resource,'accepted':r.accepted,'code':r.code,'evidence_used':list(r.evidence_used)}
        ledger.append(event)
        out.append({'proposal':{'id':p.id,'action':p.action,'resource':p.resource,'evidence_ids':list(p.evidence_ids)},'decision':r.to_dict()})
    totals={code:sum(row['decision']['code']==code for row in out) for code in sorted({row['decision']['code'] for row in out})}
    return {'project':'TrustLayer','cases':out,'evidence_count':len(facts),'metrics':{'proposals':len(out),'validated':sum(x['decision']['accepted'] for x in out),'rejected':sum(not x['decision']['accepted'] for x in out),'decision_counts':totals,'ledger_integrity':ledger.verify()},'audit_head':ledger.entries[-1]['hash'][:16],'disclaimer':'Deterministic policy and evidence-validation demo; no live LLM calls or real tool execution.'}