Fish Game

The purpose of this project is to create the board game Fish.

Fish Directory

    -Common: This folder contains the data representations and code necessary to create and run games of Fish, as well as it's components. 
    -Planning: folder contains documents of the design process for each component of Fish.
    -Makefile is used to set up the python environment required for the code to run, and
    is also responsible for making sure that all necessary files are executable.
    -xtest is a testing script used to launch all of the unit tests in the project. Use this file before pushing any 
     changes to github. To use the script, simply type "./xtest" into the command line from the Fish directory,
     and it will display any failed tests or errors that occured in the course of running the unit tests, along
     with the file locations and line numbers of where the program failed. The final output indicates how many total
     tests were run.
     

Common
    
    board.py: This file contains the representation of a Fish game board. It includes a class Board, which
              contains an array of Tiles and data related to the board, such as its height and width in terms of
              the amount of rows of tiles a board has, and how many Tiles exist in a row.
    Tile.py: This files contains the data representation of a Tile and a NoTile. A Fish gameboard is comprised of
            tiles, and these classes represent those tiles or the lack therof. A tile only contains information
            about how many fish it contains.
    state.py: This file contains the data representation of a Fish game state. A state includes a Board with it's 
              Tile array, a list of PlayerInfos, and a counter representing which player has the next turn.
              The state class contains the methods neccesary for a players Penguins to be placed onto or moved on
              a board. It also has methods for getting information about the current state of a game, including the
              positions of each player's Penguins, the tiles which are reachable from any position, 
              the tile array of the gameboard, and whether the game is over.
    PlayerInfo.py: This file contains the data representation of a player's infermation. a PlayerInfo contains
              a count of fish, a penguin color, a turn priority, and a list of penguins. it has methods for getting
              how much fish you have, as well as adding fish to your tally when you land on a tile. It also has methods 
              for adding penguins, and updating there location when it is moved.
    penguin.py: This file contains the data representation of a Penguin. A penguin contains a penguin color,
               a x-position, and a y-position. It contains methods which get there position, color, and sets
               there new position when they are moved.
    xboard.py: This file deserializes the JSON data by splitting it into a board object and a position tuple.
    game_tree.py: This file contains the data representation of a gamenode and a Game. A game node contains a game state,
               all available moves from there. It contains methods which get there gamestate, available moves, and next state given a move.
               A game contains a root node. it also contains methods to query the game tree. 
    xstate.py: This file deserializes the JSON data by splitting it into a board object and a playerInfo object.
    xtree.py: This file deserializes the JSON data by splitting it into a state object and a from position and a to position.
    xstrategy.py: This file deserializes the JSON data by splitting it into a state object and Depth integer, either 1, 2.
    
    
Planning
 
    game-state.md: This file discusses our plans for implementing a the game state.
    games.md: This files discusses our plans for implementing a game state tree
    milestones.pdf: This files establishes our milestones for the fish game.
    self-1.md: This files is our first self evaluation.
    self-2.md: This files is our second self evaluation.
    system.pdf: This files details our system needs with in the context of the three tier architecture.
    
Fish/Player Directory
    
    -strategy: defines the methods for placing a penguin based of the heiristic specified on the assignment page.
    -testStrategy: provides unit tests for the strategy function object
    -player: This file contains the data representation of a Player. A Player contains an age,
               an id. It contains methods which set there color, move there penguins, place there penguins, 
               and get the score at the end of a game.
    -test_player: provides unit tests for the player class
    
    
Fish/Admin Directory

    -referee: defines the rules for placing a penguin and enforce them.
    
3 Directory
    
    -Tests: This folder contains the JSON data we use for testing.
    -xboard: This file is an executible that takes in a:
             Board-Posn is
                    { "position" : Position,
                      "board" : Board}
             and creates a board.
             to use xboard in the 3/ directory, use the command "./xboard < Tests/<n>-in.json" where
             <n> is an interger from 1 to 3. This will create a Board and find the amount of reachable
             tiles on that board from the specified Position
    
4 Directory
    
    -Tests: This folder contains the JSON data we use for testing.
    -xstate: This file is an executible that takes in a:
                State is
                    { "players" : Player*,
                        "board" : Board }
             and creates a board.

5 Directory
    
    -Tests: This folder contains the JSON data we use for testing.
    -xtree: This file is an executible that takes in a:
                 Move-Response-Query is
     { "state" : State,
       "from" : Position,
       "to" : Position }
    INTERPRETATION The object describes the current state and the move that the
    currently active player picked. CONSTRAINT The object is invalid, if the
    specified move is illegal in the given state.
             and makes a move.
    it then creates a:
        Action is
        either
        False false
        or
        [ Position, Position ]
    INTERPRETATION The array describes the opponent's move from the first
    position to the second; if the desired kind of move isn't possible, the
    harness delivers false.

6 Directory
    
    -Tests: This folder contains the JSON data we use for testing.
    -xstrategy: This file is an executible that takes in a:
                 Depth-State is [D, State]
           where D (short for depth) is a Natural in [1,2]

    INTERPRETATION The object includes the state and the depth which is either 1 or 2.
    CONSTRAINT The object is invalid, if the specified move is illegal in the given state.
             and makes a move.
    it then creates a:
        Action is
        either
        False false
        or
        [ Position, Position ]
    INTERPRETATION The array describes the opponent's move from the first
    position to the second; if the desired kind of move isn't possible, the
    harness delivers false.
