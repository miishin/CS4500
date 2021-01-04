## Self-Evaluation Form for Milestone 3

Under each of the following elements below, indicate below where your
TAs can find:

- the data description of states, including an interpretation:
        
    Our interpretation of a state can be found in the description of state.py under the Common section of the 
    README, which can be found at kirvin/Fish/README.md. Our implementation of the data representation can be
    found here: https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/4f52eec2b4098084f32b018c956a4e42e871c374/Fish/Common/state.py#L5-L14 

- a signature/purpose statement of functionality that creates states 

    We forgot the purpose statement for the constructor of a state, but the signature can be found here: 
    https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/4f52eec2b4098084f32b018c956a4e42e871c374/Fish/Common/state.py#L6
    it takes in a list of playerInfos and optionally a Board.

- unit tests for functionality of taking a turn 

    Our unit tests for a player moving one of their Penguins can be found here: 
    https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/4f52eec2b4098084f32b018c956a4e42e871c374/Fish/Common/test_GameState.py#L73-L84 
    We first set up a state by placing avatars for each player, then we test a player's Penguin positions
    before and after making a move for their turn.

- unit tests for functionality of placing an avatar

    https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/4f52eec2b4098084f32b018c956a4e42e871c374/Fish/Common/test_GameState.py#L27-L41
    This tests the functionality of the game state to place an avatar by placing an avatar and checking to see
    if the location is added to the list of the player's penguins.  
    
- unit tests for functionality of final-state test

    https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/4f52eec2b4098084f32b018c956a4e42e871c374/Fish/Common/test_GameState.py#L58-L71
    This tests the final state of the game by checking if there are any available moves
    for any of the penguins in the gamestate.

The ideal feedback is a GitHub perma-link to the range of lines in specific
file or a collection of files for each of the above bullet points.

  WARNING: all such links must point to your commit "4f52eec2b4098084f32b018c956a4e42e871c374".
  Any bad links will result in a zero score for this self-evaluation.
  Here is an example link:
    <https://github.ccs.neu.edu/CS4500-F20/kirvin/tree/4f52eec2b4098084f32b018c956a4e42e871c374/Fish>

A lesser alternative is to specify paths to files and, if files are
longer than a laptop screen, positions within files are appropriate
responses.

In either case you may wish to, beneath each snippet of code you
indicate, add a line or two of commentary that explains how you think
the specified code snippets answers the request.

## Partnership Eval 

Select ONE of the following choices by deleting the other two options.

A) My partner and I contributed equally to this assignment. 

If you chose C, please give some further explanation below describing
the state of your partnership and whether and how you have been or are
addressing this disparity. Describe the overall trajectory of your
partnership from the beginning until now. Be honest with your answer
here, and with each other. Even if it's uncomfortable reading this
together right now.

If you chose one of the other two options, you should feel free to
also add some explanation if you wish. 

Our partnership is going well, we are practicing "strong style" pair programming in order to complete assignments.
