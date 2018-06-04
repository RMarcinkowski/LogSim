import unittest
from LogFunc import *


class AndGateTest(unittest.TestCase):
    def testcase_00(self):
        a = AndGate()
        self.assertFalse(a.Inputs[0], "Class AndGate: Testcase 0 failed.")
        self.assertFalse(a.Inputs[1], "Class AndGate: Testcase 0 failed.")
        self.assertFalse(a.Outputs[0], "Class AndGate: Testcase 0 failed.")

    def testcase_01(self):
        a = AndGate()
        a.Inputs[0] = False
        a.Inputs[1] = False
        a.execute()
        self.assertFalse(a.Outputs[0], "Class AndGate: Testcase 1 failed.")

    def testcase_02(self):
        a = AndGate()
        a.Inputs[0] = True
        a.Inputs[1] = False
        a.execute()
        self.assertFalse(a.Outputs[0], "Class AndGate: Testcase 2 failed.")

    def testcase_03(self):
        a = AndGate()
        a.Inputs[0] = False
        a.Inputs[1] = True
        a.execute()
        self.assertFalse(a.Outputs[0], "Class AndGate: Testcase 3 failed.")

    def testcase_04(self):
        a = AndGate()
        a.Inputs[0] = True
        a.Inputs[1] = True
        a.execute()
        self.assertTrue(a.Outputs[0], "Class AndGate: Testcase 4 failed.")

    def testcase_05(self):
        a = AndGate(4, 2)
        a.Inputs[0] = True
        a.Inputs[1] = False
        a.Inputs[2] = True
        a.Inputs[3] = True
        a.execute()
        self.assertFalse(a.Outputs[0], "Class AndGate: Testcase 5 failed.")
        self.assertFalse(a.Outputs[1], "Class AndGate: Testcase 5 failed.")

    def testcase_06(self):
        a = AndGate(4, 2)
        a.Inputs[0] = True
        a.Inputs[1] = True
        a.Inputs[2] = True
        a.Inputs[3] = True
        a.execute()
        self.assertTrue(a.Outputs[0], "Class AndGate: Testcase 6 failed.")
        self.assertTrue(a.Outputs[1], "Class AndGate: Testcase 6 failed.")


class OrGateTest(unittest.TestCase):

    def testcase_00(self):
        a = OrGate()
        self.assertFalse(a.Inputs[0], "Class OrGate: Testcase 0 failed.")
        self.assertFalse(a.Inputs[1], "Class OrGate: Testcase 0 failed.")
        self.assertFalse(a.Outputs[0], "Class OrGate: Testcase 0 failed.")

    def testcase_01(self):
        a = OrGate()
        a.Inputs[0] = False
        a.Inputs[1] = False
        a.execute()
        self.assertFalse(a.Outputs[0], "Class OrGate: Testcase 1 failed.")

    def testcase_02(self):
        a = OrGate()
        a.Inputs[0] = True
        a.Inputs[1] = False
        a.execute()
        self.assertTrue(a.Outputs[0], "Class OrGate: Testcase 2 failed.")

    def testcase_03(self):
        a = OrGate()
        a.Inputs[0] = False
        a.Inputs[1] = True
        a.execute()
        self.assertTrue(a.Outputs[0], "Class OrGate: Testcase 3 failed.")

    def testcase_04(self):
        a = OrGate()
        a.Inputs[0] = True
        a.Inputs[1] = True
        a.execute()
        self.assertTrue(a.Outputs[0], "Class OrGate: Testcase 4 failed.")

    def testcase_05(self):
        a = OrGate(4, 2)
        a.Inputs[0] = False
        a.Inputs[1] = False
        a.Inputs[2] = False
        a.Inputs[3] = False
        a.execute()
        self.assertFalse(a.Outputs[0], "Class OrGate: Testcase 5 failed.")
        self.assertFalse(a.Outputs[1], "Class OrGate: Testcase 5 failed.")

    def testcase_06(self):
        a = OrGate(4, 2)
        a.Inputs[0] = False
        a.Inputs[1] = False
        a.Inputs[2] = False
        a.Inputs[3] = True
        a.execute()
        self.assertTrue(a.Outputs[0], "Class OrGate: Testcase 6 failed.")
        self.assertTrue(a.Outputs[1], "Class OrGate: Testcase 6 failed.")


