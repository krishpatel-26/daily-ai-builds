import unittest
from metrorl.policies import fixed_time,max_pressure,QPolicy
class Tests(unittest.TestCase):
    def test_fixed_phase(self):self.assertEqual(fixed_time([None],7),[1])
    def test_pressure(self):self.assertEqual(max_pressure([(3,1,1,0),(1,3,0,0)],2),[0,1])
    def test_emergency(self):self.assertEqual(max_pressure([(3,1,0,2)],1),[1])
    def test_qpolicy(self):self.assertEqual(QPolicy({(1,1,0,0):[-3.,0.]}).act([(1,1,0,0)],1),[1])
