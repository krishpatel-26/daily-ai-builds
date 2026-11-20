from .simulator import FleetSimulation

def compare(seeds=(7,47,77),ticks=110):
    result=[]
    for faults in (False,True):
        trials=[FleetSimulation(seed,ticks,faults).run()['metrics'] for seed in seeds]
        result.append({'faults_enabled':faults,'trials':len(trials),'mean_completion_rate':round(sum(x['completion_rate'] for x in trials)/len(trials),3),'mean_distance':round(sum(x['distance'] for x in trials)/len(trials),1),'mean_blocked_steps':round(sum(x['blocked_steps'] for x in trials)/len(trials),1)})
    return result
