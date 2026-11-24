from dataclasses import dataclass,field

@dataclass
class Inventory:
    on_hand: dict[str,int]
    pending: list[dict]=field(default_factory=list)
    def position(self,id):
        return self.on_hand[id]+sum(p['quantity'] for p in self.pending if p['target']==id)
    def receive(self,day):
        remaining=[];received=[]
        for p in self.pending:
            if p['arrives']<=day:
                self.on_hand[p['target']]+=p['quantity'];received.append(p)
            else:remaining.append(p)
        self.pending=remaining
        return received
    def schedule(self,target,quantity,arrives,source):
        if quantity<0:raise ValueError('Negative transfer not allowed')
        if quantity:self.pending.append({'target':target,'quantity':quantity,'arrives':arrives,'source':source})
    def consume(self,target,requested):
        if requested<0:raise ValueError('Demand must be nonnegative')
        count=min(requested,self.on_hand[target]);self.on_hand[target]-=count;return count
