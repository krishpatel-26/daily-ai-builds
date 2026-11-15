from questguard.simulator import world; from questguard.models import ProposedAction,Action; from questguard.guard import inspect
def test_valid_talk():assert inspect(world(),ProposedAction(action=Action.TALK,target="guard",evidence=["guard"]))["accepted"]
def test_hallucinated_target():assert inspect(world(),ProposedAction(action=Action.ATTACK,target="dragon",evidence=["dragon"]))["code"]=="UNGROUNDED_PROPOSAL"
def test_bad_destination():assert inspect(world(),ProposedAction(action=Action.MOVE,destination="moon",evidence=["village_square"]))["code"]=="DESTINATION_INVALID"