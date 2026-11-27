def poison(update,scale=5.0):
    # Adversarial inversion/scaling. This is one illustrative attack, not a general threat model.
    if scale<=0:raise ValueError('scale must be positive')
    return [-scale*x for x in update]
