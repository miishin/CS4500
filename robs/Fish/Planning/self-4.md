## Self-Evaluation Form for Milestone 4

Under each of the following elements below, indicate below where your
TAs can find:

- the interpretation of your data representation for `board`

        Our interpretation for board can be found in our README, which is located at Fish/READEME.md.
        The interpretation for board is under the Common section of the README, in the description for board.py.


- the interpretation of your data representation for `game state`

        Our interpretation for a game state can be found in our README, which is located at Fish/READEME.md.
        The interpretation for a game state is under the Common section of the README, in the description for state.py.


- the publicly visible methods/functions for game trees 

    https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/cf6d232857852d1dfe06f9d024bb8d6409d6acc9/Fish/Common/game_tree.py#L54-L96 
    This link includes the two querying methods, which are named applyAction, and applyFunction. The functionality for 
    creating a compltete game tree given a state is included in the __init__ method.


- the data description of the game tree, including an interpretation;

    https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/cf6d232857852d1dfe06f9d024bb8d6409d6acc9/Fish/Common/game_tree.py#L55-L58
    Our interpretation of a game tree can be found under the method name of the game object constructor. Our implementation of the data 
    representation is a Game is a tree starting with a root GameNode who's state has all Penguins of all Players placed already. this can also be found in the README.md after game_tree.py
    


- a signature/purpose statement of functionality for the first query function

    https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/cf6d232857852d1dfe06f9d024bb8d6409d6acc9/Fish/Common/game_tree.py#L62-L69
    our signature and purpose can be found under the method applyAction() which is linked above

- unit tests for first query functionality

    https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/cf6d232857852d1dfe06f9d024bb8d6409d6acc9/Fish/Common/test_game_tree.py#L54-L78
    
    https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/cf6d232857852d1dfe06f9d024bb8d6409d6acc9/Fish/Common/test_game_tree.py#L147-L180
    the tests linked above will test the first queries ability to pass with a valid move and fail on an invalid move. 
    Also note the query function depends on the getNextState() method which is what the second link shows.
    
**Please use GitHub perma-links to the range of lines in specific
file or a collection of files for each of the above bullet points.**

  WARNING: all perma-links must point to your commit "cf6d232857852d1dfe06f9d024bb8d6409d6acc9".
  Any bad links will result in a zero score for this self-evaluation.
  Here is an example link:
    <https://github.ccs.neu.edu/CS4500-F20/kirvin/tree/cf6d232857852d1dfe06f9d024bb8d6409d6acc9/Fish>

