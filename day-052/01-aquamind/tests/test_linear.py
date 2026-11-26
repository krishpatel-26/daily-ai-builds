import unittest
from aquamind.linear import solve
class LinearTests(unittest.TestCase):
    def test_two_by_two(self):
        self.assertAlmostEqual(solve([[2,1],[1,3]],[1,2])[0],.2)
    def test_pivoting(self):
        self.assertEqual(solve([[0,1],[1,0]],[3,4]),[4,3])
    def test_singular(self):
        with self.assertRaises(ValueError):solve([[1,1],[2,2]],[2,4])
    def test_bad_shape(self):
        with self.assertRaises(ValueError):solve([[1,2]],[1])
