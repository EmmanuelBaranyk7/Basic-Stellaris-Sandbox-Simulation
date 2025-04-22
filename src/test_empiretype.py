import unittest
from empiretype import create_new_empire, Pacifist, Egalitarian, Technocratic, Materialist, Militarist
from empire import EmpireType

class TestEmpireType(unittest.TestCase):
    def test_create_new_empire(self):
        empire = create_new_empire()
        self.assertIsInstance(empire.empire_type, EmpireType)

    def test_Pacifist__init__(self):
        pe = Pacifist()
        self.assertIsInstance(pe, Pacifist)
        self.assertEqual(pe.empire_type, EmpireType.PACIFIST)

    def test_Militarist__init__(self):
        me = Militarist()
        self.assertIsInstance(me, Militarist)
        self.assertEqual(me.empire_type, EmpireType.MILITARIST)

    def test_Materialist__init__(self):
        me = Materialist()
        self.assertIsInstance(me, Materialist)
        self.assertEqual(me.empire_type, EmpireType.MATERIALIST)

    def test_Technocratic__init__(self):
        te = Technocratic()
        self.assertIsInstance(te, Technocratic)
        self.assertEqual(te.empire_type, EmpireType.TECHNOCRATIC)

    def test_Egaliterian__init__(self):
        ee = Egalitarian()
        self.assertIsInstance(ee, Egalitarian)
        self.assertEqual(ee.empire_type, EmpireType.EGALITERIAN)


if __name__ == "__main__":
    unittest.main()