## Self-Evaluation Form for Milestone 5

Under each of the following elements below, indicate below where your
TAs can find:

- the data definition, including interpretation, of penguin placements for setups   
  https://github.ccs.neu.edu/CS4500-F20/whiteoak/blob/0685236e5afa39674b8d74b4bee37301d7f34eac/Player/strategy.py#L18-L29

- the data definition, including interpretation, of penguin movements for turns

  The main function:
  https://github.ccs.neu.edu/CS4500-F20/whiteoak/blob/0685236e5afa39674b8d74b4bee37301d7f34eac/Player/strategy.py#L31-L53
  
  We use 3 subfunction to complete this. They can be found here:
  https://github.ccs.neu.edu/CS4500-F20/whiteoak/blob/0685236e5afa39674b8d74b4bee37301d7f34eac/Player/strategy.py#L55-L111
  
- the unit tests for the penguin placement strategy 
  
  Did not get 100% functionality.
  https://github.ccs.neu.edu/CS4500-F20/whiteoak/blob/2f085c91d2bff48d725976201b13092ad59c2507/Player/strategytests.py#L29-L33
  
- the unit tests for the penguin movement strategy; 
  given that the exploration depth is a parameter `N`, there should be at least two unit tests for different depths 
  
  Depth = 1:
  https://github.ccs.neu.edu/CS4500-F20/whiteoak/blob/2f085c91d2bff48d725976201b13092ad59c2507/Player/strategytests.py#L36-L38
  
  Dept = 2:
  https://github.ccs.neu.edu/CS4500-F20/whiteoak/blob/2f085c91d2bff48d725976201b13092ad59c2507/Player/strategytests.py#L40-L42
  
- any game-tree functionality you had to add to create the `xtest` test harness:
  - where the functionality is defined in `game-tree.PP`
  - where the functionality is used in `xtree`
  - you may wish to submit a `git-diff` for `game-tree` and any auxiliary modules 

No new functionality in game-tree for xtest because xtree was doable with all the info contained in a GameTree object. Any other calculation wouldn't belong within a GameTree object.

**Please use GitHub perma-links to the range of lines in specific
file or a collection of files for each of the above bullet points.**

  WARNING: all perma-links must point to your commit "2f085c91d2bff48d725976201b13092ad59c2507".
  Any bad links will result in a zero score for this self-evaluation.
  Here is an example link:
    <https://github.ccs.neu.edu/CS4500-F20/whiteoak/tree/2f085c91d2bff48d725976201b13092ad59c2507/Fish>

