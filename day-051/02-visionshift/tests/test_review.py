import unittest
from visionshift.review import review_queue
from visionshift.dataset import generate
from visionshift.model import LogisticModel
class Tests(unittest.TestCase):
 def test_queue_does_not_expose_labels(self):
  rows=review_queue(generate(1,22),LogisticModel(),10)
  self.assertEqual(len(rows),10);self.assertNotIn('y',rows[0])
 def test_sorted_uncertainty(self):
  m=LogisticModel().train(generate(1,50));r=review_queue(generate(2,30),m,10)
  self.assertEqual([x['uncertainty'] for x in r],sorted((x['uncertainty'] for x in r),reverse=True))
