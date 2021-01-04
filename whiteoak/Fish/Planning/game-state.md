Game State:

At the moment our game state is just the board and all of its tiles. However in the future it will include a list of the penguin objects and the player scores. Every bit of necessary information should be contained within these three components. 

The board will be represented as a dictionary where the key is a coordinate tuple (x, y) and the value is a Tile object. Because hexagons do not fit nicely into a normal rectangular coordinate system in a way that fills up every coordinate, we use a dictionary so that we do not have a bunch of empty spaces. Instead we have hexagons at spaced out intervals over a normal grid so that diagonal movements (+x, +y and -x, -y) along with vertical (+-y) and horizontal (+-x) are preserved. 

Someone should be able to take our game state and see:
-The dimensions of the board
-How many fish are on each tile
-Which tiles have been removed
-Where the penguins are located
-Which movements are possible for each penguin
-How many fish each player has eaten (their score)


External Interface:

Ideally an interface with our model is very easy through a bunch of simple functions that allow a referee to access only the data it currently needs rather than a whole dump of information that it will need to sort through. If a referee needs to know if a tile has been removed only that data should be communicated.

