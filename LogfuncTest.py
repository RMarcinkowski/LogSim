import unittest
from Logfunc import AndGate

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


if __name__ == "__main__":
    unittest.main()                     # führt automatisch alle Methoden aus,
                                        # die mit "testcase_" beginnen.
