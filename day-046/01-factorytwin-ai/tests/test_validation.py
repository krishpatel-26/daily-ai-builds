import unittest
from dataclasses import replace
from factorytwin.config import Config
from factorytwin.validation import validate
class Tests(unittest.TestCase):
 def test_invalid_minutes(self):
  with self.assertRaises(ValueError):validate(replace(Config(),minutes=0))
