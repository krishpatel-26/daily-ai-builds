from collections import defaultdict
from fastapi import FastAPI
from .models import ScoreRequest,Signal
from .scoring import score
app=FastAPI(title='GTM Signal Engine',version='1.0.0')
@app.get('/health')
def health(): return {'status':'ok'}
@app.post('/signals',response_model=list[Signal])
def generate(req:ScoreRequest):
 grouped=defaultdict(list)
 for activity in req.activities: grouped[activity.account_id].append(activity)
 results=[]
 for account_id,items in grouped.items():
  value,reasons,action=score(items); results.append(Signal(account_id=account_id,score=value,reasons=reasons,recommended_action=action))
 return sorted(results,key=lambda x:x.score,reverse=True)
