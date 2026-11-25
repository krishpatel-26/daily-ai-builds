"""Batch-gradient logistic regression from scratch, no ML dependencies."""
import math

def sigmoid(z):
    if z>=0:return 1/(1+math.exp(-z))
    v=math.exp(z)
    return v/(1+v)

class LogisticModel:
    def __init__(self,weights=None): self.weights=list(weights) if weights else [0.]*5
    def predict_proba(self,x):
        if len(x)!=4:raise ValueError('expected four features')
        return sigmoid(self.weights[0]+sum(w*v for w,v in zip(self.weights[1:],x)))
    def predict(self,x):return int(self.predict_proba(x)>=.5)
    def train(self,rows,epochs=130,lr=.22,l2=.008):
        if not rows:raise ValueError('empty training dataset')
        if epochs<1 or lr<=0:raise ValueError('invalid hyperparameters')
        n=len(rows)
        for _ in range(epochs):
            gradients=[0.]*5
            for row in rows:
                error=self.predict_proba(row.x)-row.y
                gradients[0]+=error
                for j,v in enumerate(row.x):gradients[j+1]+=error*v
            for j in range(5):
                grad=gradients[j]/n+(l2*self.weights[j] if j else 0.)
                self.weights[j]-=lr*grad
        return self
    def to_dict(self):return {'weights':[round(x,5) for x in self.weights]}
