from . import world
from .planner import generate
from .schemas import QuestProposal
from .validation import validate
from .duplicates import duplicate_check
def propose(tone="mystery",limit=3):
 w=world.snapshot();results=generate(w,tone,limit);accepted=[]
 for r in results:
  q=QuestProposal(**r["quest"])
  if not duplicate_check(q,w["active_quests"],w["completed_quests"])["duplicate"]:accepted.append(r)
 return {"world_tick":w["tick"],"candidates":accepted,"rejected_duplicates":len(results)-len(accepted)}
def validate_proposal(data):return validate(QuestProposal(**data),world.snapshot())
def accept(data):
 q=QuestProposal(**data);v=validate(q,world.snapshot())
 if not v["valid"]:return {"accepted":False,"validation":v}
 from .lifecycle import activate
 r=activate(q.model_dump());return {"accepted":r["ok"],"validation":v,"result":r}