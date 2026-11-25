import unittest
from metrorl.qlearning import train
from metrorl.benchmark import evaluate
class Tests(unittest.TestCase):
    def test_training_reproducible(self):
        a,ra=train(episodes=5,horizon=35,seed=9);b,rb=train(episodes=5,horizon=35,seed=9)
        self.assertEqual(a.table,b.table);self.assertEqual(ra,rb)
    def test_training_nonempty(self):self.assertGreater(train(episodes=3,horizon=15)[1]['states_learned'],0)
    def test_invalid_episodes(self):
        with self.assertRaises(ValueError):train(episodes=0)
    def test_benchmark_shape(self):
        r=evaluate(seeds=(12,13),episodes=5)
        self.assertEqual(set(r['scores']),{'fixed_time','max_pressure','q_learning'})
        self.assertEqual(r['scores']['fixed_time']['exits']['n'],2)
