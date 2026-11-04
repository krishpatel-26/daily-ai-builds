import unittest
from app.services import analyze_profile
class ServiceTests(unittest.TestCase):
 def test_analysis_contract(self):
  result=analyze_profile({"resume_text":"Python SQL FastAPI","skills":[],"target_role":"Backend Engineer"})
  self.assertIn("readiness_score",result["analysis"])
  self.assertIn("skill_evidence",result)
  self.assertIn("recommended_projects",result)
  self.assertIn("disclaimer",result)
if __name__=="__main__": unittest.main()