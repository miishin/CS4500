import sys, threading
from client import Client
import player
import threading

LOCAL_HOST = '127.0.0.1'

"""
xclients is run: ./xclients n p ip
n: the number of clients to create
ip: the ip of the server that these clients will connect to
p: the port of the server that these clients will connect to

Creates n clients that connect to a server at ip:p and play a tournament of fish
"""
def main(args):
    num_clients, port, ip = args
    clients = makeClients(int(num_clients), ip, int(port))
    for client in clients:
        clientThread = threading.Thread(target=client.run)
        clientThread.start()

def makeClients(num_clients, ip, port):
    """
    Creates Clients
    :param num_clients: the number of Clients to make
    :param ip: the ip that these Clients connect to
    :param port: the port of the Server that these Clients connect to
    :return: [Client] a list of Clients
    """
    clients = []
    age = 1
    for n in range(num_clients):
        p = player.Player(age, "player " + str(age), 2)
        clients.append(Client(ip, port, p))
        age += 1
    return clients

def checkArgs(args):
    """
    Checks input arguments for correctness.
    Should follow format ./xclients n p ip
    n should be an integer, p should be 1024<=x<=65535
    :param args: arguments to check
    :return: Boolean. Whether these arguments are valid
    """
    if len(args) == 3 or len(args) == 4:
        try:
            n = int(args[1])
            p = int(args[2])
            return n > 0 and 1024 <= p <= 65535
        except ValueError:
            return False
    else:
        return False

if __name__=='__main__':
    # Check if there is an ip argument, if not, set it to local host
    # If there are < 3 or > 4 args, args are invalid
    args = sys.argv
    if checkArgs(args):
        if len(args) == 3:
            args.append(LOCAL_HOST)
        main(args[1:])
    else:
        raise ValueError("./xclients n p ip")