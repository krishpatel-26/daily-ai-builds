import unittest
from fleetops.simulator import FleetSimulation
class SimulationTests(unittest.TestCase):
    def test_deterministic(self):self.assertEqual(FleetSimulation(7,80).run(),FleetSimulation(7,80).run())
    def test_unique_positions_every_tick(self):
        r=FleetSimulation(47,110).run()
        for f in r['frames']:
            pts=[tuple(x['position']) for x in f['robots']]
            self.assertEqual(len(pts),len(set(pts)))
    def test_fault_recovery(self):
        r=FleetSimulation().run();events=[e['event'] for e in r['events']]
        self.assertIn('fault',events);self.assertIn('recovered',events)
    def test_no_fault_configuration(self):self.assertEqual(FleetSimulation(faults=False).run()['metrics']['faults'],0)
    def test_task_accounting(self):
        r=FleetSimulation().run();self.assertEqual(r['metrics']['tasks_total'],len(r['tasks']))
        self.assertEqual(r['metrics']['tasks_completed'],sum(t['status']=='completed' for t in r['tasks']))
    def test_invalid_ticks(self):
        with self.assertRaises(ValueError):FleetSimulation(ticks=0)
