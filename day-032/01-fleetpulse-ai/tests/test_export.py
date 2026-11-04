import unittest
from app.export import telemetry_csv,health_json
class ExportTests(unittest.TestCase):
 def test_csv_header(self):self.assertIn("asset_id,timestamp",telemetry_csv([]))
 def test_json(self):self.assertIn('"health_index": 90',health_json({"health_index":90}))
if __name__=="__main__":unittest.main()