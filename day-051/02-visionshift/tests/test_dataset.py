import unittest
from visionshift.dataset import generate,split_dataset
class Tests(unittest.TestCase):
    def test_reproducible(self):self.assertEqual(generate(2,30),generate(2,30))
    def test_binary_labels(self):self.assertTrue(all(r.y in (0,1) for r in generate(2,100)))
    def test_four_features(self):self.assertTrue(all(len(r.x)==4 for r in generate(2,70)))
    def test_bad_shift(self):
        with self.assertRaises(ValueError):generate(2,10,3)
    def test_dataset_splits(self):self.assertEqual(len(split_dataset()['shifted_pool']),400)
