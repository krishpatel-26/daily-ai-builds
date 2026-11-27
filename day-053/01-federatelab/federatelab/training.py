from .data import make_dataset
from .mathops import accuracy,log_loss
from .local import train_local
from .aggregation import aggregate
from .attack import poison

METHODS=('fedavg','median','trimmed_mean')

def train(seed=53,rounds=18,method='fedavg',attack=True,clients=9,poisoned=2):
    if method not in METHODS:raise ValueError('unknown method')
    if not 1<=rounds<=80 or not 0<=poisoned<clients//2:raise ValueError('invalid rounds or attacker count')
    shards,test=make_dataset(seed,clients)
    w=[0.,0.,0.];history=[]
    for round_i in range(rounds):
        updates=[]
        for client,shard in enumerate(shards):
            # Round/seed deterministic order, no user data is transmitted.
            start=(round_i*19+client*7)%len(shard)
            batch=[shard[(start+j)%len(shard)] for j in range(36)]
            delta=train_local(w,batch,epochs=2,lr=.075)
            if attack and client>=clients-poisoned:delta=poison(delta,scale=5)
            updates.append(delta)
        d=aggregate(updates,method,trim=2)
        w=[x+y for x,y in zip(w,d)]
        history.append({'round':round_i+1,'accuracy':round(accuracy(w,test),4),'loss':round(log_loss(w,test),4)})
    return {'method':method,'attack':attack,'seed':seed,'rounds':rounds,'final_accuracy':history[-1]['accuracy'],'final_loss':history[-1]['loss'],'weights':[round(x,5) for x in w],'communication_kb':round(rounds*clients*3*8/1024,2),'history':history}
