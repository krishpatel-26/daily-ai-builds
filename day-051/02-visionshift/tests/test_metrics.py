import unittest
from visionshift.dataset import generate
from visionshift.model import LogisticModel
from visionshift.metrics import classify_metrics
class Tests(unittest.TestCase):
    def test_confusion_sums(self):
        rows=generate(3,80);r=classify_metrics(LogisticModel(),rows)
        self.assertEqual(sum(r['confusion'].values()),80)
    def test_bounds(self):
        r=classify_metrics(LogisticModel(),generate(4,60))
        self.assertTrue(all(0<=r[x]<=1 for x in ('accuracy','f1','precision','recall','brier','ece')))
    def test_no_samples(self):
        with self.assertRaises(ValueError):classify_metrics(LogisticModel(),[])
