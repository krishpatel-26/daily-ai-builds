import unittest
from dataclasses import replace
from gridsentinel.network import demo_network,validate
from gridsentinel.graph import components
from gridsentinel.models import Line

class TestNetwork(unittest.TestCase):
    def test_valid_demo(self):validate(demo_network())
    def test_duplicate_line(self):
        n=demo_network()
        with self.assertRaises(ValueError):validate(replace(n,lines=n.lines+(n.lines[0],)))
    def test_components(self):
        n=demo_network();self.assertEqual(len(components([x.id for x in n.nodes],n.lines)),1)
    def test_invalid_reactance(self):
        n=demo_network()
        with self.assertRaises(ValueError):validate(replace(n,lines=(replace(n.lines[0],reactance=0),)+n.lines[1:]))
