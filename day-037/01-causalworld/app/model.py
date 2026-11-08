VARIABLES={"player_reputation":35.0,"village_trust":50.0,"faction_tension":20.0,"resource_supply":70.0,"guard_readiness":55.0,"npc_support":45.0,"quest_access":50.0,"regional_stability":60.0}
EQUATIONS={
"village_trust":("player_reputation",lambda s:.65*s["player_reputation"]+17.25),
"faction_tension":("village_trust resource_supply",lambda s:.55*(100-s["village_trust"])+.45*(100-s["resource_supply"])),
"guard_readiness":("faction_tension resource_supply",lambda s:.65*(100-s["faction_tension"])+.35*s["resource_supply"]),
"npc_support":("village_trust player_reputation",lambda s:.7*s["village_trust"]+.3*s["player_reputation"]),
"quest_access":("npc_support faction_tension",lambda s:.7*s["npc_support"]+.3*(100-s["faction_tension"])),
"regional_stability":("guard_readiness faction_tension resource_supply",lambda s:.45*s["guard_readiness"]+.3*(100-s["faction_tension"])+.25*s["resource_supply"])}
DESCRIPTIONS={"player_reputation":"How the region perceives the player","village_trust":"Collective trust in the player","faction_tension":"Conflict pressure between local factions","resource_supply":"Availability of critical village resources","guard_readiness":"Ability of guards to respond to threats","npc_support":"Willingness of NPCs to support the player","quest_access":"Availability of relationship-gated quests","regional_stability":"Overall stability of the region"}