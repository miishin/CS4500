## Self-Evaluation Form for Milestone 8

Indicate below where your TAs can find the following elements in your strategy and/or player-interface modules:

1. did you organize the main function/method for the manager around
the 3 parts of its specifications --- point to the main function

The function that runs the whole tournament can be seen:

https://github.ccs.neu.edu/CS4500-F20/robs/blob/2ba483536a021c2f271586b62f7bf883ff161276/Fish/Admin/manager.py#L204-L215

It was split to:

- Notify players of start
- Run all the rounds
- Notify players of end

So the allocation of players and running the games are not separated in this main function, but are in runRound():

https://github.ccs.neu.edu/CS4500-F20/robs/blob/2ba483536a021c2f271586b62f7bf883ff161276/Fish/Admin/manager.py#L193-L202

Where we initialize rounds (allocating players, creating games), run the games, notify the players, and then return the results of the games to the manager.

2. did you factor out a function/method for informing players about
the beginning and the end of the tournament? Does this function catch
players that fail to communicate? --- point to the respective pieces

Informing about the start is:

https://github.ccs.neu.edu/CS4500-F20/robs/blob/2ba483536a021c2f271586b62f7bf883ff161276/Fish/Admin/manager.py#L47-L53

Informing about the end is:

https://github.ccs.neu.edu/CS4500-F20/robs/blob/2ba483536a021c2f271586b62f7bf883ff161276/Fish/Admin/manager.py#L70-L88

We put the functionality to check for failure to communicate in a general "message players" function, this check can be seen:

https://github.ccs.neu.edu/CS4500-F20/robs/blob/2ba483536a021c2f271586b62f7bf883ff161276/Fish/Admin/manager.py#L99

This was so that if we needed to check for a response for the other messages we could do so.

3. did you factor out the main loop for running the (possibly 10s of
thousands of) games until the tournament is over? --- point to this
function.

Yes. The while loop can be seen here:

https://github.ccs.neu.edu/CS4500-F20/robs/blob/2ba483536a021c2f271586b62f7bf883ff161276/Fish/Admin/manager.py#L211

in the main function discussed above. This loop just checks if the tournament is over before running every round and will stop once 
this check returns True.

**Please use GitHub perma-links to the range of lines in specific
file or a collection of files for each of the above bullet points.**


  WARNING: all perma-links must point to your commit "2ba483536a021c2f271586b62f7bf883ff161276".
  Any bad links will be penalized.
  Here is an example link:
    <https://github.ccs.neu.edu/CS4500-F20/robs/tree/2ba483536a021c2f271586b62f7bf883ff161276/Fish>

