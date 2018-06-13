import unittest
from LogFunc import *


class AndGateTest(unittest.TestCase):
    def testcase_00(self):
        a = AndGate()
        self.assertFalse(a.Inputs[0], "Class AndGate: Testcase 0 failed.")
        self.assertFalse(a.Inputs[1], "Class AndGate: Testcase 0 failed.")
        self.assertFalse(a.Outputs, "Class AndGate: Testcase 0 failed.")

    def testcase_01(self):
        a = AndGate()
        a.Inputs[0] = False
        a.Inputs[1] = False
        a.execute()
        self.assertFalse(a.Outputs, "Class AndGate: Testcase 1 failed.")

    def testcase_02(self):
        a = AndGate()
        a.Inputs[0] = True
        a.Inputs[1] = False
        a.execute()
        self.assertFalse(a.Outputs, "Class AndGate: Testcase 2 failed.")

    def testcase_03(self):
        a = AndGate()
        a.Inputs[0] = False
        a.Inputs[1] = True
        a.execute()
        self.assertFalse(a.Outputs, "Class AndGate: Testcase 3 failed.")

    def testcase_04(self):
        a = AndGate()
        a.Inputs[0] = True
        a.Inputs[1] = True
        a.execute()
        self.assertTrue(a.Outputs, "Class AndGate: Testcase 4 failed.")

    def testcase_05(self):
        a = AndGate(4)
        a.Inputs[0] = True
        a.Inputs[1] = False
        a.Inputs[2] = True
        a.Inputs[3] = True
        a.execute()
        self.assertFalse(a.Outputs, "Class AndGate: Testcase 5 failed.")

    def testcase_06(self):
        a = AndGate(4)
        a.Inputs[0] = True
        a.Inputs[1] = True
        a.Inputs[2] = True
        a.Inputs[3] = True
        a.execute()
        self.assertTrue(a.Outputs, "Class AndGate: Testcase 6 failed.")


class OrGateTest(unittest.TestCase):
    def testcase_00(self):
        a = OrGate()
        self.assertFalse(a.Inputs[0], "Class OrGate: Testcase 0 failed.")
        self.assertFalse(a.Inputs[1], "Class OrGate: Testcase 0 failed.")
        self.assertFalse(a.Outputs, "Class OrGate: Testcase 0 failed.")

    def testcase_01(self):
        a = OrGate()
        a.Inputs[0] = False
        a.Inputs[1] = False
        a.execute()
        self.assertFalse(a.Outputs, "Class OrGate: Testcase 1 failed.")

    def testcase_02(self):
        a = OrGate()
        a.Inputs[0] = True
        a.Inputs[1] = False
        a.execute()
        self.assertTrue(a.Outputs, "Class OrGate: Testcase 2 failed.")

    def testcase_03(self):
        a = OrGate()
        a.Inputs[0] = False
        a.Inputs[1] = True
        a.execute()
        self.assertTrue(a.Outputs, "Class OrGate: Testcase 3 failed.")

    def testcase_04(self):
        a = OrGate()
        a.Inputs[0] = True
        a.Inputs[1] = True
        a.execute()
        self.assertTrue(a.Outputs, "Class OrGate: Testcase 4 failed.")

    def testcase_05(self):
        a = OrGate(4)
        a.Inputs[0] = False
        a.Inputs[1] = False
        a.Inputs[2] = False
        a.Inputs[3] = False
        a.execute()
        self.assertFalse(a.Outputs, "Class OrGate: Testcase 5 failed.")

    def testcase_06(self):
        a = OrGate(4)
        a.Inputs[0] = False
        a.Inputs[1] = False
        a.Inputs[2] = False
        a.Inputs[3] = True
        a.execute()
        self.assertTrue(a.Outputs, "Class OrGate: Testcase 6 failed.")


