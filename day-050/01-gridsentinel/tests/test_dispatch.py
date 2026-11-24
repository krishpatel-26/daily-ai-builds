import unittest
from dataclasses import replace
from gridsentinel.network import demo_network
from gridsentinel.dispatch import evaluate
from gridsentinel.models import Network

class TestDispatch(unittest.TestCase):
    def test_base_serves_load(self):
        r=evaluate(demo_network());self.assertGreater(r['served_pct'],80)
    def test_failure_creates_islands(self):
        n=demo_network();lines=tuple(l for l in n.lines if l.start!='HOSPITAL' and l.end!='HOSPITAL')
        r=evaluate(Network(n.nodes,lines));self.assertGreaterEqual(len(r['islands']),2)
    def test_critical_priority(self):
        n=demo_network();n=replace(n,nodes=tuple(replace(x,generation_capacity=10 if x.id=='NORTH' else 0) for x in n.nodes))
        r=evaluate(n)
        self.assertAlmostEqual(r['served']['HOSPITAL'],10)
        self.assertEqual(r['served']['INDUSTRY'],0)
    def test_outage_excludes_line(self):self.assertNotIn('L05',evaluate(demo_network(),['L05'])['flows'])
    def test_backup_helps(self):
        n=demo_network()
        a=evaluate(n,('L05',));b=evaluate(n,('L05',),backup=True)
        self.assertGreaterEqual(b['served_pct'],a['served_pct'])
    def test_generation_conservation(self):
        r=evaluate(demo_network(),('L07',));self.assertAlmostEqual(sum(r['generation'].values()),r['served_load'],places=2)
