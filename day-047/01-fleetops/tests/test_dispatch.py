import unittest
from fleetops.dispatcher import choose_assignment,nearest_charger
from fleetops.models import Robot,Task
class DispatchTests(unittest.TestCase):
    def test_priority_and_distance(self):
        r=Robot('R',(0,1),80)
        options=[Task('A',(2,1),1,99),Task('B',(2,2),3,99)]
        self.assertEqual(choose_assignment(r,options,0)[0].id,'B')
    def test_low_battery_does_not_assign(self):
        self.assertIsNone(choose_assignment(Robot('R',(0,1),1),[Task('A',(2,1),1,99)],0))
    def test_charge_route(self):self.assertEqual(nearest_charger((1,0))[-1],(0,0))
