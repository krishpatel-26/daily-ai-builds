from .simulator import Simulator
from .benchmark import compare


def report(policy='nearest',fault=True,limit=200):
    simulation=Simulator(policy,fault,limit).run()
    return {'simulation':simulation,'comparison':compare(),
            'note':'Grounded symbolic robot-task planning in a synthetic world. No natural-language model or physical robot control.'}
