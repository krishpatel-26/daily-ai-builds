import json
from pathlib import Path
def export_result(result,path):
 p=Path(path);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(result,indent=2));return str(p)
def policy_summary(tables):
 return {team:{"states":len(table),"state_action_values":sum(len(v) for v in table.values())} for team,table in tables.items()}