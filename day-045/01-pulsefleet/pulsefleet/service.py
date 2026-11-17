from .simulator import generate_fleet
from .ingestion import group_by_robot
from .health import assess_fleet
from .report import fleet_report
def build_demo(seed=7):return fleet_report(assess_fleet(group_by_robot(generate_fleet(seed=seed))))
