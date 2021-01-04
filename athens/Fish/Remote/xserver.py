from fish_server import Server
from sys import argv

"""
A Server object is run on the local host (ip 127.0.0.1) and a given port.
"""
def main(port):
    serv = Server(port)
    serv.runServer()

# Check that there is only one argument (port number)
# and that it is a valid port
def checkArgs(args):
    """
    Checks input arguments for correctness.
    Should follow format ./xserver p
    p should be 1024<=x<=65535
    :param args: arguments to check
    :return: Boolean. Whether these arguments are valid
    """
    if len(args) == 2:
        try:
            p = int(args[1])
        except ValueError:
            return False
        return 1024 <= p <= 65535
    else:
        print("Incorrect # of args")
        return False

if __name__=='__main__':
    if checkArgs(argv):
        main(int(argv[1]))
    else:
        raise ValueError("Invalid args")

