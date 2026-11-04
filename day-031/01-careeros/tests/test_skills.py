import unittest
from app.skills import extract_skills, normalize_skills
class SkillTests(unittest.TestCase):
 def test_extracts_evidence(self):
  result=extract_skills("Built APIs with Python and FastAPI; deployed a RAG system.")
  names={x["skill"] for x in result}
  self.assertTrue({"Python","FastAPI","RAG"}.issubset(names))
  self.assertTrue(all(x["evidence"] and not x["verified"] for x in result))
 def test_normalize(self):
  self.assertEqual(normalize_skills(["Python"," Python ",""]),["Python"])
if __name__=="__main__": unittest.main()