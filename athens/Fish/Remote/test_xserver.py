import unittest
import xserver

class MyTestCase(unittest.TestCase):

    def testCheckArgsGood(self):
        self.assertTrue(xserver.checkArgs(['xserver', 12345]))

    def testCheckArgsEmpty(self):
        self.assertFalse(xserver.checkArgs([]))

    def testCheckArgsNoArgs(self):
        self.assertFalse(xserver.checkArgs(['xserver']))

    def testCheckArgsBadPort(self):
        self.assertFalse(xserver.checkArgs(['xserver', 100]))

    def testCheckArgsBadPort2(self):
        self.assertFalse(xserver.checkArgs(['xserver', 65536]))

    def testCheckArgsBadPortString(self):
        self.assertFalse(xserver.checkArgs(['xserver', 'asdf']))


if __name__ == '__main__':
    unittest.main()
