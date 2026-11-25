"""Design a bounded review queue without exposing or changing oracle labels."""
from .active import select

def review_queue(pool,model,budget=12):
    rows=select(pool,model,budget,'uncertainty')
    return [{'id':r.id,'features':[round(x,3) for x in r.x],
             'predicted_probability':round(model.predict_proba(r.x),4),
             'uncertainty':round(1-2*abs(model.predict_proba(r.x)-.5),4)} for r in rows]
