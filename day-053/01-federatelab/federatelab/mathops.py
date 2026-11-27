import math

def sigmoid(z):
    if z < -35: return 1e-15
    if z > 35: return 1 - 1e-15
    return 1 / (1 + math.exp(-z))

def predict(weights,features):
    return sigmoid(weights[0]*features[0]+weights[1]*features[1]+weights[2])

def accuracy(weights, samples):
    if not samples: raise ValueError('empty evaluation set')
    return sum((predict(weights,x)>=0.5)==bool(y) for x,y in samples)/len(samples)

def log_loss(weights,samples):
    if not samples: raise ValueError('empty evaluation set')
    return -sum(y*math.log(max(predict(weights,x),1e-12))+(1-y)*math.log(max(1-predict(weights,x),1e-12)) for x,y in samples)/len(samples)
