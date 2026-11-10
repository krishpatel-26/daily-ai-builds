import unittest
from app.validator import validate_template,validate_progress
from app.templates import TEMPLATES
class T(unittest.TestCase):
 def test_templates_valid(self):
  for t in TEMPLATES:self.assertTrue(validate_template(t)[0])
 def test_unknown_progress(self):
  r=validate_progress(TEMPLATES[0],["not_real"]);self.assertFalse(r["valid"])
if __name__=="__main__":unittest.main()