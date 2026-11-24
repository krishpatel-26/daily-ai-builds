import unittest
from supplychain.models import POLICIES,SUPPLIERS
from supplychain.procurement import procurement_orders
class ProcurementTests(unittest.TestCase):
 def test_lean_uses_primary_only(self):
  r=procurement_orders(100,POLICIES['lean'],{s.id:s.capacity_per_day for s in SUPPLIERS},25)
  self.assertEqual({x['source'] for x in r},{'SOURCE-A'})
 def test_dual_source(self):
  r=procurement_orders(100,POLICIES['diversified'],{s.id:s.capacity_per_day for s in SUPPLIERS},25)
  self.assertEqual(len(r),2)
 def test_capacity_conserved(self):
  limit={s.id:s.capacity_per_day for s in SUPPLIERS}
  r=procurement_orders(200,POLICIES['resilient'],limit,25)
  self.assertLessEqual(sum(x['quantity'] for x in r),sum(s.capacity_per_day for s in SUPPLIERS))
 def test_zero_order(self):self.assertEqual(procurement_orders(0,POLICIES['lean'],{'SOURCE-A':50},0),[])
