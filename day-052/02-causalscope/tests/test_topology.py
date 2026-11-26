import unittest
from causalscope.topology import SERVICES,EDGES,downstream_hops,topology
class TopologyTests(unittest.TestCase):
    def test_eight_services(self):self.assertEqual(len(SERVICES),8)
    def test_database_downstream(self):
        nodes=downstream_hops('database')
        self.assertEqual(nodes['database'],0)
        self.assertGreater(nodes['frontend'],0)
    def test_frontend_has_no_descendants(self):self.assertEqual(downstream_hops('frontend'),{'frontend':0})
    def test_bad_root(self):
        with self.assertRaises(ValueError):downstream_hops('imaginary-service')
    def test_edges_in_topology(self):self.assertEqual(len(topology()['dependencies']),len(EDGES))
