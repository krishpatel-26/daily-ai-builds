import unittest
from app.projects import recommend_projects
class ProjectTests(unittest.TestCase):
 def test_projects_map_to_missing_skills(self):
  result=recommend_projects(["RAG","Python"])
  self.assertTrue(result)
  self.assertTrue(any("RAG" in p["matched_gaps"] for p in result))
if __name__=="__main__": unittest.main()