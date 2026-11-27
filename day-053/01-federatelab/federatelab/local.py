from .mathops import predict

def train_local(initial, samples, epochs=2, lr=.12):
    if not samples or epochs<1 or not 0<lr<=1: raise ValueError('invalid training config')
    w=list(initial)
    for _ in range(epochs):
        for x,y in samples:
            err=predict(w,x)-y
            w[0]-=lr*err*x[0];w[1]-=lr*err*x[1];w[2]-=lr*err
    return [new-old for new,old in zip(w,initial)]
