import copy
from Tile import Tile, NoTile
from math import floor, ceil

"""
This class contains our implementation of a game board.
INTERPRETATION: a game board is made up of an array of Tiles, or a List of Lists of Tiles, and the
class also contains information about the board's height and width.

The methods of the Board class operate of this Tile array.

The coordinate system used internally by the Board class is based on the x, y coordinate system featured in computer graphics,
where the y coordinate represents the index of a list within the array and increase as you move down a game board,
and the x coordinate represent the index of an element within an inner list of the array.

Specific coordinates of a board are specified by a pos, which a a tuple of (col, row)
INTERPRETATION: the col in a pos represent the column index of the tile being specified, where the first tile starts at index 0
the row is a pos represent the row index that a tile exists in, where the first row is row zero and row indices increase
as rows move downward ( higher row index indicates lower position on a screen for example)
"""

class Board:
	def __init__(self, fish=1, holes=[], width=3, height=4, tiles=None):
		"""
		A board for a game of Fish. Contains and operates on an array of Tiles
		:param width: The amount of tiles in a single row of the game board
		:param height: The amount of tiles in a column of the game board
		:param holes: A list of tuple (col, row) coordinates indicating where empty spaces should be on a board
		:param fish: The amount of fish each game tile should have
		:param tiles: List of List of int an array that contains integer indicating how many fish to give a tile.
		"""
		self.tiles = []
		self.width = width
		self.height = height

		# Used to create a board from an existing tiles array
		if tiles != None:
			maxRowLength = 0
			for row in tiles:
				if len(row) > maxRowLength:
					maxRowLength = len(row)
			for row in tiles:
				tileRow  = []
				for amountOfFish in row:
					if amountOfFish == 0:
						tileRow.append(NoTile())
					elif 0 < amountOfFish <= 5:
						tileRow.append(Tile(amountOfFish))
					else:
						Exception("Invalid amount of fish on a tile")
				for excluded in range(0, maxRowLength  - len(tileRow)):
					tileRow.append(NoTile())
				#TODO: can we assume a tile array given to us in the JSON object will have an equal amount of tiles per row?
				self.tiles.append(tileRow)

		# Creates an array of tiles that make up the board
		# for x in range(0, width):
		else:
			for y in range(0, height):
				row = []
				for x in range(0, width):
				# for y in range(0, height):
					if (x, y) not in holes:
						row.append(Tile(fish))
					else:
						row.append(NoTile())
				self.tiles.append(row)


	def removeTile(self, pos):
		"""
		Replaces a Tile in the board's tile array with a NoTile
		:param pos: the position of the in a board to be removed
		:return:  None. Mutates self.tiles
		"""
		# self.tiles[y][x] = NoTile()
		self.tiles[pos[1]][pos[0]] = NoTile()



	def getReachableTiles(self, col, row, stopTiles=[]):
		"""
		Generates a list with all of the tiles that can be reached via a straight line of a specified tile
		on a hexagonal grid. NoTiles and Tiles beyond NoTiles are not reachable.
		:param col: The row of the tile array that the targeted tile exists in
		:param row: The index of the tile list that the targeted tile exists in
		:param stopTiles: An optional list of (x, y) tuple coordinates of Tiles that are to not be included nor searched past for reachable tiles.
		:return: List of tuple coordinate pairs (x, y), representing the tile positions in the tile array
		"""
		return self.getReachableTilesInATileArray(self.tiles, col,row, stopTiles)

	@staticmethod
	def getReachableTilesInATileArray(tileArray, col, row, stopTiles=[]):
		"""
		Generates a list with all of the tiles that can be reached via a straight line of a specified tile
		on a hexagonal grid. NoTiles and Tiles beyond NoTiles are not reachable. Tile beyond Tiles specified
		in stopTiles are also not reachable
		:param tileArray: A List of List of tiles representing a gameboards tiles
		:param col: The row of the tile array that the targeted tile exists in
		:param row: The index of the tile list that the targeted tile exists in
		:param stopTiles: An optional list of (x, y) tuple coordinates of Tiles that are to not be included nor searched past for reachable tiles.
		:return: List of tuple coordinate pairs (x, y), representing the tile positions in the tile array
		"""
		# Check that the origin, (col, row), is on the board
		width = len(tileArray[0])
		height = len(tileArray)
		if not 0 <= col < width or not 0 <= row < height:
			return []

		positions = []
		for direction in [Board.southWest, Board.northEast, Board.southEast, Board.northWest, Board.north, Board.south]:
			endOfTheLine = False # Indicates whether a search has reached a hole or the end of the board
			i = 1
			while not endOfTheLine:
				nextX, nextY = direction(col, row, i)
				i += 1
				if 0 <= nextX < width and 0 <= nextY < height and (nextX, nextY) not in stopTiles and tileArray[nextY][nextX].getFish() > 0:
					positions.append((nextX, nextY))
				else:
					endOfTheLine = True
		return positions

	@staticmethod
	def northEast(col, row, index):
		"""
		Gives the coordinate of hexagonal point index hexagons away from the point specified by x and y in the northeast direction
		:param col: int the x coordinate of the origin point
		:param row: int the y coordinate of the origin point
		:param index: int the amount of hexagons away the target point is
		:return: tuple (x, y)
		"""
		if row%2 == 0:
			return (col + floor(index / 2), row - index)
		else:
			return (col + ceil(index / 2), row - index)

	@staticmethod
	def southEast(col, row, index):
		"""
		Gives the coordinate of hexagonal point index hexagons away from the point specified by x and y in the southeast direction
		:param col: int the x coordinate of the origin point
		:param row: int the y coordinate of the origin point
		:param index: int the amount of hexagons away the target point is
		:return: tuple (x, y)
		"""
		if row%2 == 0:
			return (col + floor(index / 2), row + index)
		else:
			return (col + ceil(index / 2), row + index)

	@staticmethod
	def northWest(col, row, index):
		"""
		Gives the coordinate of hexagonal point index hexagons away from the point specified by x and y in the northwest direction
		:param col: int the x coordinate of the origin point
		:param row: int the y coordinate of the origin point
		:param index: int the amount of hexagons away the target point is
		:return: tuple (x, y)
		"""
		if row%2 == 0:
			return (col - ceil(index / 2), row - index)
		else:
			return (col - floor(index / 2), row - index)

	@staticmethod
	def southWest(col, row, index):
		"""
		Gives the coordinate of hexagonal point index hexagons away from the point specified by x and y in the southest direction
		:param col: int the x coordinate of the origin point
		:param row: int the y coordinate of the origin point
		:param index: int the amount of hexagons away the target point is
		:return: tuple (x, y)
		"""
		if row%2 == 0:
			return (col - ceil(index / 2), row + index)
		else:
			return (col - floor(index / 2), row + index)

	@staticmethod
	def north(col, row, index):
		"""
		Gives the coordinate of hexagonal point index hexagons away from the point specified by x and y in the north direction
		:param col: int the x coordinate of the origin point
		:param row: int the y coordinate of the origin point
		:param index: int the amount of hexagons away the target point is
		:return: tuple (x, y)
		"""
		return (col, row - index * 2)

	@staticmethod
	def south(col, row, index):
		"""
		Gives the coordinate of hexagonal point index hexagons away from the point specified by x and y in the south direction
		:param col: int the x coordinate of the origin point
		:param row: int the y coordinate of the origin point
		:param index: int the amount of hexagons away the target point is
		:return: tuple (x, y)
		"""
		return (col, row + index * 2)

	def getTiles(self):
		return copy.deepcopy(self.tiles)

	def getTile(self, x, y):
		return copy.deepcopy(self.tiles[y][x])
	
	def copy(self):
		return Board(tiles=self.tiles)



