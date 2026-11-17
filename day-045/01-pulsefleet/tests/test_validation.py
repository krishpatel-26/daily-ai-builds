import unittest
from pulsefleet.validation import parse_record
BASE={"robot_id":"AMR-01","timestamp":"2026-11-18T08:00:00+00:00","battery_v":25,"motor_temp_c":48,"vibration_mm_s":2,"current_a":7}
class ValidationTests(unittest.TestCase):
 def test_valid_record(self):self.assertEqual(parse_record(BASE).robot_id,"AMR-01")
 def test_missing_field(self):
  with self.assertRaises(ValueError):parse_record({"robot_id":"AMR-01"})
 def test_out_of_range(self):
  with self.assertRaises(ValueError):parse_record({**BASE,"battery_v":-1})
if __name__=="__main__":unittest.main()
