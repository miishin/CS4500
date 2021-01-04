## Self-Evaluation Form for Milestone 5

Under each of the following elements below, indicate below where your
TAs can find:

- the data definition, including interpretation, of penguin placements for setups 
    https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/501b081f5e03f55aa1cd27fc8db2eecb480f141c/Fish/Player/strategy.py#L56-L61
    
         This links to our data representation and interpretatoin of a Movement.
         This function is used to place our penguins.
- the data definition, including interpretation, of penguin movements for turns
    
    https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/501b081f5e03f55aa1cd27fc8db2eecb480f141c/Fish/Common/game_tree.py#L14-L16
    
        This links to our data representation and interpretatoin of a Movement.
         This structure is used by the our tree representation and in our minimax implementation
    
- the unit tests for the penguin placement strategy 

     https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/501b081f5e03f55aa1cd27fc8db2eecb480f141c/Fish/Player/test_strategy.py#L87-L113
     
        our penguin placement features a method for getting a placement location, and a method for executing the
        placement. The link includes tests for both methods.

- the unit tests for the penguin movement strategy; 
  given that the exploration depth is a parameter `N`, there should be at least two unit tests for different depths 
  
  https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/501b081f5e03f55aa1cd27fc8db2eecb480f141c/Fish/Player/test_strategy.py#L116-L143
  
        We include tests for our method that decides on which movement to choose (test_minimax) using mutliple values on N.
        We also include our tests for our method that executes the movement
  
  
- any game-tree functionality you had to add to create the `xtest` test harness:
  - where the functionality is defined in `game-tree.PP`
        We did not have to add any functionality to game-tree.py to complete the xtree task.
        
  - where the functionality is used in `xtree`
        We did not have to add any functionality to game-tree.py to complete the xtree task. instead we 
        used the state to place and move penguins in the linked function.
        
        https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/501b081f5e03f55aa1cd27fc8db2eecb480f141c/Fish/Common/xtree.py#L48-L60
        
  - you may wish to submit a `git-diff` for `game-tree` and any auxiliary modules 
  
  
        We did not have to add any funtionality to complete the xtree task, we did however change
        the code in the class to address issues brought up in grading feedback.
        
   https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/501b081f5e03f55aa1cd27fc8db2eecb480f141c/Fish/Common/game_tree.py#L72-L97
   
    The difference is that we now generate all child nodes of a given node at once to more 
    closely resemble a tree structure. This change only affects the how child nodes are created within a node
    and is not seen externally, and so the functionality is not directly called on by xtree

**Please use GitHub perma-links to the range of lines in specific
file or a collection of files for each of the above bullet points.**

  WARNING: all perma-links must point to your commit "501b081f5e03f55aa1cd27fc8db2eecb480f141c".
  Any bad links will result in a zero score for this self-evaluation.
  Here is an example link:
    <https://github.ccs.neu.edu/CS4500-F20/kirvin/tree/501b081f5e03f55aa1cd27fc8db2eecb480f141c/Fish>

