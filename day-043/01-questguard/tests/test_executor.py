from questguard.simulator import world; from questguard.models import ProposedAction,Action; from questguard.executor import execute
def test_rejection_preserves_state():
 s=world();r=execute(s,ProposedAction(action=Action.ATTACK,target="dragon",evidence=["dragon"]));assert not r["executed"] and r["state"]==s.model_dump()
def test_move():assert execute(world(),ProposedAction(action=Action.MOVE,destination="forest_path",evidence=["village_square"]))["state"]["location"]=="forest_path"