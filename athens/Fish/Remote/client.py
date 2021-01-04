import socket, sys, json, logging

sys.path.append("../Common")
import state, board
import PlayerInfo

sys.path.append("../Player")
import player

BLOCK_SIZE = 4096
TOURNAMENT_START_TIMEOUT = 60
TIMEOUT = 30

"""
A Client represents a remote player connecting to the Server to play in a tournament of Fish.
A Client has:
- self.sock: A socket that connects it to the server
- self.player: An implementation of Player_Interface that it uses to play the game

A Client receives JSON method calls from a ProxyPlayer and interprets them into function calls in
the Player object self.player. Function returns from that object are then turned into JSON that is sent back 
to the ProxyPlayer.
"""


class Client:

    def __init__(self, ip, port, aPlayer):
        """
        Constructor for a Client
        :param ip: ip address of the server it will connect to
        :param port: the port of the server it will connect to
        :param aPlayer: an implementation of the Player_Interface that will play for the Client
        """
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (ip, port)
        self.player = aPlayer
        self.keepRunning = True
        logging.basicConfig(level=logging.INFO)
        self.sock.settimeout(TIMEOUT)

    def connect(self):
        """
        Connects this Client's socket to the Server
        :return: None. Raises an error if connection fails
        """
        try:
            self.sock.connect(self.server_address)
            logging.info('client.py: Connected Socket')
        except ConnectionError:
            raise ConnectionError("Unable to connect")

    def send(self, msg):
        """
        Sends a given message to the connected Server
        :param msg: the message to send (in Python JSON format, ie. must be encoded in JSON)
        :return: None. Raises an error if sending failed
        """
        try:
            message = str.encode(json.dumps(msg))
            self.sock.sendall(message)
            logging.info('client.py: Sent: ' + message.decode())
        except ConnectionError:
            raise ConnectionError(msg + "was not sent")

    def receive(self):
        """
        Receives a message from the server
        :return: The received message
        """
        msg = b''
        while True:
            try:
                data = self.sock.recv(BLOCK_SIZE)
                if data == b'':
                    break
                else:
                    msg += data
                logging.info('client.py: received' + data.decode())
            except ConnectionError:
                raise ConnectionError("did not receive message")
        msg = msg.decode()
        logging.info('client.py: Received: ' + msg)
        return msg

    def run(self):
        """
        Runs this Client. Connects to the server, sends player name, then plays until tournament is over.
        :return: None
        """
        self.runInitialConnection()
        self.send(self.waitTournamentStart())
        self.playTournament()
        self.sock.close()

    def runInitialConnection(self):
        """
        Initial connection the Server
        :return: None
        """
        logging.info('client.py: connecting')
        self.connect()
        self.send(self.player.id)

    def waitTournamentStart(self):
        """
        Waits for tournament start message
        :return:
        """
        logging.info('client.py: going to wait for start')
        self.sock.settimeout(TOURNAMENT_START_TIMEOUT)
        response = self.parseMessage(self.receive())
        self.sock.settimeout(TIMEOUT)
        logging.info('client.py: t started')
        return response

    def playTournament(self):
        """
        Play a single game in a Tournament's Round
        :return:
        """
        logging.info('client.py: going to play')
        while self.keepRunning:
            logging.info('client.py: playing')
            self.sock.settimeout(TIMEOUT)
            msg = self.receive()
            response = self.parseMessage(msg)
            self.send(response)

    def parseMessage(self, msg):
        """
        Parses a message received from the server. This message will be a method call with format:
        [method-name, [arguments, ...]]
        :param msg: The message to be parsed
        :return: The response message. Either "void", Action, or Position
        """
        logging.info('client.py: parsing ' + msg)
        message = json.loads(msg)
        msgType = message[0]
        if msgType == "start" or msgType == "playing-as" or msgType == "playing-with":
            return "void"
        elif msgType == "end":
            self.keepRunning = False
            return "void"
        elif msgType == "setup":
            gstate = self.jsonToState(message[1][0])
            logging.info('client.py: setup')
            return self.player.placeAvatar(gstate)
        elif msgType == "take-turn":
            return self.player.moveAvatar(self.jsonToState(message[1][0]))
        else:
            raise ValueError("invalid message received")

    def jsonToState(self, jsonState):
        """
        Converts a JSON representation of a GameState to a GameState object
        :param jsonState: JSON State
        :return: GameState
        """
        players = jsonState["players"]
        b = jsonState["board"]
        iloplayer = []
        stateBoard = board.Board(tiles=b)
        turnPriority = 0
        for player in players:
            iloplayer.append(PlayerInfo.PlayerInfo(player["color"], turnPriority, player["score"]))
            turnPriority += 1
        return state.State(iloplayer, stateBoard)
