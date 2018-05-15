import unittest
from LogFunc import *


class AndGateTest(unittest.TestCase):
    
    def testcase_00(self):
        a = AndGate()
        self.assertFalse(a.Input0, "Class AndGate: Testcase 0 failed.")
        self.assertFalse(a.Input1, "Class AndGate: Testcase 0 failed.")        
        self.assertFalse(a.Output, "Class AndGate: Testcase 0 failed.")

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
    
    def testcase_00(self):
        a = OrGate()
        self.assertFalse(a.Input0, "Class OrGate: Testcase 0 failed.")
        self.assertFalse(a.Input1, "Class OrGate: Testcase 0 failed.")        
        self.assertFalse(a.Output, "Class OrGate: Testcase 0 failed.")

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
    
    def testcase_00(self):
        a = XorGate()
        self.assertFalse(a.Input0, "Class XorGate: Testcase 0 failed.")
        self.assertFalse(a.Input1, "Class XorGate: Testcase 0 failed.")        
        self.assertFalse(a.Output, "Class XorGate: Testcase 0 failed.")        

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
    
    def testcase_00(self):
        a = NandGate()
        self.assertFalse(a.Input0, "Class NandGate: Testcase 0 failed.")
        self.assertFalse(a.Input1, "Class NandGate: Testcase 0 failed.")        
        self.assertTrue(a.Output, "Class NandGate: Testcase 0 failed.")

    def testcase_01(self):
        a = NandGate()
        a.Input0 = False
        a.Input1 = False
        a.execute()
        self.assertTrue(a.Output, "Class NandGate: Testcase 1 failed.")

    def testcase_02(self):
        a = NandGate()
        a.Input0 = True
        a.Input1 = False
        a.execute()
        self.assertTrue(a.Output, "Class NandGate: Testcase 2 failed.")

    def testcase_03(self):
        a = NandGate()
        a.Input0 = False
        a.Input1 = True
        a.execute()
        self.assertTrue(a.Output, "Class NandGate: Testcase 3 failed.")

    def testcase_04(self):
        a = NandGate()
        a.Input0 = True
        a.Input1 = True
        a.execute()
        self.assertFalse(a.Output, "Class NandGate: Testcase 4 failed.")

if __name__ == "__main__":
    unittest.main()
