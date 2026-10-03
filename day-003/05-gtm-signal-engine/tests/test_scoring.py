from datetime import datetime,timezone,timedelta
from app.scoring import score
def test_hot_account():
 now=datetime.now(timezone.utc)
 activities=[type('A',(),{'event':'demo_request','weight':1,'occurred_at':now})(),type('A',(),{'event':'pricing_view','weight':1,'occurred_at':now})()]
 value,reasons,action=score(activities)
 assert value>=70 and reasons and 'Contact account executive now'==action

def test_old_activity_decays():
 now=datetime.now(timezone.utc)
 fresh=[type('A',(),{'event':'pricing_view','weight':1,'occurred_at':now})()]
 old=[type('A',(),{'event':'pricing_view','weight':1,'occurred_at':now-timedelta(days=30)})()]
 assert score(fresh)[0]>score(old)[0]
