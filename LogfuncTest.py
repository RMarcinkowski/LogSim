import unittest
from Logfunc import AndGate

class AndGateTest(unittest.TestCase):
    def testcase_01(self):
        a = AndGate()
        a.Input0 = False
        a.Input1 = False
        a.execute()
        self.assertFalse(a.Output, "Class AndGate: Testcase 1 failed.")

if __name__ == "__main__":
    unittest.main()                     # führt automatisch alle Methoden aus,
                                        # die mit "testcase_" beginnen.
