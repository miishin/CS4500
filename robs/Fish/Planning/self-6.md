## Self-Evaluation Form for Milestone 6

Indicate below where your TAs can find the following elements in your strategy and/or player-interface modules:

The implementation of the "steady state" phase of a board game
typically calls for several different pieces: playing a *complete
game*, the *start up* phase, playing one *round* of the game, playing a *turn*, 
each with different demands. The design recipe from the prerequisite courses call
for at least three pieces of functionality implemented as separate
functions or methods:

- the functionality for "place all penguins"
        https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/89513b2e00fef5b2a1c0a0cb16f07af6567c8d95/Fish/Admin/referee.py#L53-L67

- a unit test for the "place all penguins" funtionality 
        https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/89513b2e00fef5b2a1c0a0cb16f07af6567c8d95/Fish/Admin/test_referee.py#L89-L91
        
- the "loop till final game state"  function
        https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/89513b2e00fef5b2a1c0a0cb16f07af6567c8d95/Fish/Admin/referee.py#L87
        
- this function must initialize the game tree for the players that survived the start-up phase
        

- a unit test for the "loop till final game state"  function
        https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/89513b2e00fef5b2a1c0a0cb16f07af6567c8d95/Fish/Admin/test_referee.py#L115-L122

- the "one-round loop" function

        Our code loops over turns until there are no turns remaining, but does not separate rounds.
        Our assumption of a game was that players would move their avatars until they all ran out of movements,
        following this assumption, it did not seem necessary to distinguish rounds. Our code below shows where
        turns are divided, and a round technically starts when the youngest player makes a move, but that is
        not visibly marked by anything in the code
https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/89513b2e00fef5b2a1c0a0cb16f07af6567c8d95/Fish/Admin/referee.py#L80-L96
        

- a unit test for the "one-round loop" function


- the "one-turn" per player function

https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/89513b2e00fef5b2a1c0a0cb16f07af6567c8d95/Fish/Admin/referee.py#L88-L96

        Since our movement phase operates on turns rather than rounds as stated in the previously mentioned issue,
        a single turn is handled within each iteration of the main loop of the movement phase function.

- a unit test for the "one-turn per player" function with a well-behaved player 
        https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/89513b2e00fef5b2a1c0a0cb16f07af6567c8d95/Fish/Player/test_player.py#L107-L111

- a unit test for the "one-turn" function with a cheating player


- a unit test for the "one-turn" function with an failing player 


- for documenting which abnormal conditions the referee addresses 

https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/89513b2e00fef5b2a1c0a0cb16f07af6567c8d95/Fish/Admin/referee.py#L57
https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/89513b2e00fef5b2a1c0a0cb16f07af6567c8d95/Fish/Admin/referee.py#L84

- the place where the referee re-initializes the game tree when a player is kicked out for cheating and/or failing 



**Please use GitHub perma-links to the range of lines in specific
file or a collection of files for each of the above bullet points.**

  WARNING: all perma-links must point to your commit "89513b2e00fef5b2a1c0a0cb16f07af6567c8d95".
  Any bad links will be penalized.
  Here is an example link:
    <https://github.ccs.neu.edu/CS4500-F20/kirvin/tree/89513b2e00fef5b2a1c0a0cb16f07af6567c8d95/Fish>

