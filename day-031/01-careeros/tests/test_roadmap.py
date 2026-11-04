import unittest
from app.roadmap import build_roadmap
class RoadmapTests(unittest.TestCase):
 def test_items_map_to_gaps(self):
  result=build_roadmap(["Python","RAG"])
  self.assertEqual({x["skill"] for x in result},{"Python","RAG"})
  self.assertTrue(all(x["duration"] for x in result))
if __name__=="__main__": unittest.main()