from .engine import compare
from .model import VARIABLES
def run(name,interventions):
 r=compare(interventions);return {"name":name,"summary":f"{r['changed_count']} variables changed","result":r}
def catalog():return [{"variable":k,"baseline":v} for k,v in VARIABLES.items()]