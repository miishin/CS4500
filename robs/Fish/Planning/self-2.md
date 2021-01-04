## Self-Evaluation Form for Milestone 2

A fundamental guideline of Fundamentals I, II, and OOD is to design
methods and functions systematically, starting with a signature, a
clear purpose statement (possibly illustrated with examples), and
unit tests.

Under each of the following elements below, indicate below where your
TAs can find:


- the data description of tiles, including an interpretation: https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/d54bc98fd915c7d0ec73b6e6c5a7771850b82cc8/Fish/Common/Tile.py#L2-L27
 the data description for tiles is in the Tile.py file in the Common directory of the project. 
 There we go through the one parameter which tile takes in which is fish and the functionality which is to indicate the number of fish it contains.
- the data description of boards, include an interpretation: https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/d54bc98fd915c7d0ec73b6e6c5a7771850b82cc8/Fish/Common/Board.py#L3-L26
        We included a data description of the board with in the game-state.md file. which is located in the kirvin/Planning/system.pdf file.
        In that file we go over the different data pieces which are contained with in our board representation.
        Such as, the nested array of tiles which is representative of all of the tiles in play at the moment,
        the holes array which contain the coordinates of tiles which have been remove, and many others. Linked above is 
        the class Board, and its constructor, describing the data it contains.
- the functionality for removing a tile: https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/d54bc98fd915c7d0ec73b6e6c5a7771850b82cc8/Fish/Common/Board.py#L29-L37
  - purpose: We overlooked the purpose statement for this method as we mistakenly assumed the purpose was straightforward.
  
  - signature: https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/d54bc98fd915c7d0ec73b6e6c5a7771850b82cc8/Fish/Common/Board.py#L32-L34
  
    Here we link to the the parameters names and descriptions the removeTile takes in, as well describing what it does to the Board data.
  
  - unit tests: https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/d54bc98fd915c7d0ec73b6e6c5a7771850b82cc8/Fish/Common/test_Board.py#L14-L26
  
    Here we link to our unit tests for the removeTile. We tested removing several points and checking to make sure
  area removed had no fish in it, since a NoTile contains no fish, and our minimum fish on a Tile is 1.

- the functionality for reaching other tiles on the board: https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/d54bc98fd915c7d0ec73b6e6c5a7771850b82cc8/Fish/Common/Board.py#L39-L85
    
    Here we link to the method in our Board class called getReachableTiles, produces a list of all tiles reachable from 
    a tile at some x, y coordinates.
    
  - purpose: https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/d54bc98fd915c7d0ec73b6e6c5a7771850b82cc8/Fish/Common/Board.py#L41-L42
    
    Here we link to the line where we describe purpose of the getReachableTiles method of the Board class.
  
  - signature: https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/d54bc98fd915c7d0ec73b6e6c5a7771850b82cc8/Fish/Common/Board.py#L43-L45
    
    Here we link to the section where we specify the parameter names and descriptions, as well as what the method returns.
  
  - unit tests: https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/d54bc98fd915c7d0ec73b6e6c5a7771850b82cc8/Fish/Common/test_Board.py#L30-L39
    
    Here we link our set of unit tests that test the functionality of getReachableTiles. We use the unittest library, 
    and the example values for our board states can be found in the setUp method of the same file: https://github.ccs.neu.edu/CS4500-F20/kirvin/blob/d54bc98fd915c7d0ec73b6e6c5a7771850b82cc8/Fish/Common/test_Board.py#L8-L12

The ideal feedback is a GitHub perma-link to the range of lines in specific
file or a collection of files for each of the above bullet points.

  WARNING: all such links must point to your commit "d54bc98fd915c7d0ec73b6e6c5a7771850b82cc8".
  Any bad links will result in a zero score for this self-evaluation.
  Here is an example link:
    <https://github.ccs.neu.edu/CS4500-F20/kirvin/tree/d54bc98fd915c7d0ec73b6e6c5a7771850b82cc8/Fish>

A lesser alternative is to specify paths to files and, if files are
longer than a laptop screen, positions within files are appropriate
responses.

In either case you may wish to, beneath each snippet of code you
indicate, add a line or two of commentary that explains how you think
the specified code snippets answers the request.
