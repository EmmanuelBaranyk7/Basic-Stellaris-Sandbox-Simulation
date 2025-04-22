import unittest
from empire import Empire, EmpireType
from system import System
from build import Sandbox
from empiretype import create_new_empire, Pacifist, Materialist, Militarist, Egalitarian, Technocratic

class TestEmpire(unittest.TestCase):

    def test_add_system(self):
        empire = Empire()
        sys = System()
        empire.add_system(sys)
        test_cases = [
            (1, empire.system_count),
            (sys.econ_value, empire.economy),
            (2, empire.fleet_cap),
            (-1, empire.military_power) #ehhhh
            #(sys.econ_value, empire.score)
        ]
        self.assertListEqual(empire.systems, [sys])
        for actual, expected in test_cases:
            self.assertEqual(actual, expected)
            #later try mith many values?

    def test_lose_system(self):
        empire = Empire()
        sys = System()
        empire.add_system(sys)
        empire.lose_system(sys)
        test_cases = [
            (0, empire.system_count),
            (0, empire.economy),
            (0, empire.fleet_cap),
            (0, empire.military_power) #ehhhh
            #(0, empire.score)
        ]
        self.assertListEqual(empire.systems, [])
        for actual, expected in test_cases:
            self.assertEqual(actual, expected)
            #does not test sovereign

    def test_vassalize(self):
        ep1 = Empire()
        ep2 = Empire()
        sys1 = System()
        sys2 = System()
        sys1.add_border(sys2)
        ep1.add_system(sys1)
        ep2.add_system(sys2)
        ep1.neighbors.append(ep2)
        ep2.neighbors.append(ep1)  #I might need to make a func for this
        old_cap = ep1.fleet_cap
        ep1.vassalize(ep2)
        self.assertEqual(ep1.fleet_cap, old_cap + ep2.fleet_cap)
        self.assertNotIn(ep2, ep1.neighbors)
        self.assertNotIn(ep1, ep2.neighbors)
        self.assertIn(ep2, ep1.vassals)
        self.assertEqual(ep2.overlord, ep1)

    def test_rescore(self): 
        ep1 = Empire()
        ep2 = Empire()
        sys1 = System()
        ep1.add_system(sys1)
        ep2.add_system(sys1) # same system/ same size/econ etc()
        ep1.neighbors.append(ep2)
        ep2.neighbors.append(ep1)  
        self.assertEqual(ep1.score, ep2.score)
        ep1.vassalize(ep2)  # note: unrealiztic vassaliztion, score too close
        self.assertEqual(ep1.score, ep2.score)
        ep1.rescore() # note, tech is zero (makes * 2 easy)
        self.assertEqual(ep1.score, ep2.score * 2) 




                         

if __name__ == "__main__":
    unittest.main()