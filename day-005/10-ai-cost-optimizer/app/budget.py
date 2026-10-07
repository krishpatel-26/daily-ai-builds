def within_budget(cost: float, budget: float) -> bool:
    return cost >= 0 and budget >= 0 and cost <= budget
