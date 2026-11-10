from copy import deepcopy
SEED={"turn":0,"resources":{"wood":8,"food":10,"ore":4},"agents":{"alpha":{"id":"alpha","name":"Astra","team":"blue","hp":10,"energy":8,"x":1,"y":1,"policy":"balanced","alive":True},"bravo":{"id":"bravo","name":"Bram","team":"blue","hp":10,"energy":8,"x":1,"y":2,"policy":"economist","alive":True},"cinder":{"id":"cinder","name":"Cinder","team":"red","hp":10,"energy":8,"x":6,"y":6,"policy":"aggressive","alive":True},"dusk":{"id":"dusk","name":"Dusk","team":"red","hp":10,"energy":8,"x":6,"y":5,"policy":"defensive","alive":True}},"log":[],"scores":{"blue":0,"red":0}}
STATE=deepcopy(SEED)
def snapshot():return deepcopy(STATE)
def reset():
 global STATE
 STATE=deepcopy(SEED);return snapshot()