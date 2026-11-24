import unittest
from gridsentinel.models import Line
from gridsentinel.powerflow import dc_flow

class TestPowerFlow(unittest.TestCase):
    def test_two_bus(self):self.assertAlmostEqual(dc_flow(['A','B'],[Line('L','A','B',.2,100)],{'A':10,'B':-10})['L'],10)
    def test_unbalanced(self):
        with self.assertRaises(ValueError):dc_flow(['A','B'],[Line('L','A','B',.2,100)],{'A':5,'B':-10})
    def test_single_bus(self):self.assertEqual(dc_flow(['A'],[],{'A':0}),{})
