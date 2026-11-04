import unittest
from app.gap_analysis import analyze_gaps
class GapTests(unittest.TestCase):
 def test_full_match(self):
  skills=["Python","SQL","FastAPI","Docker","Cloud","Git","Testing","System Design","Communication"]
  self.assertEqual(analyze_gaps(skills,"Backend Engineer")["readiness_score"],100)
 def test_missing_prioritized(self):
  result=analyze_gaps(["Python"],"AI Engineer")
  self.assertTrue(any(x["skill"]=="RAG" and x["priority"]=="high" for x in result["gaps"]))
if __name__=="__main__": unittest.main()