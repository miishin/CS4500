import socket, sys, time, json, logging
import remote_player
sys.path.insert(0, "../Admin")
import manager


"""
Represents a server that will allow a certain number of clients to connect and play in a tournament of Fish.
The server waits for min. # of players to connect
If at the end of a specified timeout the min has not been reached, wait again once
End waiting period when server has accepted maximal number of clients

MIN_PLAYERS: the minimum number of players required to start the tournament
MAX_PLAYERS: the maximum number of players that can enter the tournament
TIMEOUT: How many seconds in one waiting period for incoming signups
NUMBER_RETRIES: How many times to rerun the waiting period when not enough players have signed up
"""

MIN_PLAYERS = 5
MAX_PLAYERS = 10
TIMEOUT = 30
NUMBER_RETRIES = 1
LOCAL_HOST = '127.0.0.1'

class Server:

    # Creates a server given a port, opens up socket with ip local host and given port
    def __init__(self, port):
        """
        Constructor for a Server object.
        :param port: the port to open up on this local machine
        """
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((LOCAL_HOST, self.port))
        logging.basicConfig(level=logging.INFO)

    def runServer(self):
        """
        Runs the server. Accepts signups then runs tournament.
        :return: None
        """
        logging.info('server.py: Running Server')
        self.runTournament(self.waitingPeriod())
        self.sock.close()
        logging.info('server.py: Closing Server')

    def runTournament(self, players):
        """
        Runs the tournament off a given list of players. Creates a Tournament Manager that runs the game,
        then displays the number of winners and cheaters.
        :param players: The Players who will play in the tournament.
        :return: Writes to stdout
        """
        if len(players) >= MIN_PLAYERS:
            tManager = manager.Manager(players)
            tManager._setRowSize(5)
            tManager._setColSize(5)
            tManager._setNumFish(2)
            tManager._setRandomize(False)
            logging.info('Running Tournament')
            tManager.runTournament()
            logging.info('Tournament Finished')
            self.displayResults(tManager)
        else:
            sys.stdout.write("not enough players (minimum %s)\n" % MIN_PLAYERS)

    def displayResults(self, tManager):
        """
        Given a tournament manager, displays the results in the form [w, cf]
        where w is the number of tournament winners and cf is
        the number of players who cheated or failed to respond.
        :param tManager: The Tournament Manager that just ran the tournament for the Server.
        :return: Writes to stdout
        """
        results = []
        results.append(len(tManager.TournamentWinners))
        results.append(tManager.getNumCheaters())
        sys.stdout.write(json.dumps(results))

    def waitingPeriod(self):
        """
        Waits for player signups until either a time limit is reached or enough players have signed up.
        After this time limit will retry until another timeout or sufficient signups.
        :return: The Players who signed up
        """
        players = []
        clients = []
        deadline = time.time() + TIMEOUT
        timeoutCount = 0
        age = 1
        logging.info('Starting Waiting Period')
        while len(players) < MAX_PLAYERS:
            if time.time() >= deadline:
                if timeoutCount == NUMBER_RETRIES:
                    logging.info('Max Retries Reached')
                    break
                else:
                    timeoutCount += 1
                    deadline = time.time() + TIMEOUT
                    logging.info('Restarting Waiting Period')
            else:
                self.sock.settimeout(deadline - time.time())
                self.sock.listen()
                try:
                    conn, addr = self.sock.accept()
                    name = conn.recv(1024)
                    clients.append((conn, addr))
                    players.append(remote_player.RemotePlayer(conn, age, name, 2))
                    age += 1
                    logging.info('Added Player')
                except:
                    continue
            time.sleep(0.05) # Check 20x a second
        return players
