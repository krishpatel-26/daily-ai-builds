import numpy as np,torch
from torch.distributions import Categorical
from .returns import compute_gae
def update(actor,critic,actor_opt,critic_opt,b,epochs=4):
 obs=torch.tensor(np.asarray(b["obs"]),dtype=torch.float32); adj=torch.tensor(np.asarray(b["adj"]),dtype=torch.float32); actions=torch.tensor(np.asarray(b["actions"]),dtype=torch.long); old=torch.tensor(np.asarray(b["logp"]),dtype=torch.float32); values=np.asarray(b["values"]); adv,ret=compute_gae(b["rewards"],values,b["dones"]); adv=torch.tensor(adv); ret=torch.tensor(ret); adv=(adv-adv.mean())/(adv.std()+1e-8); logs=[]
 for _ in range(epochs):
  logits=[]; predicted=[]
  for t in range(len(obs)):
   z,_=actor(obs[t],adj[t]); logits.append(z); predicted.append(critic(obs[t]))
  logits=torch.stack(logits); predicted=torch.stack(predicted); dist=Categorical(logits=logits); new=dist.log_prob(actions); ratio=torch.exp(new-old); aa=adv[:,None].expand_as(ratio); policy=-torch.minimum(ratio*aa,torch.clamp(ratio,.8,1.2)*aa).mean()-.01*dist.entropy().mean(); actor_opt.zero_grad(); policy.backward(); torch.nn.utils.clip_grad_norm_(actor.parameters(),.5); actor_opt.step()
  value_loss=.5*((predicted-ret)**2).mean(); critic_opt.zero_grad(); value_loss.backward(); torch.nn.utils.clip_grad_norm_(critic.parameters(),.5); critic_opt.step(); logs.append((float(policy.detach()),float(value_loss.detach())))
 return {"actor_loss":float(np.mean([x[0] for x in logs])),"critic_loss":float(np.mean([x[1] for x in logs]))}