import unittest
from aquamind.interventions import compare_pipe_isolation
from aquamind.network import PIPES
class InterventionTests(unittest.TestCase):
    def test_all_pipes(self):self.assertEqual(len(compare_pipe_isolation()),len(PIPES))
    def test_infeasible_recorded(self):
        self.assertTrue(all('feasible' in row for row in compare_pipe_isolation()))
    def test_min_pressure_when_feasible(self):
        self.assertTrue(all('minimum_pressure' in row for row in compare_pipe_isolation() if row['feasible']))
