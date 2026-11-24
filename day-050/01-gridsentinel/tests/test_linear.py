import unittest
from gridsentinel.linear import solve_linear

class TestLinear(unittest.TestCase):
    def test_known_solution(self):self.assertEqual([round(x,5) for x in solve_linear([[3,1],[1,2]],[9,8])],[2.0,3.0])
    def test_singular(self):
        with self.assertRaises(ValueError):solve_linear([[1,2],[2,4]],[3,6])
    def test_empty(self):self.assertEqual(solve_linear([],[]),[])
