import unittest
from crisismesh.world import make_scenario
from crisismesh.dispatch import dispatch
from crisismesh.metrics import evaluate
class DispatchTests(unittest.TestCase):
 def test_no_team_duplicated(self):
  d=dispatch(make_scenario()); ids=[x['team_id'] for x in d['assignments']];self.assertEqual(len(ids),len(set(ids)))
 def test_capacity_respected(self):
  s=make_scenario();d=dispatch(s);teams={t['id']:t for t in s['teams']};self.assertTrue(all(a['persons_capacity']<=teams[a['team_id']]['capacity'] for a in d['assignments']))
 def test_routes_follow_team_limit(self):
  s=make_scenario();d=dispatch(s);teams={t['id']:t for t in s['teams']}
  for a in d['assignments']:
   self.assertTrue(all(s['water'][y][x]<=teams[a['team_id']]['max_water'] for x,y in a['route']))
 def test_all_incidents_accounted(self):
  s=make_scenario();d=dispatch(s);self.assertEqual(len(s['incidents']),len(d['assignments'])+len(d['unserved']))
 def test_metrics_bounded(self):
  s=make_scenario();m=evaluate(s,dispatch(s));self.assertTrue(0<=m['coverage_pct']<=100)