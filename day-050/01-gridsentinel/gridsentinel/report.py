from .scenarios import run,compare_outages
from .metrics import compare_strategies

def report(strategy='baseline',failed_line=None):
    result=run(failed_line,strategy)
    result['comparisons']=compare_strategies(compare_outages())
    return result
