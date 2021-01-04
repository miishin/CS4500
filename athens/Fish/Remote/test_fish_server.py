import unittest, socket, threading, json
import fish_server

class TestFishServer(unittest.TestCase):

    def setUp(self):
        self.fishServer = fish_server.Server(12345)
        self.p1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.p1.settimeout(1)
        self.p2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.p2.settimeout(1)
        self.p3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.p3.settimeout(1)
        self.p4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.p4.settimeout(1)
        self.p5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.p5.settimeout(1)

    def testWaitingPeriod(self):
        p = []
        t1 = threading.Thread(target=self.connectAndSend(self.p1, "Player 1"))
        t2 = threading.Thread(target=self.connectAndSend(self.p2, "Player 2"))
        t3 = threading.Thread(target=self.connectAndSend(self.p3, "Player 3"))
        t4 = threading.Thread(target=self.connectAndSend(self.p4, "Player 4"))
        t5 = threading.Thread(target=self.connectAndSend(self.p5, "Player 5"))
        t6 = threading.Thread(target=self.runFunc, args=(self.fishServer.waitingPeriod,p))
        t6.start()
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()


        print(p)


    def runFunc(self, func, container):
        container = func()

    def connectAndSend(self, sock, name):
        sock.connect(('127.0.0.1', 12345))
        sock.sendall(str.encode(json.dumps(name)))

if __name__ == '__main__':
    unittest.main()
