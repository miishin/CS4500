### Data Representation:
Our representation of a game state contains:

    - A Board
    - A list of PlayerInfo
    - A turn counter

A Board contains:

    - A 2D array of Tiles. These Tiles include holes and # of fish on each tile as well.

The order of the list of PlayerInfo encodes the turn order of the players. The turn counter is an 
integer that tracks that current player who has a turn. Each playerInfo has a turnPriority that this 
number matches on their turn. It also represents a players index in a states list of playerInfos.

### External Interface:

A Referee manipulating a Game State can access the following functionality:

    - The constructor can be used to construct a game state at any point in a game by giving it a Board and Players.
    - nextTurn: increments turn of the State (used after every move)
    - getTiles: getter for all the tiles on the board at the moment
    - getPenguins: getter for all the penguins on the board at the moment
    - placeAvatar: places an avatar at a given position for the current player
    - getPlayerPositions: getter for all the positions of all the penguins of a given player
    - gameOver: determines if the game is over (no player can move)
    - movePenguin: move a penguin according to a given movement tuple of positions
    - getAllPenguinPositions: getter for all occupied positions on the board
    - getReachableTiles: returns all the tiles that can be moved to from a given tile
    - handleIllegalMove: handles an illegal move
    - allPossibleActions: returns all possible moves for the current player
    - deletePlayer: deletes a cheating player from the game
    - getColorOfPenguinAtPosition: returns the color of the penguin at a given position
    
    
