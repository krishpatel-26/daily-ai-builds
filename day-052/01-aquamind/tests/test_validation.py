import unittest
from aquamind.hydraulics import model
from aquamind.sensors import observe
class ValidationTests(unittest.TestCase):
    def test_negative_rate(self):
        with self.assertRaises(ValueError):model('J-06',-1)
    def test_rate_upper_bound(self):
        with self.assertRaises(ValueError):model('J-06',50)
    def test_unknown_pipe(self):
        with self.assertRaises(ValueError):model(closed_pipes=['not-a-pipe'])
    def test_negative_noise(self):
        with self.assertRaises(ValueError):observe(noise_sd=-1)
