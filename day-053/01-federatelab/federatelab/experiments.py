from .training import train,METHODS

def compare(seed=53,rounds=18):
    return [train(seed,rounds,method,attack) for attack in (False,True) for method in METHODS]

def benchmark(seeds=(11,22,33,44,55),rounds=18):
    rows=[]
    for attack in (False,True):
        for method in METHODS:
            scores=[train(seed,rounds,method,attack)['final_accuracy'] for seed in seeds]
            rows.append({'attack':attack,'method':method,'trials':len(scores),'mean_accuracy':round(sum(scores)/len(scores),4),'min_accuracy':min(scores),'max_accuracy':max(scores)})
    return rows
