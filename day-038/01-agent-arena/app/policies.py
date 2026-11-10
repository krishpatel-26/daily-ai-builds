POLICIES={"balanced":{"gather":3,"guard":2,"attack":2,"rest":1,"trade":1},"aggressive":{"attack":5,"move":3,"guard":1,"gather":1,"rest":0},"defensive":{"guard":5,"rest":3,"gather":2,"attack":1,"move":1},"economist":{"gather":5,"trade":4,"guard":2,"rest":2,"attack":0}}
def score(agent,action,state):
 base=POLICIES.get(agent["policy"],POLICIES["balanced"]).get(action["action"],0)
 if action["action"]=="rest" and agent["energy"]<4:base+=4
 if action["action"]=="attack" and agent["energy"]<3:base-=5
 if action["action"]=="gather" and state["resources"]["food"]<4:base+=3
 if action["action"]=="guard" and agent["hp"]<5:base+=2
 return base+action.get("priority",1)*.1