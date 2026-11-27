import unittest
from orbitshield.scenarios import make
from orbitshield.screening import screen
from orbitshield.report import build
class Tests(unittest.TestCase):
 def test_five_objects(self):self.assertEqual(len(screen(make(53))),5)
 def test_sorted(self):
  rows=screen(make(53));self.assertEqual([r['min_separation_km'] for r in rows],sorted(r['min_separation_km'] for r in rows))
 def test_deterministic(self):self.assertEqual(screen(make(53),step=40),screen(make(53),step=40))
 def test_flagged(self):self.assertTrue(any(r['illustrative_flag'] for r in screen(make(53))))
 def test_bad_seed(self):
  with self.assertRaises(ValueError):make(-1)