class XorGateTest(unittest.TestCase):
    def testcase_00(self):
        a = XorGate()
        self.assertFalse(a.Inputs[0], "Class XorGate: Testcase 0 failed.")
        self.assertFalse(a.Inputs[1], "Class XorGate: Testcase 0 failed.")
        self.assertFalse(a.Outputs, "Class XorGate: Testcase 0 failed.")

    def testcase_01(self):
        a = XorGate()
        a.Inputs[0] = False
        a.Inputs[1] = False
        a.execute()
        self.assertFalse(a.Outputs, "Class XorGate: Testcase 1 failed.")

    def testcase_02(self):
        a = XorGate()
        a.Inputs[0] = True
        a.Inputs[1] = False
        a.execute()
        self.assertTrue(a.Outputs, "Class XorGate: Testcase 2 failed.")

    def testcase_03(self):
        a = XorGate()
        a.Inputs[0] = False
        a.Inputs[1] = True
        a.execute()
        self.assertTrue(a.Outputs, "Class XorGate: Testcase 3 failed.")

    def testcase_04(self):
        a = XorGate()
        a.Inputs[0] = True
        a.Inputs[1] = True
        a.execute()
        self.assertFalse(a.Outputs, "Class XorGate: Testcase 4 failed.")

    def testcase_05(self):
        a = XorGate(4)
        a.Inputs[0] = False
        a.Inputs[1] = True
        a.Inputs[2] = True
        a.Inputs[3] = False
        a.execute()
        self.assertFalse(a.Outputs, "Class XorGate: Testcase 5 failed.")

    def testcase_06(self):
        a = XorGate(4)
        a.Inputs[0] = False
        a.Inputs[1] = False
        a.Inputs[2] = False
        a.Inputs[3] = True
        a.execute()
        self.assertTrue(a.Outputs, "Class XorGate: Testcase 6 failed.")


class NandGateTest(unittest.TestCase):
    def testcase_00(self):
        a = NandGate()
        self.assertFalse(a.Inputs[0], "Class NandGate: Testcase 0 failed.")
        self.assertFalse(a.Inputs[1], "Class NandGate: Testcase 0 failed.")
        self.assertTrue(a.Outputs, "Class NandGate: Testcase 0 failed.")

    def testcase_01(self):
        a = NandGate()
        a.Inputs[0] = False
        a.Inputs[1] = False
        a.execute()
        self.assertTrue(a.Outputs, "Class NandGate: Testcase 1 failed.")

    def testcase_02(self):
        a = NandGate()
        a.Inputs[0] = True
        a.Inputs[1] = False
        a.execute()
        self.assertTrue(a.Outputs, "Class NandGate: Testcase 2 failed.")

    def testcase_03(self):
        a = NandGate()
        a.Inputs[0] = False
        a.Inputs[1] = True
        a.execute()
        self.assertTrue(a.Outputs, "Class NandGate: Testcase 3 failed.")

    def testcase_04(self):
        a = NandGate()
        a.Inputs[0] = True
        a.Inputs[1] = True
        a.execute()
        self.assertFalse(a.Outputs, "Class NandGate: Testcase 4 failed.")

    def testcase_05(self):
        a = NandGate(4)
        a.Inputs[0] = True
        a.Inputs[1] = True
        a.Inputs[2] = True
        a.Inputs[3] = True
        a.execute()
        self.assertFalse(a.Outputs, "Class NandGate: Testcase 5 failed.")

    def testcase_06(self):
        a = NandGate(4)
        a.Inputs[0] = False
        a.Inputs[1] = True
        a.Inputs[2] = True
        a.Inputs[3] = False
        a.execute()
        self.assertTrue(a.Outputs, "Class NandGate: Testcase 6 failed.")


