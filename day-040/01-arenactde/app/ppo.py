import numpy as np,torch
from torch.distributions import Categorical
from .returns import gae
def update(actor,critic,ao,co,b,epochs=4):
 obs=torch.tensor(np.array(b["obs"]),dtype=torch.float32);states=torch.tensor(np.array(b["states"]),dtype=torch.float32);acts=torch.tensor(np.array(b["actions"]),dtype=torch.long);old=torch.tensor(np.array(b["logp"]),dtype=torch.float32);adv,ret=gae(b["rewards"],b["values"],b["dones"]);adv=torch.tensor(adv);ret=torch.tensor(ret);adv=(adv-adv.mean())/(adv.std()+1e-8);stats=[]
 for _ in range(epochs):
  dist=Categorical(logits=actor(obs.reshape(-1,6)));ratio=torch.exp(dist.log_prob(acts.reshape(-1))-old.reshape(-1));a=adv.repeat_interleave(2);loss=-torch.minimum(ratio*a,torch.clamp(ratio,.8,1.2)*a).mean()-.01*dist.entropy().mean();ao.zero_grad();loss.backward();torch.nn.utils.clip_grad_norm_(actor.parameters(),.5);ao.step()
  vl=((critic(states)-ret)**2).mean();co.zero_grad();(.5*vl).backward();torch.nn.utils.clip_grad_norm_(critic.parameters(),.5);co.step();stats.append((loss.item(),vl.item()))
 return {"actor_loss":float(np.mean([x[0] for x in stats])),"critic_loss":float(np.mean([x[1] for x in stats]))}