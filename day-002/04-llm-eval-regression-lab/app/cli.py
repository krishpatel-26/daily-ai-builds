from .evaluator import evaluate,load_cases
from .providers import MockProvider
def main():
    summary=evaluate(MockProvider(),load_cases()); print('mean_score=',summary.mean_score,'passed=',summary.passed)
if __name__=='__main__': main()