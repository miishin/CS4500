from Penguin import *
"""
This class contains the construct that represents the information that a game state tracks for each player
participating in a game of fish

A PlayerInfo contains a count of a players score, their color, their turn priority number, and their list of penguins

score is an integer representing the amount of fish a player has collected throughout the game
INTERPRETATION: This value starts at zero for each player and increase with each penguin movement

color is PenguinColor enum that determines the color of a players penguin avatars. This color can identify players.
INTERPRETATION: Each game has up to four players that are uniquely represented by their own color. Uses PenguinColor 

turn priority number indicates what turn in a round of movements/placements belongs to this player
INTERPRETATION: A referee decides turn ordering based off of an external players age

list of Penguins tracks all of a players avatars that are currently on the game board
INTERPRETATION: The referee determines how many Penguins that a players has at the beggining of the game and adds one
				penguins to each players Penguin list for each placement round that takes place. Every player has the same
				amount of penguins at the end of each round, and players should never lose penguins unless they are
				kicked from the game

 
"""
class PlayerInfo:
	def __init__(self, color, turnPriority, fish=0):
		self.fish = fish
		self.color = color
		self.turnPriority = turnPriority
		self.penguins = []

	def getFish(self):
		"""
		Gets the number of fish that a player has collected
		:return: int  the amount of fish a player has
		"""
		return self.fish

	def addFish(self, fish):
		"""
		Increases the amount of fish a player has
		:param fish: int representing how many fish a player just collected
		:return: None. Increases fish field value
		"""
		self.fish += fish

	def getColor(self) -> PenguinColor:
		"""
		Gets the color of the player's Penguins
		:return: PenguinColor
		"""
		return self.color

	def getTurnPriority(self):
		"""
		Gets the priority number of a player
		:return: int  a player's priority number
		"""
		return self.turnPriority

	def getPenguins(self):
		"""
		Gets the list of the player's Penguins
		:return: List of Penguin
		"""
		return self.penguins

	def addPenguin(self, pos):
		"""
		Creates a Penguin with the specified location
		:param x: the x coordinate that a Penguin is placed at
		:param y: the y coordinate that a Penguin is placed at
		:return: None. adds a Penguin to a players Penguin list
		"""
		self.penguins.append(Penguin(self.color, pos))

	def updatePenguin(self, pInd, pos):
		"""
		Moves a Penguin's position
		:param pInd: The index of the Penguin in a players Penguin list
		:param x: The new x coordinate of the Pengiun
		:param y: The new y coordinate of the Penguin
		:return: None. Updates a Penguin in the player's Penguin list
		"""
		self.penguins[pInd] = pos
