### File Organization of Remote/

client.py
    
    Contains the Client class that represents a single remote player's client that 
    will connect to a server to play a tournament.
    
server.py

    Contains code that will run a server - waits for a certain number of players 
    to sign up and will retry a waiting period once. Will create a tournament manager
    and make it run the tournament. 
    
remote_player.py

    An implementation of PlayerInterface that represents a proxy for the remote clients to 
    play in the locally hosted game. Function calls that would normally be for a Player directly
    are instead sent as JSON to the remote client, which will return a response. 

xclients.py

    Takes in three arguments:
    - n, the number of clients
    - p, the port number of the server
    - ip, the ip of the server to connect to
    
    Creates n clients, each connected to the server at the ip address on the given port.
    Then runs these clients (connect to and play tournament)

xserver.py

    Takes in one argument:
    - p, the port number to open up
    Opens up port p on local host and runs the Server, which will
    accept incoming connections and run a tournament.
    
test_[file_name]

    Unit test files for each component listed above.
    
### Other Modifications:

Edited state.py and playerinfo.py to be able to return JSON representations of them 
for use in the method calls. This was then later changed to be placed into 
Other/devtools.py because the first implementation created a circular import.

In player_interface.py - added "TournamentLoss" as a update type so that the end(false) call can be run.

In manager.py added getNumCheaters() function to fulfill the runnables 
portion of Assignment 10 (returning [w, cf]). 

In devtools.py we made returnJSON static.

There were some weird import issues scattered everywhere, fixed by using path.append
instead of path.insert.

Edited PlayerInfo to use PenguinColor.value because we couldn't JSON serialize
the enum object (needed the string "red" for example).

In state.py fixed an incorrect comment about kicking players (not specified by color but by index)
Also moved turn incrementation to after penguin placement so if there was an error and the player was 
kicked the game wouldn't increment to skip the next player.

In referee.py fixed an incorrect function call (used color instead of index)
Also fixed high score calculation at the end to return 0 when all players were kicked.

