import unittest
from decisionlab.sensitivity import demand_sensitivity
class SensitivityTests(unittest.TestCase):
    def test_all_combinations(self):self.assertEqual(len(demand_sensitivity()),9)
