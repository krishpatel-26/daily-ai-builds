import unittest
from aquamind.inverse import infer
from aquamind.sensors import observe
class InverseTests(unittest.TestCase):
    def test_identifies_default_fault(self):
        r=infer(observe());self.assertEqual(r['most_likely']['node'],'J-07')
    def test_rate_estimate(self):self.assertAlmostEqual(infer(observe())['most_likely']['estimated_rate'],4.5,delta=.2)
    def test_evidence_ranking(self):
        rows=infer(observe())['all_candidates'];self.assertTrue(all(a['sse']<=b['sse'] for a,b in zip(rows,rows[1:])))
    def test_three_sensors_minimum(self):
        with self.assertRaises(ValueError):infer({'J-01':64.0})
    def test_reject_noise(self):
        with self.assertRaises(ValueError):infer(observe(),noise_sd=0)
    def test_better_fit_than_no_leak(self):
        r=infer(observe());self.assertLess(r['most_likely']['rmse'],r['baseline_rmse'])
