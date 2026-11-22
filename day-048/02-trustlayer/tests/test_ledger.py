import unittest
from trustlayer.ledger import Ledger
class LedgerTests(unittest.TestCase):
 def test_valid_chain(self):
  l=Ledger();l.append({'a':1});l.append({'a':2});self.assertTrue(l.verify())
 def test_tamper_detected(self):
  l=Ledger();l.append({'a':1});l.append({'a':2});l.entries[0]['event']['a']=3;self.assertFalse(l.verify())
 def test_previous_hash_bound(self):
  l=Ledger();first=l.append({'a':1});second=l.append({'a':2});self.assertEqual(second['previous_hash'],first['hash'])