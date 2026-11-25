import unittest
from metrorl.environment import Corridor
from metrorl.config import Config
from metrorl.policies import fixed_time,max_pressure
class Tests(unittest.TestCase):
    def test_deterministic(self):self.assertEqual(Corridor(seed=5).run(fixed_time),Corridor(seed=5).run(fixed_time))
    def test_conservation(self):
        for seed in range(3):self.assertEqual(Corridor(seed=seed).run(max_pressure)['metrics']['conservation_error'],0)
    def test_capacity(self):
        r=Corridor(seed=8).run(max_pressure)
        self.assertTrue(all(n<=36 and e<=36 for n,e in r['final_queues']))
    def test_bad_action(self):
        with self.assertRaises(ValueError):Corridor().step([0])
    def test_emergency(self):
        r=Corridor().run(max_pressure)
        self.assertGreaterEqual(r['metrics']['emergencies_served'],1)
    def test_invalid_config(self):
        with self.assertRaises(ValueError):Corridor(config=Config(service=0))