class NotGateTest(unittest.TestCase):
    def testcase_00(self):
        a = NotGate(1)
        self.assertFalse(a.Inputs[0], "Class NotGate: Testcase 0 failed.")
        self.assertTrue(a.Outputs[0], "Class NotGate: Testcase 0 failed.")

    def testcase_01(self):
        a = NotGate(3)
        a.Inputs[0] = False
        a.Inputs[1] = True
        a.Inputs[2] = True
        a.execute()
        self.assertTrue(a.Outputs[0], "Class NotGate: Testcase 1 failed.")
        self.assertFalse(a.Outputs[1], "Class NotGate: Testcase 1 failed.")
        self.assertFalse(a.Outputs[2], "Class NotGate: Testcase 1 failed.")


class HalfAdderTest(unittest.TestCase):
    def testcase_00(self):
        a = HalfAdder()
        self.assertFalse(a.Inputs[0], "Class HalfAdder: Testcase 0 failed.")
        self.assertFalse(a.Inputs[1], "Class HalfAdder: Testcase 0 failed.")
        self.assertFalse(a.Outputs[0], "Class HalfAdder: Testcase 0 failed.")
        self.assertFalse(a.Outputs[1], "Class HalfAdder: Testcase 0 failed.")

    def testcase_01(self):
        a = HalfAdder()
        a.Inputs[0] = False
        a.Inputs[1] = True
        a.execute()
        self.assertFalse(a.Outputs[0], "Class HalfAdder: Testcase 1 failed.")
        self.assertTrue(a.Outputs[1], "Class HalfAdder: Testcase 1 failed.")

    def testcase_02(self):
        a = HalfAdder()
        a.Inputs[0] = True
        a.Inputs[1] = False
        a.execute()
        self.assertFalse(a.Outputs[0], "Class HalfAdder: Testcase 2 failed.")
        self.assertTrue(a.Outputs[1], "Class HalfAdder: Testcase 2 failed.")

    def testcase_03(self):
        a = HalfAdder()
        a.Inputs[0] = True
        a.Inputs[1] = True
        a.execute()
        self.assertTrue(a.Outputs[0], "Class HalfAdder: Testcase 3 failed.")
        self.assertFalse(a.Outputs[1], "Class HalfAdder: Testcase 3 failed.")


class FullAdderTest(unittest.TestCase):
    def testcase_00(self):
        a = FullAdder()
        self.assertFalse(a.Inputs[0], "Class FullAdder: Testcase 0 failed.")
        self.assertFalse(a.Inputs[1], "Class FullAdder: Testcase 0 failed.")
        self.assertFalse(a.Inputs[2], "Class FullAdder: Testcase 0 failed.")
        self.assertFalse(a.Outputs[0], "Class FullAdder: Testcase 0 failed.")
        self.assertFalse(a.Outputs[1], "Class FullAdder: Testcase 0 failed.")

    def testcase_01(self):
        a = FullAdder()
        a.Inputs[0] = False
        a.Inputs[1] = False
        a.Inputs[2] = True
        a.execute()
        self.assertFalse(a.Outputs[0], "Class FullAdder: Testcase 1 failed.")
        self.assertTrue(a.Outputs[1], "Class FullAdder: Testcase 1 failed.")

    def testcase_02(self):
        a = FullAdder()
        a.Inputs[0] = False
        a.Inputs[1] = True
        a.Inputs[2] = False
        a.execute()
        self.assertFalse(a.Outputs[0], "Class FullAdder: Testcase 2 failed.")
        self.assertTrue(a.Outputs[1], "Class FullAdder: Testcase 2 failed.")

    def testcase_03(self):
        a = FullAdder()
        a.Inputs[0] = False
        a.Inputs[1] = True
        a.Inputs[2] = True
        a.execute()
        self.assertTrue(a.Outputs[0], "Class FullAdder: Testcase 3 failed.")
        self.assertFalse(a.Outputs[1], "Class FullAdder: Testcase 3 failed.")

    def testcase_04(self):
        a = FullAdder()
        a.Inputs[0] = True
        a.Inputs[1] = False
        a.Inputs[2] = False
        a.execute()
        self.assertFalse(a.Outputs[0], "Class FullAdder: Testcase 4 failed.")
        self.assertTrue(a.Outputs[1], "Class FullAdder: Testcase 4 failed.")

    def testcase_05(self):
        a = FullAdder()
        a.Inputs[0] = True
        a.Inputs[1] = False
        a.Inputs[2] = True
        a.execute()
        self.assertTrue(a.Outputs[0], "Class FullAdder: Testcase 5 failed.")
        self.assertFalse(a.Outputs[1], "Class FullAdder: Testcase 5 failed.")

    def testcase_06(self):
        a = FullAdder()
        a.Inputs[0] = True
        a.Inputs[1] = True
        a.Inputs[2] = False
        a.execute()
        self.assertTrue(a.Outputs[0], "Class FullAdder: Testcase 6 failed.")
        self.assertFalse(a.Outputs[1], "Class FullAdder: Testcase 6 failed.")

    def testcase_07(self):
        a = FullAdder()
        a.Inputs[0] = True
        a.Inputs[1] = True
        a.Inputs[2] = True
        a.execute()
        self.assertTrue(a.Outputs[0], "Class FullAdder: Testcase 7 failed.")
        self.assertTrue(a.Outputs[1], "Class FullAdder: Testcase 7 failed.")


