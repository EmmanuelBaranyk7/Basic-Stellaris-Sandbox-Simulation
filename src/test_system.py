import unittest
from system import System
from build import Sandbox

class TestSystem(unittest.TestCase):
    def test___init__(self):
        sys = System()
        self.assertIsInstance(sys.size, int)
        self.assertIsInstance(sys.econ_value, int)
        self.assertEqual(sys.sovereign, None)
        self.assertEqual(sys.has_border, False)
        self.assertIsInstance(sys.border_max, int)
        self.assertEqual(sys.border_count, 0)
        self.assertEqual(sys.borders, [])

    def test_add_border(self):
        sys1 = System()
        sys2 = System()
        sys3 = System()
        sys1.add_border(sys2)
        self.assertEqual(sys1.has_border, True)
        self.assertEqual(sys2.has_border, True)
        self.assertEqual(sys1.borders, [sys2])
        self.assertEqual(sys2.borders, [sys1])
        self.assertEqual(sys1.border_count, 1)
        self.assertEqual(sys2.border_count, 1)

    def test_add_system(self):
        sandbox = Sandbox()
        sandbox.create_galaxy(10)
        sys = System()
        sys.add_system(sandbox.galaxy)
        self.assertEqual(sandbox.galaxy[-1].size, sys.size)
        self.assertEqual(sandbox.galaxy[-1].econ_value, sys.econ_value)
        self.assertEqual(sandbox.galaxy[-1].sovereign, sys.sovereign)
        #note, not checked borders in galaxy here becuase they are changed




if __name__ == "__main__":
    unittest.main()