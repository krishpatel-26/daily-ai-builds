import unittest
from causalscope.simulator import simulate
from causalscope.infer import diagnose,rank_roots
from causalscope.topology import SERVICES
class InferenceTests(unittest.TestCase):
    def test_default_root(self):self.assertEqual(diagnose(simulate()['timeline'])['most_likely']['service'],'database')
    def test_all_roots_recovered_low_noise(self):
        for root in SERVICES:
            self.assertEqual(diagnose(simulate(root,seed=5,noise_sd=.08)['timeline'])['most_likely']['service'],root)
    def test_ranked_sse(self):
        rows=rank_roots(simulate()['timeline']);self.assertTrue(all(a['sse']<=b['sse'] for a,b in zip(rows,rows[1:])))
    def test_missing_timeline(self):
        with self.assertRaises(ValueError):rank_roots([])
    def test_valid_start_range(self):
        start=diagnose(simulate()['timeline'])['most_likely']['estimated_start'];self.assertTrue(11<=start<=20)