class EightBitAdderTest(unittest.TestCase):
    def testcase_00(self):
        a = EightBitAdder()
        for i in range(16):
            self.assertFalse(a.Inputs[i], "Class EightBitAdder: Testcase 0 failed.")
        for i in range(9):
            self.assertFalse(a.Outputs[i], "Class EightBitAdder: Testcase 0 failed.")

    def testcase_01(self):
        a = EightBitAdder()
        a.Inputs[0] = True
        a.execute()
        self.assertTrue(a.Outputs[0], "Class EightBitAdder: Testcase 1 failed.")
        for i in range(1, 9):
            self.assertFalse(a.Outputs[i], "Class EightBitAdder: Testcase 1 failed.")

    def testcase_02(self):
        a = EightBitAdder()
        a.Inputs[5] = True
        a.Inputs[5+8] = True        # inputs a5 and b5 = True
        a.execute()
        self.assertTrue(a.Outputs[6], "Class EightBitAdder: Testcase 2 failed.")
        for i in range(1, 6):
            self.assertFalse(a.Outputs[i], "Class EightBitAdder: Testcase 2 failed.")
        for i in range(7, 9):
            self.assertFalse(a.Outputs[i], "Class EightBitAdder: Testcase 2 failed.")

    def testcase_03(self):
        a = EightBitAdder()
        a.Inputs[4] = True
        a.Inputs[4 + 8] = True
        a.Inputs[5] = True     # inputs a4, b4 and a5 = True
        a.execute()
        self.assertTrue(a.Outputs[6], "Class EightBitAdder: Testcase 3 failed.")
        for i in range(1, 6):
            self.assertFalse(a.Outputs[i], "Class EightBitAdder: Testcase 3 failed.")
        for i in range(7, 9):
            self.assertFalse(a.Outputs[i], "Class EightBitAdder: Testcase 3 failed.")

    def testcase_04(self):
        a = EightBitAdder()
        for i in range(7):
            a.Inputs[i] = True
        a.Inputs[15] = True
        a.execute()
        self.assertFalse(a.Outputs[8], "Class EightBitAdder: Testcase 4 failed.")
        for i in range(8):
            self.assertTrue(a.Outputs[i], "Class EightBitAdder: Testcase 4 failed.")

    def testcase_05(self):
        a = EightBitAdder()
        a.Inputs = [True] * 16
        a.execute()
        self.assertFalse(a.Outputs[0], "Class EightBitAdder: Testcase 5 failed.")
        for i in range(1,8):
            self.assertTrue(a.Outputs[i], "Class EightBitAdder: Testcase 5 failed.")


if __name__ == "__main__":
    unittest.main()
