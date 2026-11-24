from dataclasses import dataclass

@dataclass(frozen=True)
class Supplier:
    id: str
    capacity_per_day: int
    lead_days: int
    unit_cost: float

@dataclass(frozen=True)
class Warehouse:
    id: str
    opening_stock: int

@dataclass(frozen=True)
class Store:
    id: str
    warehouse: str
    avg_demand: float
    opening_stock: int
    priority: int

@dataclass(frozen=True)
class Policy:
    name: str
    store_cover_days: float
    warehouse_cover_days: float
    suppliers: tuple[str,...]
    disruption_safety_factor: float

SUPPLIERS=(Supplier('SOURCE-A',54,2,4.0),Supplier('SOURCE-B',42,4,4.7))
WAREHOUSES=(Warehouse('HUB-WEST',170),Warehouse('HUB-EAST',155))
STORES=(Store('CLINIC-01','HUB-WEST',12,36,5),Store('RETAIL-02','HUB-WEST',15,45,2),Store('PHARMACY-03','HUB-EAST',14,42,5),Store('RETAIL-04','HUB-EAST',13,39,2))
POLICIES={
 'lean':Policy('lean',1.7,2.3,('SOURCE-A',),1.0),
 'diversified':Policy('diversified',2.6,3.2,('SOURCE-A','SOURCE-B'),1.0),
 'resilient':Policy('resilient',3.8,4.7,('SOURCE-A','SOURCE-B'),1.35),
}
