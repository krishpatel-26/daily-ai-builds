from .config import Config
from .simulator import simulate
from .optimizer import evaluate
from .pareto import pareto_front
def build_report(config=Config()):
 baseline=simulate(config,"reactive");candidates=evaluate(config);best=candidates[0]
 return {"title":"FactoryTwin AI","baseline":baseline,"candidates":candidates,"pareto":pareto_front(candidates),"recommended_scenario":best,"note":"Illustrative optimization from synthetic simulation, not a validated factory recommendation."}
