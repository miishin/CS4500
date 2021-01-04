- Reword purpose/signature of minimax function in strategy.py to explain all possible results

  Added an explanation of how minimax returns None if no movement is found

  fix: https://github.ccs.neu.edu/CS4500-F20/robs/commit/8f47b690398d02242fca79a784a4a89990c6e00b


- Fix integration tests for 5/ by:
  Making sure Game Tree implements turn skipping & game over

  Fixed GameTree to implement turn skipping properly, and this fixed the issues with the integration tests.

  fix: https://github.ccs.neu.edu/CS4500-F20/robs/commit/bc5afeed767e5d0518c987854b3dc303878f1ee2

- Fix signature of movePenguin function

  Changed input from 4 values to just a movement (tuple of positions)

  fix: https://github.ccs.neu.edu/CS4500-F20/robs/commit/bc5afeed767e5d0518c987854b3dc303878f1ee2

- Remove unused function _sortMoves

  Just deleted the function since it isn't used anywhere

  fix: https://github.ccs.neu.edu/CS4500-F20/robs/commit/982959fcdfa38991027e07a15a81bab6d8a769c3

- "insufficient coverage of unit tests for turn taking functionality"

  Added several unit tests for making movements at a state level. Tested moving off board, moving to a hole, moving not in
  a straight line, moving to an occupied tile, moving over another penguin
 
  fix: https://github.ccs.neu.edu/CS4500-F20/robs/commit/09d58282bfd1c254b504af35187e2afc35ef9d64
 
 - Needed more tests for the avatar placement functionality within the State class
 
    Added tests for placing a penguin off the board, in a hole, and in an occupied tile
 
    fix: https://github.ccs.neu.edu/CS4500-F20/robs/commit/952aa4c8a3e1584bc8204442748585a50204ec94
 
- referee.md did not specify how turn order is decided or how idle/timed out players are handled.

  Turn order is decided by the order the players are in when they are given to the referee, and idle players are kicked.

  fix: https://github.ccs.neu.edu/CS4500-F20/robs/commit/c0b33f66dde5b98abf19f51440b13fcec38e0056

- isValidMove in games.md did not specify whether it checks if a move is valid for the current player rather than overall.

  Removed isValidMove specification from games.md because it was not implemented.

  fix: https://github.ccs.neu.edu/CS4500-F20/robs/commit/12e7e5e7d5acfa1adc940d6950274d4643894591

- game-state.md did not separate data representation and the external interface, mention creating intermediate game states, or the turn order

  Separated data and interface, mentioned intermediate game states, added all the new functions that were implemented in state.py, and added info about the turn order

  fix: https://github.ccs.neu.edu/CS4500-F20/robs/commit/cd5ad28b88359ac997c78e86380224719459d6c7

- Did not have a unit test for when penguin placement in strategy.py failed

  Added a unit test for when penguin placement was attempted after all penguins were placed

  fix: https://github.ccs.neu.edu/CS4500-F20/robs/commit/e2a0de36a595f18317c54bb4e74a7142043c758d

- placePenguin in strategy.py did not check if a penguin would fail before attempting it

  made placePenguin return False if the placement was None (no placement possible)

  fix: https://github.ccs.neu.edu/CS4500-F20/robs/commit/92f2f047b21b0ca71e1296be88a03187835d4e70

- Did not have a unit test for when minimax failed to find a move in test-strategy.py

  Added a unit test to check that when a player cannot move minimax returns () (the skip move)

  fix: https://github.ccs.neu.edu/CS4500-F20/robs/commit/f816cd07dc57893dc83b52f4012c7f4355d22970

