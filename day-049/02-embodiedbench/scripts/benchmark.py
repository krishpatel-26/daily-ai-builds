"""Print the four planner-condition comparisons as JSON."""
import json
from embodiedbench.benchmark import compare
if __name__=='__main__':print(json.dumps(compare(),indent=2))
