import socket, json, logging
from time import sleep
from sys import path

path.insert(0, "../Common")
import player_interface, state
from Penguin import PenguinColor

path.insert(0, "../Other")
import devtools

BLOCK_SIZE = 4096
TIMEOUT = 1.0

"""
ProxyPlayer is the representation of an internal Proxy for an external Player/Client. 
Function calls that are usually called on an internal player are routed through the ProxyPlayer 
as JSON to a Client that will respond with JSON to be decoded and returned to the Referee or Manager.
"""


class ProxyPlayer(player_interface.PlayerInterface):

    def __init__(self, conn, age, id, depth=1):
        """
        Constructor for a RemotePlayer
        :param conn: The Socket it will communicate over with the external Client
        :param age: The age of the Player
        :param id: The id of the Player
        :param depth: The depth it will use in its strategy component
        """
        self.conn = conn
        self.age = age
        self.id = id
        self.depth = depth
        logging.basicConfig(level=logging.INFO)

    def notifyTournamentUpdate(self, msg):
        """
        Inform player of update regarding Tournament.
        :param msg: Update message from Tournament Manager
        :return: The response to the message
        """
        if msg["type"] == player_interface.TournamentUpdateType.TournamentStart:
            self.start(True)
        elif msg["type"] == player_interface.TournamentUpdateType.TournamentLoss:
            self.end(False)
        elif msg["type"] == player_interface.TournamentUpdateType.TournamentWin:
            self.end(True)
            return "WIN"

    def assignColor(self, color: PenguinColor):
        """
        Assigns a color to this Player
        :param color: the color of this player
        :return: The response to this assignment.
        """
        msg = ["playing-as", [color.value]]
        self.send(msg)
        return self.receive()

    def placeAvatar(self, s: state.State):
        """
        Sends ["setup"...] message.
        :param s: The State to encode in message
        :return: The response from the Client. Should be a Position.
        """
        msg = ["setup", [devtools.DevTools.returnJSON(s)]]
        self.send(msg)
        return self.receive()

    def moveAvatar(self, s: state.State):
        """
        Sends the ["take-turn"...] message
        :param s: The State to encode in the message
        :return: The response from the Client. Should be an Action.
        """
        msg = ["take-turn", [devtools.DevTools.returnJSON(s), []]]
        self.send(msg)
        return self.receive()

    def playingWith(self, colors):
        """
        Sends the external Client information about the other Players in the game.
        :param colors: The colors of the other players
        :return: The response from the Client.
        """
        msg = ["playing-with", [colors]]
        self.send(msg)
        return self.receive()

    def start(self, b):
        """
        Notifies external Client of Tournament start
        :param b: Boolean value. Always True.
        :return: The response from the Client.
        """
        msg = ["start", [b]]
        self.send(msg)

    def end(self, b):
        """
        Notifies external Client of Tournament results
        :param b: Boolean indicating Win
        :return: The response from the Client
        """
        msg = ["end", [b]]
        self.send(msg)

    def send(self, msg):
        """
        Sends a given message to the external Client
        :param msg: The message to send as JSON
        :return: None. Raises an error if sending fails
        """
        try:
            message = json.dumps(msg)
            self.conn.sendall(str.encode(message))
            logging.info('player: Sent: ' + message)
        except ValueError:
            raise ValueError(msg + "was not sent")

    def receive(self):
        """
        Receives a message from the external Client
        :return: The message received. Raises error if there is an issue with receiving
        """
        msg = b''
        while True:
            try:
                data = self.conn.recv(BLOCK_SIZE)
                msg += data
                if data == "":
                    break
            except ValueError:
                raise ValueError("did not receive message")
        logging.info('player: Received: ' + msg.decode())
        return json.loads(msg.decode())
