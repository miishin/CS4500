## Self-Evaluation Form for Milestone 7

Please respond to the following items with

1. the item in your `todo` file that addresses the points below.
    It is possible that you had "perfect" data definitions/interpretations
    (purpose statement, unit tests, etc) and/or responded to feedback in a 
    timely manner. In that case, explain why you didn't have to add this to
    your `todo` list.

2. a link to a git commit (or set of commits) and/or git diffs the resolve
   bugs/implement rewrites: 

These questions are taken from the rubric and represent some of the most
critical elements of the project, though by no means all of them.

(No, not even your sw arch. delivers perfect code.)

### Board

- a data definition and an interpretation for the game _board_

This was done in response to previous feedback.

Can be found at https://github.ccs.neu.edu/CS4500-F20/robs/blob/a54e95240e1c21fc1a5e2250fb1eada2a1884374/Fish/Common/board.py#L9-L21

Commit: https://github.ccs.neu.edu/CS4500-F20/robs/commit/0e9d1ed4ce44865fb284b1217a5be626a04d2c95#diff-a2e5e9a5574dc815c4a99949d621cf78

- a purpose statement for the "reachable tiles" functionality on the board representation

This was already added before:

Can be found at https://github.ccs.neu.edu/CS4500-F20/robs/blob/a54e95240e1c21fc1a5e2250fb1eada2a1884374/Fish/Common/board.py#L85-L90

Commit: https://github.ccs.neu.edu/CS4500-F20/robs/commit/425e0b2ed8ff5bab6f5f8a8329b47ba478f47d40#diff-a2e5e9a5574dc815c4a99949d621cf78

- two unit tests for the "reachable tiles" functionality

There was already unit testing for this:

Can be found at: https://github.ccs.neu.edu/CS4500-F20/robs/blob/a54e95240e1c21fc1a5e2250fb1eada2a1884374/Fish/Common/test_Board.py#L50

First commit: https://github.ccs.neu.edu/CS4500-F20/robs/commit/9cb5151424a40f17588fb72da5eaa23b35e6dd49#diff-15ec32380b0c14eae0c025df08a3121a 

### Game States 


- a data definition and an interpretation for the game _state_

This was already included before the todo assignment.

Can be found at: https://github.ccs.neu.edu/CS4500-F20/robs/blob/a54e95240e1c21fc1a5e2250fb1eada2a1884374/Fish/Common/state.py#L7-L22

Commit: https://github.ccs.neu.edu/CS4500-F20/robs/commit/0e9d1ed4ce44865fb284b1217a5be626a04d2c95#diff-3c0c742881289081d1c3cfb361c6da0e

- a purpose statement for the "take turn" functionality on states

There was a purpose statement before, but the turn taking aspect was clarified in Milestone 7.

It was an item on our todo list:

[x] Fix signature of movePenguin

Commit: https://github.ccs.neu.edu/CS4500-F20/robs/commit/09d58282bfd1c254b504af35187e2afc35ef9d64

- two unit tests for the "take turn" functionality 

[x] Need more unit tests for turn taking in test-gamestate (Line 19 in todo.md)

https://github.ccs.neu.edu/CS4500-F20/robs/commit/09d58282bfd1c254b504af35187e2afc35ef9d64

### Trees and Strategies


- a data definition including an interpretation for _tree_ that represent entire games

This was addressed before Milestone 7

Can be found at: https://github.ccs.neu.edu/CS4500-F20/robs/blob/a45d6ef83ed5398d144690f88e58f3c6921f7768/Fish/Common/game_tree.py#L6-L25

Commit: https://github.ccs.neu.edu/CS4500-F20/robs/commit/0e9d1ed4ce44865fb284b1217a5be626a04d2c95#diff-a2b85550c39cc14472cf741196ccb390

- a purpose statement for the "maximin strategy" functionality on trees

The strategy component already had a purpose statement.
  
Can be found at: https://github.ccs.neu.edu/CS4500-F20/robs/blob/9ba2588f8ac24323979fbc8569257f820c9956a7/Fish/Player/strategy.py#L51-L55

Commit: https://github.ccs.neu.edu/CS4500-F20/robs/commit/8d1ba6588020070cd2b659e5b41e8b3e200451b4#diff-8668b6307021688899b1d56141354730

- two unit tests for the "maximin" functionality 

Did not have a unit test for when minimax failed to find a move in test-strategy.py (Line 25 in todo.md)

https://github.ccs.neu.edu/CS4500-F20/robs/commit/f816cd07dc57893dc83b52f4012c7f4355d22970

### General Issues

Point to at least two of the following three points of remediation: 


- the replacement of `null` for the representation of holes with an actual representation 

From the beginning None was not used for holes.

Can be seen: https://github.ccs.neu.edu/CS4500-F20/robs/blob/ea10b88ea5fd0174d2b7fbeb3af23ac12c4e7aae/Fish/Common/Tile.py#L22-L33

Commit: https://github.ccs.neu.edu/CS4500-F20/robs/commit/9e3543010dc8a5d1f04683c7c6aec3a9b14f12d5#diff-9ec3aaa69902115ef6ec7c01da1f8a7a

- one name refactoring that replaces a misleading name with a self-explanatory name


- a "debugging session" starting from a failed integration test:
  - the failed integration test
  
    3-in.json for xstrategy
    
  - its translation into a unit test (or several unit tests)
  
    Same issue was causing an issue in a unit test (https://github.ccs.neu.edu/CS4500-F20/robs/blob/9ba2588f8ac24323979fbc8569257f820c9956a7/Fish/Player/test_strategy.py#L167)
  
  - its fix
  
    The fix was changing a <= to a <, this was making the algorithm go one level too shallow while searching for a move.
    
    https://github.ccs.neu.edu/CS4500-F20/robs/commit/f7bad00887f7c792e2672cc7236da466ef729eab#diff-8668b6307021688899b1d56141354730
    
  - bonus: deriving additional unit tests from the initial ones 


### Bonus

Explain your favorite "debt removal" action via a paragraph with
supporting evidence (i.e. citations to git commit links, todo, `bug.md`
and/or `reworked.md`).

We had failed to address what should happen in a game tree when a player cannot move but the game is not over. 
The game would end when a player could not move without checking if other players could. We needed an action to get 
from one node to another, but did not have one explicitly for skipping. A empty move (empty tuple) was implemented so that 
a node will always have one child signifying a turn skip as long as the game is not over. 

The todo item was:

[x] Make sure Game Tree implements turn skipping & game over

The fix can be seen: https://github.ccs.neu.edu/CS4500-F20/robs/commit/bc5afeed767e5d0518c987854b3dc303878f1ee2

