"""
This file contains the data representation for Tiles, which are the hexaagonal units that make up a game Board
Each tile contains an amount of fish.
INTERPRETATION: The amount of fish is an integer between 1 and 5 for any valid Tile, and 0 for NoTiles
"""
class Tile:

	def __init__(self, fish):
		"""
		Represents a valid tile on a game board that contains at least one fish, but no more than five fish.
		:param fish: An integer value representing the amount of fish a tile has.
		"""
		self.fish = fish

	def getFish(self):
		"""
		Gets the amount of fish held by a tile
		:return:  The amount of fish that this tile contains
		"""
		return self.fish

class NoTile:
	"""
	This class represnts an empty space on a game board where a tile once was or could have been
	"""
	def __init__(self):
		pass
	def getFish(self):
		"""
		A NoTile contains no fish, as it represents empty space.
		:return: 0
		"""
		return 0