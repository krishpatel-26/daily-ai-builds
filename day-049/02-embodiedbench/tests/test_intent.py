import unittest
from embodiedbench.intent import parse_instruction,sample_tasks
class Tests(unittest.TestCase):
 def test_three_tasks(self):self.assertEqual(len(sample_tasks()),3)
 def test_supported_command(self):self.assertEqual(parse_instruction('move red_cube to zone_a').zone,'zone_a')
 def test_unknown_item(self):
  with self.assertRaises(ValueError):parse_instruction('move invisible_kitten to zone_a')
 def test_invalid_syntax(self):
  with self.assertRaises(ValueError):parse_instruction('delete all machines')
