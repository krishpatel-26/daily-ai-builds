import unittest
from aegis.data import DOCUMENTS
from aegis.retrieval import retrieve, tokenize

class RetrievalTests(unittest.TestCase):
    def test_tokenization(self):
        self.assertEqual(tokenize("BM25, Retrieval!"), ["bm25", "retrieval"])

    def test_methods_return_valid_document_ids(self):
        valid = {doc_id for doc_id, _ in DOCUMENTS}
        for method in ("bm25", "tfidf", "hybrid"):
            ranked = retrieve(method, "bootstrap confidence intervals", DOCUMENTS, 5)
            self.assertEqual(len(ranked), 5)
            self.assertTrue(set(ranked).issubset(valid))

    def test_unknown_method(self):
        with self.assertRaises(ValueError):
            retrieve("magic", "query", DOCUMENTS)

if __name__ == "__main__":
    unittest.main()
