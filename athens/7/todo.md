# [x] Data Representation

[x] Refactor to use tuples for positions*

# [x] Functionality

[x] Fix integration tests for 5/

[x] Make sure Game Tree implements turn skipping & game over

[x] Fix signature of movePenguin

[x] Reword purpose/signature of minimax function in strategy.py to explain all possible results

[x] Remove _sortMoves*

# [x] Unittests

[x] Need more unit tests for turn taking in test-gamestate

[x] Need more unit tests for avatar placements in test-gamestate

[x] Need unit test for illegal placement (in strategy.py)

[x] Add a unit test for minimax when no moves are found (strategy.py)

# [x] Design

[x] game-state.md does not specify data representation and external interface separately

[x] game-state.md interface does not mention creating intermediate game states

[x] game-state.md does not mention state of player or the turn order

[x] isValidMove in games.md does not specify whether it checks if a valid move is for the right player (shouldn't be "valid" if it's not their turn)

[x] referee.md does not specify how the turn order is decided (are the players queried for their ages or are player imported with age information included)

[x] referee.md does not specify how players who go idle or timeout are handled
