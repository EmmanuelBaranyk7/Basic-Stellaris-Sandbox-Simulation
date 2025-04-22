import unittest
import random
from empire import Empire, EmpireType
from system import System
from build import Sandbox
from empiretype import create_new_empire, Pacifist, Materialist, Militarist, Egalitarian, Technocratic

class TestBuild(unittest.TestCase):
    def test__int__(self):
        sandbox = Sandbox()
        test_cases = [
            (sandbox.end_year, 0),
            (sandbox.contigency_start_year, 0),
            (sandbox.current_year, 0),
            (sandbox.galaxy, []),
            (sandbox.empires, [])
        ]
        for actual, expected in test_cases:
            self.assertEqual(actual, expected)

    def test_create_galaxy(self):
        sandbox = Sandbox()
        sandbox.create_galaxy(10)
        for system in sandbox.galaxy:
            self.assertIsInstance(system, System)
            self.assertIsInstance(system.name, type(" "))

    def test_create_galaxy_borders(self):
        sandbox = Sandbox()
        sandbox.create_galaxy(10)
        for system in sandbox.galaxy:
            self.assertLessEqual(system.border_count, 3)
            self.assertLessEqual(1, system.border_count)
            #self.assertEqual(system.has_border, True)
            self.assertLessEqual(1, len(system.borders))
            for border in system.borders:
                self.assertIsInstance(border, System)

    def test_colonize_empires(self):
        sandbox = Sandbox()
        sandbox.create_galaxy(10)
        sandbox.colonize_empires(2)
        for sys in sandbox.galaxy:
            if sys.sovereign != None:
                self.assertIsInstance(sys.sovereign, Empire)
                self.assertIn(sys.sovereign, sandbox.empires)
                self.assertEqual(sys.sovereign.systems[0].borders, sys.borders)
        self.assertEqual(len(sandbox.empires), 2)

    def test_create_system_names_list(self):
        sandbox = Sandbox()
        sandbox.create_system_names_list()
        self.assertEqual(sandbox.s_names[0], "Xyphor-7")
        self.assertEqual(sandbox.s_names[23], "Maveros")
        self.assertEqual(sandbox.s_names[71], "Jornath Prime")

    

            


if __name__ == "__main__":
    unittest.main()