## Terminology:
- Position is a (x, y) tuple of coordinates

- Move is a ((x,y),(x1,y1)) tuple of Position denoting the starting and ending position of a movement

- Player ID is an integer that identifies a player

## A referee should have the following functionality:
- Setting up a game

- Running the game

- Shutting down the game

- A referee should have a reference to a GameTree object (the game it is managing). 

## Setting up a game contains the following functionality:

- make_board - referee should create an initial board along with holes and fish

- place_avatar - a function that takes in a Position along with a player ID. this should then have the referee place the avatar for that player at that position. Returns true if placed, and false if it was an illegal placement.

- is_game_set_up - a function that returns whether the game has been set up (all penguins placed) as a boolean value.

## Running a game contains the following functionality:

- get_children - a function that will return the possible moves from the current state (to move to next nodes) as a JSON list.

- expand_node - a function that will take in a move and return the game state result of it in JSON format.

- move_avatar - a function that takes in a player ID along with a Move. The referee will check that Move for that player and if it is valid will execute that Move. Returns true if executed, and false if illegal move.

- kick_player - a function that kicks a player that has attempted to cheat. Returns nothing.

## Shutting down a game

- shut_down - a function that shuts down the current game. Should not return anything, but should set it so that any subsequent requests from players are ignored.

- send_results - a function that sends the results of the game to the tournament admin. 

## At any time while game is running.

- get_score - a function that returns the score of the queried Player

- get_game - a function that returns a JSON representation of the current GameState to be passed to the player that requested it

- turn_validation - a Referee should be able to validate that a request (a move or a placement) has been sent from the right player (turn wise). 

- phase_validation - It is also important to not accept placement actions during the real game and movement actions during the placement phase.

- timeout - a Referee should kick players when it is their turn but they have not sent a move for some time
