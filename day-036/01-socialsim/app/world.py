from copy import deepcopy
SEED={"tick":0,"characters":{"player":{"id":"player","name":"The Adventurer"},"mira":{"id":"mira","name":"Mira the Healer"},"rowan":{"id":"rowan","name":"Rowan the Scout"},"elder":{"id":"elder","name":"Village Elder"},"kael":{"id":"kael","name":"Kael the Merchant"}},"relationships":{},"rumours":[],"events":[]}
for a,b,v in [("mira","player",20),("rowan","player",0),("elder","player",10),("kael","player",-10),("mira","rowan",25),("rowan","mira",15),("elder","mira",40),("kael","elder",-20)]:SEED["relationships"][a+"->"+b]={"source":a,"target":b,"trust":v,"fear":0,"loyalty":0,"rivalry":0}
STATE=deepcopy(SEED)
def snapshot():return deepcopy(STATE)
def reset():
 global STATE
 STATE=deepcopy(SEED);return snapshot()