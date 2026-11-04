"""Fleet-level health aggregation."""
from . import repository
from .health import assess

def fleet_summary():
 assets=repository.list_assets();items=[assess(a,repository.telemetry_for(a["asset_id"])) for a in assets]
 counts={k:sum(x["status"]==k for x in items) for k in ("healthy","watch","degraded","critical","no_data")}
 known=[x["health_index"] for x in items if x["health_index"] is not None]
 orders=repository.list_work_orders("open")
 return {"asset_count":len(assets),"average_health":round(sum(known)/len(known),1) if known else None,
 "status_counts":counts,"open_work_orders":len(orders),"assets":items}
