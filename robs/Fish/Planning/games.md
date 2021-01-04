Our data representation for the entire game will be a tree where each node of the tree represents
a game state, and each branch of the tree represents a valid move by a Penguin into the next game state. The 
Nodes of our data structure will contains the following:

    •	State: The current state of the game.
            a state contains the game Board and it's Tile array, a list of all the players in the game, and
            information about each player's Penguins locations on the board, and a turn counter tracking which
            player is allowed to make a move in the current game state.
    •   availableActions: A list of valid moves that can be made from the current game state.
    •	Children: A mapping of valid movements to Nodes representing the child Nodes that can be reached from the current game state.
    •	Parent: A reference to the parent Node, which can be useful when tracing a path through the tree. For the
                top level node, this just points to itself.
    •	fromAction: A Tuple of two Tuples, ( moveFrom, moveTo ) representing the move that took the parent state
                to the current state: 
        o	moveFrom: (fromX, fromY) The x and y coordinate of the tile that the Penguin existed at before moving. Since
                       game state store's the information about the which player has a turn, this coordinate can easily
                       be traced back to the player and penguin that were moved 
        o	moveTo: (toX, toY) The x and y coordinate of the tile that the Penguin was moved to.
Our game tree will be accessed by both a game's referee, and a game's players. A referee can use the game tree
to check the validity of a move that a player attempts to make. A player can use the structure to find moves
and plan future moves. The interface that the referee and players may use includes:

    •	getGameState: gets the game state at the present moment.
    •	getParent: gets parent of the current Node. Can be used to trace paths of movement sequences when planning.
    •	getParentMove: gets the action that resulted in the gamestate of a given Node, in the form of (( fromX, fromY), ( toX, toY)).
    •   getAvailableMoves: gets a list of all movements possible for the player who's turn the gamestate belongs to.
    •   getNextState: given a valid movement action, returns the node containing the reulting state of making that move    •	isTerminal: checks if the current Node is a terminal state, meaning there are no moves can be made
    •   isRoot: checks whetehr the current Node is the root node. Useful when tracing paths througn the tree.
