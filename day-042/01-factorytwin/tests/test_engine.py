import unittest
from app.data import generate
from app.engine import analyze
class T(unittest.TestCase):
 def test_five_assets(self):self.assertEqual(len(analyze(generate())),5)
 def test_sorted(self):
  x=analyze(generate());self.assertEqual(x,sorted(x,key=lambda z:z["risk_score"],reverse=True))
 def test_diagnostics(self):self.assertIn("maintenance",analyze(generate())[0])
if __name__=="__main__":unittest.main()