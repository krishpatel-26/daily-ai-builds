from questguard.quests import propose,can_complete; from questguard.simulator import world
def test_visible_npc():assert propose(world(),"dragon") is None
def test_quest_flag():
 s=world();q={"required_flag":"done"};assert not can_complete(s,q);s.flags["done"]=True;assert can_complete(s,q)