from .models import SUPPLIERS,WAREHOUSES,STORES,POLICIES
from .scenarios import demand_stream
from .procurement import procurement_orders
from .inventory import Inventory


def simulate(policy='diversified',seed=50,days=70,disrupted=True):
    if policy not in POLICIES:raise ValueError('Unknown policy')
    if not isinstance(days,int) or not 1<=days<=365:raise ValueError('days must be 1..365')
    config=POLICIES[policy]
    warehouse=Inventory({w.id:w.opening_stock for w in WAREHOUSES})
    stores=Inventory({s.id:s.opening_stock for s in STORES})
    demand=demand_stream(seed,days,disrupted)
    total_demand=total_sold=total_orders=total_shipped=lost_sales=0
    procurement_cost=transport_cost=holding_cost=0.0
    events=[];daily=[];supplier_units={x.id:0 for x in SUPPLIERS}
    start_units=sum(warehouse.on_hand.values())+sum(stores.on_hand.values())
    for day in range(days):
        received_wh=warehouse.receive(day);received_store=stores.receive(day)
        for x in received_wh:
            events.append({'day':day,'event':'supplier_delivery','source':x['source'],'target':x['target'],'units':x['quantity']})
        day_demand=sum(demand[day].values());day_sold=0;day_lost=0
        # Customer purchases consume store stock. Lost sales are explicit, not backordered.
        for s in STORES:
            requested=demand[day][s.id];fulfilled=stores.consume(s.id,requested)
            day_sold+=fulfilled;day_lost+=requested-fulfilled
        total_demand+=day_demand;total_sold+=day_sold;lost_sales+=day_lost
        # Replenish downstream stores by medical-service priority, then ID.
        day_store_shipped=0
        for s in sorted(STORES,key=lambda x:(-x.priority,x.id)):
            target=round(s.avg_demand*config.store_cover_days*(1.2 if disrupted and 30<=day<50 else 1.0))
            required=max(0,target-stores.position(s.id))
            qty=warehouse.consume(s.warehouse,required)
            stores.schedule(s.id,qty,day+1,s.warehouse)
            day_store_shipped+=qty
        total_shipped+=day_store_shipped;transport_cost+=day_store_shipped*.24
        # Orders placed across warehouses share each supplier's daily capacity.
        remaining={s.id:s.capacity_per_day for s in SUPPLIERS}
        day_orders=0
        for w in WAREHOUSES:
            avg=sum(s.avg_demand for s in STORES if s.warehouse==w.id)
            factor=config.disruption_safety_factor if disrupted and 20<=day<52 else 1.0
            target=round(avg*config.warehouse_cover_days*factor)
            shortfall=max(0,target-warehouse.position(w.id))
            orders=procurement_orders(shortfall,config,remaining,day,disrupted)
            for o in orders:
                warehouse.schedule(w.id,o['quantity'],o['arrives'],o['source'])
                supplier_units[o['source']]+=o['quantity'];procurement_cost+=o['quantity']*o['unit_cost']
                events.append({'day':day,'event':'order','source':o['source'],'target':w.id,'units':o['quantity']})
                day_orders+=o['quantity']
        total_orders+=day_orders
        day_holding=sum(warehouse.on_hand.values())+sum(stores.on_hand.values())
        holding_cost+=day_holding*.045
        if day in (22,30,44,50) and disrupted:
            events.append({'day':day,'event':'environment_change','detail':{22:'Primary supplier disruption begins',30:'Demand surge begins',44:'Primary supplier resumes',50:'Demand surge ends'}[day]})
        daily.append({'day':day+1,'demand':day_demand,'sold':day_sold,'lost_sales':day_lost,'fill_rate_pct':round(day_sold/max(1,day_demand)*100,2),
                      'warehouse_units':sum(warehouse.on_hand.values()),'store_units':sum(stores.on_hand.values()),
                      'in_transit':sum(x['quantity'] for x in warehouse.pending)+sum(x['quantity'] for x in stores.pending),
                      'supplier_orders':day_orders,'warehouse_to_store':day_store_shipped})
    end_units=sum(warehouse.on_hand.values())+sum(stores.on_hand.values())
    transit=sum(x['quantity'] for x in warehouse.pending)+sum(x['quantity'] for x in stores.pending)
    if start_units+total_orders!=total_sold+end_units+transit:
        raise RuntimeError('Inventory conservation invariant violated')
    # All cost parameters are illustrative, not calibrated monetary estimates.
    lost_sales_cost=lost_sales*14
    estimated_cost=procurement_cost+transport_cost+holding_cost+lost_sales_cost
    return {'project':'SupplyChainOS','policy':policy,'seed':seed,'days':days,'disrupted':disrupted,
            'metrics':{'demand_units':total_demand,'sold_units':total_sold,'lost_sales_units':lost_sales,
                       'fill_rate_pct':round(100*total_sold/max(1,total_demand),2),
                       'procured_units':total_orders,'warehouse_to_store_units':total_shipped,
                       'estimated_cost':round(estimated_cost,2),'procurement_cost':round(procurement_cost,2),
                       'transport_cost':round(transport_cost,2),'holding_cost':round(holding_cost,2),
                       'lost_sales_penalty':round(lost_sales_cost,2),'inventory_end':end_units,'units_in_transit':transit,
                       'supplier_units':supplier_units},'trace':daily,'events':events[-100:],
            'assumptions':'Stochastic simulated demand, fixed lead times, finite supplier capacities, lost-sales model, synthetic costs.'}
