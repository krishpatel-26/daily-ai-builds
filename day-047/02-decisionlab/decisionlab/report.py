from .config import Experiment
from .simulator import simulate
from .experiment import compare
from .sensitivity import demand_sensitivity

def report():
    experiment=Experiment()
    baseline=simulate('reactive',47,experiment)
    candidates=compare()
    return {'name':'DecisionLab','assumptions':{'horizon_minutes':experiment.horizon,'demand_units':experiment.demand,'buffer_capacity':experiment.buffer_capacity,'paired_seed_count':25,'uncertainty':'Normal-approximation confidence intervals; illustrative simulation only'},'baseline':baseline,'candidates':candidates,'sensitivity':demand_sensitivity(),'selected_scenario':candidates[0],'scope':'Counterfactuals only within the stated simulator assumptions; no verified real-world causal claim.'}
