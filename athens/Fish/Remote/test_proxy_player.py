import unittest, json
import remote_player


class FakeRemotePlayer(remote_player.RemotePlayer):

    def send(self, msg):
        return json.dumps(msg)


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.rp = FakeRemotePlayer(None, 10, "Fake Player 1", 2)

if __name__ == '__main__':
    unittest.main()
