import unittest
from supplychain.inventory import Inventory
class InventoryTests(unittest.TestCase):
 def test_transfer_timing(self):
  s=Inventory({'A':4,'B':0});s.schedule('B',3,2,'A');s.receive(1);self.assertEqual(s.on_hand['B'],0);s.receive(2);self.assertEqual(s.on_hand['B'],3)
 def test_inventory_position(self):
  s=Inventory({'A':2});s.schedule('A',4,3,'S');self.assertEqual(s.position('A'),6)
 def test_consume_cannot_go_negative(self):
  s=Inventory({'A':2});self.assertEqual(s.consume('A',8),2);self.assertEqual(s.on_hand['A'],0)
 def test_reject_negative_transfer(self):
  with self.assertRaises(ValueError):Inventory({'A':0}).schedule('A',-2,1,'S')
