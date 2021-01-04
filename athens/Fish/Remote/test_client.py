import unittest, json, socket
import client, remote_player
import player
import devtools, Penguin


class TestClient(unittest.TestCase):

    def setUp(self):
        self.c1 = client.Client('127.0.0.1', 12345, player.Player(1, "p1"))
        self.startMessage = ["start", [True]]
        self.playingAsMessage = ["playing-as", ["red"]]
        self.playingWithMessage = ["playing-with", ["white"]]
        self.setupMessage = ["setup", [{"players":
                                  [{"color": "red", "score": 0, "places": []},
                                   {"color": "white", "score": 0, "places": []}],
                                   "board":
                                   [[1, 1, 1],
                                   [1, 1, 1],
                                   [1, 1, 1]]}]]
        self.takeTurnMessage = ["take-turn", [{"players":
                                  [{"color": "red", "score": 0, "places": [[0, 0]]},
                                   {"color": "white", "score": 0, "places": [[0, 1]]}],
                                   "board":
                                   [[1, 1, 1],
                                   [1, 1, 1],
                                   [1, 1, 1]]},
                                         []]]
        self.exampleState = {"players":
                                  [{"color": Penguin.PenguinColor.red, "score": 0, "places": []},
                                   {"color": Penguin.PenguinColor.white, "score": 0, "places": []}],
                                   "board":
                                   [[1, 1, 1],
                                   [1, 1, 1],
                                   [1, 1, 1]]}
        self.endMessageWin = ["end", [True]]
        self.endMessageLose = ["end", [False]]


    def testParseStart(self):
        self.assertEqual(self.c1.parseMessage(json.dumps(self.startMessage)), "void")

    def testParsePlayingAs(self):
        self.assertEqual(self.c1.parseMessage(json.dumps(self.playingAsMessage)), "void")

    def testParsePlayingWith(self):
        self.assertEqual(self.c1.parseMessage(json.dumps(self.playingWithMessage)), "void")

    def testParseSetup(self):
        self.assertEqual(self.c1.parseMessage(json.dumps(self.setupMessage)), (0, 0))

    def testParseTakeTurn(self):
        self.assertEqual(self.c1.parseMessage(json.dumps(self.takeTurnMessage)), ())

    def testParseEndWin(self):
        self.assertEqual(self.c1.parseMessage(json.dumps(self.endMessageWin)), "void")

    def testParseEndLoss(self):
        self.assertEqual(self.c1.parseMessage(json.dumps(self.endMessageLose)), "void")

    def test_json_to_state(self):
        c1s = self.c1.jsonToState(self.exampleState)
        self.assertDictEqual(devtools.DevTools.returnJSON(c1s), self.setupMessage[1][0])




if __name__=='__main__':
    unittest.main()