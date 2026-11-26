import unittest
from aquamind.hydraulics import model,residual_mass_balance
from aquamind.network import JUNCTIONS,PIPES
class HydraulicsTests(unittest.TestCase):
    def test_conservation(self):
        self.assertAlmostEqual(residual_mass_balance(model()),0,places=4)
    def test_leak_increases_supply(self):
        self.assertAlmostEqual(model('J-07',4.5)['source_supply']-model()['source_supply'],4.5,places=4)
    def test_pressure_decreases_under_leak(self):
        self.assertLess(model('J-07',4.5)['pressure']['J-07'],model()['pressure']['J-07'])
    def test_pipe_count(self):self.assertEqual(len(model()['flow']),len(PIPES))
    def test_junction_count(self):self.assertEqual(len(model()['pressure']),len(JUNCTIONS)+1)
    def test_bad_leak(self):
        with self.assertRaises(ValueError):model('J-88',2)
