# whiteoak

# Fish:
- Directory containing files related to Fish

# Fish/Common: 

The files actually implementing the Fish game. 

- board.py - the board implementation

- fish_view.py - the view implementation

- fishexceptions.py - custom exceptions

- game_tree.py - the Game (tree) implementation

- jsoninterpreter.py - utilities for changing JSON into our representations

- penguin.py - the avatar implementation

- fish_player.py - the player implementation

- player_interface.py - the implementation of player interactions with referee to play game

- referee.py - the referee implementation

- state.py - the game state implementation

- tile.py - the tile implementation

- {file}tests.py - the unittests for corresponding file:
    
      boardtests.py: create boards and test
        - Making a board with holes
        - Making a board given holes that are not on the board (should not remove some other tile)
        - Getting the possible moves from a given coordinate
        - Getting the possible moves from a given coordinate where some of the possibilties are occupied (shouldn't count)
        - Making sure that removing a tile changes the possible moves for a tile
        - Testing illegal removals (tiles that don't exist)
        - Testing returning JSON representation of this board
        
      game_tree_tests.py:
        - Tests creating child nodes for a given node
        - Whether those children are correct
        - Tests that illegal moves do not create new nodes
        - Tests functionality to test a state and an action
        - Tests functionality to apply function to all child nodes
        
      statetests.py: create gamestates and test
        - Testing game_over
        - Testing movement leading to game over  
        - Testing getting moves from a given position
        - Testing whether game can start (all penguins placed)
        
      viewtests.py: 
        - Try rendering boards of different sizes
        - Testing getting vertices of a hexagon
        - Testing finding center of a hexagon
        - Testing finding dimensions of a hexagon
 
# Fish/Planning
- Text files documenting design decisions

### games.md
- File describing the design of GameTree

### game-state.md
- File describing the design of GameState

### manager-protocol.md
- File describing the functionality of the Tournament Manager

### player-protocol.md
- File describing how a player can get info from the referee about the game

### referee.md
- File describing the design of a Referee

# Fish/Admin
- Files pertaining to the referee and tournament manager

### referee.py
- The referee implementation

### refereetests.py 
- Unittests for the referee implementation

### manager-interface.py
- Skeleton file describing the functionality of the tournament manager       

# Fish/Player
- Files related to the Player component that actually plays the game

### player.py
- The player implementation, a player contains

### strategy.py
- A strategy implementation that describes how game decisions are made

### strategytests.py
- Unittests for the strategy

# 3/
- Testing component for milestone 3 (the game state)

### Makefile 
- Simply sets files as executable

### Other/ 
- Extraneous files: runxboard runs xboard on all the test cases and signals whether xboard's output matches the output in Tests/

### Tests/ 
- Test files (n-in.json -> n-out.json)

### xboard 
- Test harness that takes in JSON containing a board and a position, returning how many possible moves are possible from that position

# 4/
- Testing component for milestone 4 (the game tree)

### Makefile
- Simply sets files as executables 

### Other/ 
- Extraneous files: runxstate runs xstate on all the test cases and signals whether xstate's output matches the output in Tests/

### Tests/
 - Test files (n-in.json -> n-out.json)

### xstate
- Test harness that takes in a JSON representation of a GameState, runs a move on the first player's first penguin, then returns the new state in JSON format

# 5/
- Testing component for milestone 5 (the strategy)
### Makefile
- Simply sets files as executables

### Other/
- Extraneous files: runxtree runs xtree on all the test cases and signals whether xtree's output matches the output in Tests/

### Tests/
- Test files (n-in.json -> n-out.json)

### xtree
- Test harness that takes in a Move-Response-Query (A JSON object with State, From (position), and To (position)) and returns an action the next player can take to get a penguin to a neighboring tile of the penguin that was just moved

# 6/
- Testing component for milestone 6 (Games!)

### Makefile
- Simply sets files as executables

### Other/
- Extraneous files: runxstrategy runs xstrategy on all the test cases and signals whether xstrategy's output matches the output in Tests/

### Tests/
- Test files (n-in.json -> n-out.json)

### xstrategy
- Test harness that takes in a depth and a GameState and returns the move that the current player should make according to the strategy in strategy.py

# Test-me
All unittests can be run with:

    ./xtest

This will run all the makefiles in each directory then run all the unittests. 

# Terminology

    A Position is a (x, y) coordinate tuple. Also can be read as (row, column).
    
    A Move is a (Position, Position) tuple denoting the source and destination Positions of a movement
    
    Player ID is an integer identifying a player.
    
# Positions

The JSON inputs for the assignment test harnesses use positions as:
    
    [Row, Column]
    
however our code uses

    [Column, Row]

and does not use every single coordinate in that the coordinate (1, 0) for example is not used (it is a gap where there is no hexagon). 

This can be read up on at 

    https://www.redblobgames.com/grids/hexagons/#coordinates-doubled
    
By leaving gaps within a normal 2D grid we can simulate the diagonal nature of hexagon movement.