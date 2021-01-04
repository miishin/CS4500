- The minimax cut off search early by one turn.

  failing integration tests for milestone 6 https://github.ccs.neu.edu/CS4500-F20/robs/commit/ef567bc11d9ef0175e05713c70ea0ec8f5f596bc

  fix: https://github.ccs.neu.edu/CS4500-F20/robs/commit/f7bad00887f7c792e2672cc7236da466ef729eab

- Place avatar didn't check for placement off board, or handle checking for placing on an occupied tile correctly

  https://github.ccs.neu.edu/CS4500-F20/robs/commit/09d58282bfd1c254b504af35187e2afc35ef9d64

  fix: https://github.ccs.neu.edu/CS4500-F20/robs/commit/952aa4c8a3e1584bc8204442748585a50204ec94
 
- Unit test for minimax when player cannot move failed because we sort the moves, but sorting the list of empty move [()] caused errors

  unit test can be seen: https://github.ccs.neu.edu/CS4500-F20/robs/commit/f816cd07dc57893dc83b52f4012c7f4355d22970

  fix: https://github.ccs.neu.edu/CS4500-F20/robs/commit/b4f7634022bd7623cacaf341d80f77cb3b1b9095#diff-8668b6307021688899b1d56141354730
