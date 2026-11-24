from .models import SUPPLIERS
from .scenarios import availability

def procurement_orders(shortfall, policy, source_remaining, day, disrupted=True):
    """Allocate an order to suppliers with remaining daily capacities."""
    requested=max(0,int(shortfall));orders=[]
    options=[s for s in SUPPLIERS if s.id in policy.suppliers]
    if len(options)>1 and policy.name=='resilient':
        options=sorted(options,key=lambda x: (x.id=='SOURCE-A',x.id))  # prioritize resilient alternate first
    for s in options:
        available=min(source_remaining[s.id],int(s.capacity_per_day*availability(s.id,day,disrupted)))
        count=min(requested,available)
        if count:
            orders.append({'source':s.id,'quantity':count,'arrives':day+s.lead_days,'unit_cost':s.unit_cost})
            source_remaining[s.id]-=count;requested-=count
    return orders
