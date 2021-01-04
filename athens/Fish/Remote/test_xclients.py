import unittest
import xclients

class Testxclients(unittest.TestCase):

    def testCheckGoodArgs(self):
        self.assertTrue(xclients.checkArgs(['./xclients', 4, 12345, '127.0.0.1']))

    def testCheckGoodArgsNoIP(self):
        self.assertTrue(xclients.checkArgs(['./xclients', 4, 12345]))

    def testInvalidPort1(self):
        self.assertFalse(xclients.checkArgs(['./xclients', 4, 0, '127.0.0.1']))

    def testInvalidPort2(self):
        self.assertFalse(xclients.checkArgs(['./xclients', 4, 65536, '127.0.0.1']))

    def testInvalidPortString(self):
        self.assertFalse(xclients.checkArgs(['./xclients', 4, 'bad']))

    def testInvalidNumClients(self):
        self.assertFalse(xclients.checkArgs(['./xclients', 0, 12345]))

    def testInvalidNumClientsString(self):
        self.assertFalse(xclients.checkArgs(['./xclients', 'bad', 12345]))

    def testNoArgs(self):
        self.assertFalse(xclients.checkArgs(['./xclients']))

    def testMakeClients(self):
        clients = xclients.makeClients(5, '127.0.0.1', 12345)
        self.assertEqual(len(clients), 5)


if __name__ == '__main__':
    unittest.main()
