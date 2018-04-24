import unittest
from LogFunc import *

class AndGateTest(unittest.TestCase):
    def testcase_01(self):
        a = AndGate()
        a.Input0 = False
        a.Input1 = False
        a.execute()
        self.assertFalse(a.Output, "Class AndGate: Testcase 1 failed.")

    def testcase_02(self):
        a = AndGate()
        a.Input0 = True
        a.Input1 = False
        a.execute()
        self.assertFalse(a.Output, "Class AndGate: Testcase 2 failed.")

    def testcase_03(self):
        a = AndGate()
        a.Input0 = False
        a.Input1 = True
        a.execute()
        self.assertFalse(a.Output, "Class AndGate: Testcase 3 failed.")

    def testcase_04(self):
        a = AndGate()
        a.Input0 = True
        a.Input1 = True
        a.execute()
        self.assertTrue(a.Output, "Class AndGate: Testcase 4 failed.")

class OrGateTest(unittest.TestCase):
    def testcase_01(self):
        a = OrGate()
        a.Input0 = False
        a.Input1 = False
        a.execute()
        self.assertFalse(a.Output, "Class OrGate: Testcase 1 failed.")

    def testcase_02(self):
        a = OrGate()
        a.Input0 = True
        a.Input1 = False
        a.execute()
        self.assertTrue(a.Output, "Class OrGate: Testcase 2 failed.")

    def testcase_03(self):
        a = OrGate()
        a.Input0 = False
        a.Input1 = True
        a.execute()
        self.assertTrue(a.Output, "Class OrGate: Testcase 3 failed.")

    def testcase_04(self):
        a = OrGate()
        a.Input0 = True
        a.Input1 = True
        a.execute()
        self.assertTrue(a.Output, "Class OrGate: Testcase 4 failed.")

class XorGateTest(unittest.TestCase):
    def testcase_01(self):
        a = XorGate()
        a.Input0 = False
        a.Input1 = False
        a.execute()
        self.assertFalse(a.Output, "Class XorGate: Testcase 1 failed.")

    def testcase_02(self):
        a = XorGate()
        a.Input0 = True
        a.Input1 = False
        a.execute()
        self.assertTrue(a.Output, "Class XorGate: Testcase 2 failed.")

    def testcase_03(self):
        a = XorGate()
        a.Input0 = False
        a.Input1 = True
        a.execute()
        self.assertTrue(a.Output, "Class XorGate: Testcase 3 failed.")

    def testcase_04(self):
        a = XorGate()
        a.Input0 = True
        a.Input1 = True
        a.execute()
        self.assertFalse(a.Output, "Class XorGate: Testcase 4 failed.")

class NandGateTest(unittest.TestCase):
    def testcase_01(self):
        a = NandGate()
        a.Input0 = False
        a.Input1 = False
        a.execute()
        self.assertTrue(a.Output, "Class AndGate: Testcase 1 failed.")

    def testcase_02(self):
        a = NandGate()
        a.Input0 = True
        a.Input1 = False
        a.execute()
        self.assertTrue(a.Output, "Class AndGate: Testcase 2 failed.")

    def testcase_03(self):
        a = NandGate()
        a.Input0 = False
        a.Input1 = True
        a.execute()
        self.assertTrue(a.Output, "Class AndGate: Testcase 3 failed.")

    def testcase_04(self):
        a = NandGate()
        a.Input0 = True
        a.Input1 = True
        a.execute()
        self.assertFalse(a.Output, "Class AndGate: Testcase 4 failed.")
if __name__ == "__main__":
    unittest.main()