class XorGateTest(unittest.TestCase):

    def testcase_00(self):
        a = XorGate()
        self.assertFalse(a.Inputs[0], "Class XorGate: Testcase 0 failed.")
        self.assertFalse(a.Inputs[1], "Class XorGate: Testcase 0 failed.")
        self.assertFalse(a.Outputs[0], "Class XorGate: Testcase 0 failed.")

    def testcase_01(self):
        a = XorGate()
        a.Inputs[0] = False
        a.Inputs[1] = False
        a.execute()
        self.assertFalse(a.Outputs[0], "Class XorGate: Testcase 1 failed.")

    def testcase_02(self):
        a = XorGate()
        a.Inputs[0] = True
        a.Inputs[1] = False
        a.execute()
        self.assertTrue(a.Outputs[0], "Class XorGate: Testcase 2 failed.")

    def testcase_03(self):
        a = XorGate()
        a.Inputs[0] = False
        a.Inputs[1] = True
        a.execute()
        self.assertTrue(a.Outputs[0], "Class XorGate: Testcase 3 failed.")

    def testcase_04(self):
        a = XorGate()
        a.Inputs[0] = True
        a.Inputs[1] = True
        a.execute()
        self.assertFalse(a.Outputs[0], "Class XorGate: Testcase 4 failed.")

    def testcase_05(self):
        a = XorGate(4, 2)
        a.Inputs[0] = False
        a.Inputs[1] = True
        a.Inputs[2] = True
        a.Inputs[3] = False
        a.execute()
        self.assertFalse(a.Outputs[0], "Class XorGate: Testcase 5 failed.")
        self.assertFalse(a.Outputs[1], "Class XorGate: Testcase 5 failed.")

    def testcase_06(self):
        a = XorGate(4, 2)
        a.Inputs[0] = False
        a.Inputs[1] = False
        a.Inputs[2] = False
        a.Inputs[3] = True
        a.execute()
        self.assertTrue(a.Outputs[0], "Class XorGate: Testcase 6 failed.")
        self.assertTrue(a.Outputs[1], "Class XorGate: Testcase 6 failed.")


class NandGateTest(unittest.TestCase):

    def testcase_00(self):
        a = NandGate()
        self.assertFalse(a.Inputs[0], "Class NandGate: Testcase 0 failed.")
        self.assertFalse(a.Inputs[1], "Class NandGate: Testcase 0 failed.")
        self.assertTrue(a.Outputs[0], "Class NandGate: Testcase 0 failed.")

    def testcase_01(self):
        a = NandGate()
        a.Inputs[0] = False
        a.Inputs[1] = False
        a.execute()
        self.assertTrue(a.Outputs[0], "Class NandGate: Testcase 1 failed.")

    def testcase_02(self):
        a = NandGate()
        a.Inputs[0] = True
        a.Inputs[1] = False
        a.execute()
        self.assertTrue(a.Outputs[0], "Class NandGate: Testcase 2 failed.")

    def testcase_03(self):
        a = NandGate()
        a.Inputs[0] = False
        a.Inputs[1] = True
        a.execute()
        self.assertTrue(a.Outputs[0], "Class NandGate: Testcase 3 failed.")

    def testcase_04(self):
        a = NandGate()
        a.Inputs[0] = True
        a.Inputs[1] = True
        a.execute()
        self.assertFalse(a.Outputs[0], "Class NandGate: Testcase 4 failed.")

    def testcase_05(self):
        a = NandGate(4, 2)
        a.Inputs[0] = True
        a.Inputs[1] = True
        a.Inputs[2] = True
        a.Inputs[3] = True
        a.execute()
        self.assertFalse(a.Outputs[0], "Class NandGate: Testcase 5 failed.")
        self.assertFalse(a.Outputs[1], "Class NandGate: Testcase 5 failed.")

    def testcase_06(self):
        a = NandGate(4, 2)
        a.Inputs[0] = False
        a.Inputs[1] = True
        a.Inputs[2] = True
        a.Inputs[3] = False
        a.execute()
        self.assertTrue(a.Outputs[0], "Class NandGate: Testcase 6 failed.")
        self.assertTrue(a.Outputs[1], "Class NandGate: Testcase 6 failed.")


class NotGateTest(unittest.TestCase):

    def testcase_00(self):
        a = NotGate(1,1)
        self.assertFalse(a.Inputs[0], "Class NotGate: Testcase 0 failed.")
        self.assertTrue(a.Outputs[0], "Class NotGate: Testcase 0 failed.")

    def testcase_01(self):
        a = NotGate(3, 3)
        a.Inputs[0] = False
        a.Inputs[1] = True
        a.Inputs[2] = True
        a.execute()
        self.assertTrue(a.Outputs[0], "Class NotGate: Testcase 1 failed.")
        self.assertFalse(a.Outputs[1], "Class NotGate: Testcase 1 failed.")
        self.assertFalse(a.Outputs[2], "Class NotGate: Testcase 1 failed.")

    def testcase_02(self):
        with self.assertRaises(ArithmeticError):
            NotGate()
        with self.assertRaises(ArithmeticError):
            NotGate(3, 4)


if __name__ == "__main__":
    unittest.main()
