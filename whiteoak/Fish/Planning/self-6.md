## Self-Evaluation Form for Milestone 6

Indicate below where your TAs can find the following elements in your strategy and/or player-interface modules:

The implementation of the "steady state" phase of a board game
typically calls for several different pieces: playing a *complete
game*, the *start up* phase, playing one *round* of the game, playing a *turn*, 
each with different demands. The design recipe from the prerequisite courses call
for at least three pieces of functionality implemented as separate
functions or methods:

- the functionality for "place all penguins"

https://github.ccs.neu.edu/CS4500-F20/whiteoak/blob/214b82e2425d847ab3de687974a14d56429768e1/Fish/Admin/referee.py#L43-L53

- a unit test for the "place all penguins" funtionality 

https://github.ccs.neu.edu/CS4500-F20/whiteoak/blob/214b82e2425d847ab3de687974a14d56429768e1/Fish/Admin/refereetests.py#L12-L18

- the "loop till final game state"  function

https://github.ccs.neu.edu/CS4500-F20/whiteoak/blob/214b82e2425d847ab3de687974a14d56429768e1/Fish/Admin/referee.py#L57-L72

- this function must initialize the game tree for the players that survived the start-up phase

We do not initialize a game tree because we thought having a game tree wouldn't mak sense when a tree can't have placements and a referee has to handle placements.

- a unit test for the "loop till final game state"  function

https://github.ccs.neu.edu/CS4500-F20/whiteoak/blob/214b82e2425d847ab3de687974a14d56429768e1/Fish/Admin/refereetests.py#L20-L25

- the "one-round loop" function
Do not really haev this kind of "one-round" functionality.
- a unit test for the "one-round loop" function


- the "one-turn" per player function


- a unit test for the "one-turn per player" function with a well-behaved player 


- a unit test for the "one-turn" function with a cheating player


- a unit test for the "one-turn" function with an failing player 


- for documenting which abnormal conditions the referee addresses 

https://github.ccs.neu.edu/CS4500-F20/whiteoak/blob/214b82e2425d847ab3de687974a14d56429768e1/Fish/Admin/referee.py#L17-L21

- the place where the referee re-initializes the game tree when a player is kicked out for cheating and/or failing 

We don't reinitialize because we generate a tree node on demand, so we just mutate our game state which will change whatever node is requested.

**Please use GitHub perma-links to the range of lines in specific
file or a collection of files for each of the above bullet points.**

  WARNING: all perma-links must point to your commit "214b82e2425d847ab3de687974a14d56429768e1".
  Any bad links will be penalized.
  Here is an example link:
    <https://github.ccs.neu.edu/CS4500-F20/whiteoak/tree/214b82e2425d847ab3de687974a14d56429768e1/Fish>

