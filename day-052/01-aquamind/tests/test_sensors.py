import unittest
from aquamind.sensors import observe,residuals
from aquamind.network import SENSORS
class SensorTests(unittest.TestCase):
    def test_repeatable(self):self.assertEqual(observe(seed=5),observe(seed=5))
    def test_eight_sensors(self):self.assertEqual(set(observe()),set(SENSORS))
    def test_residual_sign(self):self.assertEqual(residuals({'A':2},{'A':3}),{'A':-1})
    def test_no_overlap(self):
        with self.assertRaises(ValueError):residuals({'A':2},{'B':3})
