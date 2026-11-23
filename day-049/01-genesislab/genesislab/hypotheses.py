"""Structured hypothesis/explanation records for each experiment."""
def explain(candidate, prediction, previous_best):
    if prediction is None:
        return {'hypothesis':'Seed measurement to establish a baseline',
                'evidence':'No model posterior available yet', 'type':'initial'}
    if prediction['uncertainty'] > 7:
        motivation = 'Explore an uncertain region of the feasible process envelope'
        family = 'exploration'
    else:
        motivation = 'Test a high-expected-improvement parameter combination'
        family = 'exploitation'
    return {'hypothesis':motivation, 'type':family,
            'evidence':f"Expected improvement {prediction['expected_improvement']}; prior best {previous_best:.2f}"}
