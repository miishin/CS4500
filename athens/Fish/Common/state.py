from board import Board
from Penguin import *
from Tile import *
import copy

"""
This file contains the data representation of a Fish game state. 

A state includes a Board with it's Tile array, a list of playerInfos, and a turn counter.

list of PlayerInfos
INTERPRETATION: The ordering of a list of playerInfos encodes the turn order of the players

turn counter
INTERPRETATION: An integer that tracks that current player who has a turn. Each playerInfo has a turnPriority that this 
				number matches on their turn. It also represents a players index in a states list of playerInfos


The state class contains the methods necessary for a players Penguins to be placed onto or moved on
a board. It also has methods for getting information about the current state of a game, including the
positions of each player's Penguins, the tiles which are reachable from any position, 
the tile array of the gameboard, and whether the game is over.
"""
class State:
	def __init__(self, players, board=None):
		"""
		A state represents the current state of the game, including the current shape of the board, the positions
		of all player penguins, and the scores of all players
		:param players: A list of playerInfos in the order of each players turn priority
		:param board: the current game board being played on
		"""
		if board is None:
			self.board = Board(holes=[])
		else:
			self.board = board

		self.players = players
		self.turn = 0

	def copy(self):
		return copy.deepcopy(self)

	def getTiles(self):
		"""
		Grabs the tile array of the game board
		:return: List of List of Tile
		"""
		return self.board.getTiles()
	def getPenguins(self):
		"""
		Lists all of the penguins in the state
		:return: List of Penguin
		"""
		return [penguin for player in self.players for penguin in player.getPenguins()]

	def placeAvatar(self, pos):
		"""
		Adds a penguin to a player's current list of Penguins with the specified valid position
		:param pos: Tuple (col, row) The position to place the avatar at on a game board
		:return: None. Adds a Penguins to a playerInfo's List of Penguins
		"""
		(x, y) = pos
		player = self.players[self.turn]
		# Checks if postion is on board, and if position has hole
		if 0 <= x < len(self.board.getTiles()[0]) and 0 <= y < len(self.board.getTiles())  and self.board.getTiles()[y][x].getFish() == 0:
			return self.handleIllegalMove()
		if not (0 <= x < len(self.board.getTiles()[0]) or 0 <= y < len(self.board.getTiles())):
			return self.handleIllegalMove()
		for otherPlayer in self.players:
			for peng in otherPlayer.getPenguins():
				if (x, y) == peng.getPos():
					return self.handleIllegalMove()
		player.addPenguin((x, y))
		self.nextTurn()
		return True

	def nextTurn(self):
		turn = (self.turn + 1) % len(self.players)
		self.turn = turn

	def getPlayerPositions(self, playerIndex):
		"""
		Lists all of the (x, y) positions of a player's Penguin's
		:param playerIndex: The priority number of a player
		:return: List of Tuple (x, y)
		"""
		penguinPositions = [penguin.getPos() for penguin in self.players[playerIndex].getPenguins()]
		return penguinPositions


	def gameOver(self):
		"""
		Determines whether there are no more available moves on the board
		:return: Boolean. Whether any players have any available moves
		"""
		for player in self.players:
			for penguin in player.getPenguins():
				if len(self.board.getReachableTiles(penguin.getPos()[0], penguin.getPos()[1], self.getAllPenguinPositions())) != 0:
					return False
		return True

	def movePenguin(self, movement):
		"""
		Changes a Penguin's location to a specified position if the move is valid
		If a player makes an invalid move, their turn is discarded
		The turn coutner is incremented regardless of whether a movement was valid or not
		:param movement: tuple of (x, y) tuples
		:return: Boolean. Whether a movement was executed. Changes a Pengiun's posx and posy
		"""
		# player = self.players[playerInd]

		player = self.players[self.turn]
		self.nextTurn()
		if movement == ():
			return True

		(x, y) = movement[1]

		penguinIndex = -1
		for peng in player.getPenguins():
			penguinIndex += 1
			if peng.getPos() == movement[0]:
				break

		penguinCurrentPosition =  player.getPenguins()[penguinIndex].getPos()
		if (x, y) not in self.board.getReachableTiles(penguinCurrentPosition[0], penguinCurrentPosition[1], self.getAllPenguinPositions()): #TODO: add optional penguin position argument to reachable tiles
			return self.handleIllegalMove()
		elif (x, y) in self.getAllPenguinPositions():
			return self.handleIllegalMove()
		else:
			player.getPenguins()[penguinIndex].setPos((x, y))
			player.addFish(self.board.getTile(penguinCurrentPosition[0], penguinCurrentPosition[1]).getFish())
			self.board.removeTile((penguinCurrentPosition[0], penguinCurrentPosition[1]))
			return True

	def getAllPenguinPositions(self):
		"""
		Gets a list of (x, y) positions belonging to all Penguins in the current game state
		:return: List of Tuple (x, y)
		"""
		penguinPositions = [penguin.getPos() for player in self.players for penguin in player.getPenguins()]
		return penguinPositions


	def getReachableTiles(self, col, row):
		"""
		Generates a list with all of the tiles that can be reached via a straight line of a specified tile
		on a hexagonal grid. NoTiles and Tiles beyond NoTiles are not reachable.
		:param col: The row of the tile array that the targeted tile exists in
		:param row: The index of the tile list that the targeted tile exists in
		:param stopTiles: An optional list of (x, y) tuple coordinates of Tiles that are to not be included nor searched past for reachable tiles.
		:return: List of tuple coordinate pairs (x, y), representing the tile positions in the tile array
		"""
		return self.board.getReachableTiles(col,row, stopTiles=self.getAllPenguinPositions())



	def handleIllegalMove(self):
		"""
		Discards the players turn.
		:return:
		"""
		return False

	def movePenguinNewState(self, playerInd, fromx, fromy, x, y):
		"""
		creates a new state as if a move took place
		:param playerInd: The priority number of a player
		:param fromx: The initial x coordinate of the Penguin
		:param fromy: The initial y coordinate of the Penguin
		:param x: The x coordinate to move the Penguin to
		:param y: The y coordinate to move the Penguin to
		:return: None. Changes a Pengiun's posx and posy
		"""

		turn = (self.turn + 1) % len(self.players)

		player = self.players[playerInd]
		penguinIndex = -1
		for peng in player.getPenguins():
			penguinIndex += 1
			if peng.getPos() == (fromx, fromy):
				break


		penguinCurrentPosition =  player.getPenguins()[penguinIndex].getPos()
		if (x, y) not in self.board.getReachableTiles(penguinCurrentPosition[0], penguinCurrentPosition[1], self.getAllPenguinPositions()): #TODO: add optional penguin position argument to reachable tiles
			return self.handleIllegalMove()
		elif (x, y) in self.getAllPenguinPositions():
			return self.handleIllegalMove()
		else:
			player.getPenguins()[penguinIndex].setPos((x, y))
			player.addFish(self.board.getTile(penguinCurrentPosition[0], penguinCurrentPosition[1]).getFish())
			self.board.removeTile((penguinCurrentPosition[0], penguinCurrentPosition[1]))

	def getColorOfPenguinAtPosition(self, pos):
		"""
		Gets the color of the penguin that exists at a specified position, gives false if no penguin exists
		:param x: The x coordinate of the tile
		:param y: The y coordinate of the tile
		:return: PencuinColor an enum indicating the color of the penguin that exists at a certain tile poisition
					False if no penguin exists at the position
		"""
		for player in self.players:
			for penguin in player.getPenguins():
				if penguin.getPos() == pos:
					return penguin.getColor()
		return False

	def deletePlayer(self, playerIndex):
		"""
		Removes all of the penguins of the player who is assigned the given PenguinColor
		:param playerIndex: The index of the player to kick
		:return: None
		"""
		for player in self.players[playerIndex + 1:]:
			player.turnPriority -= 1
			#TODO Check if turnpriority is still necessary
		self.players = self.players[:playerIndex] + self.players[playerIndex+1:]




	def allPossibleActions(self):
		"""
		Gets all possible actions for the player who has the current turn
		:return: List of movements
		"""
		possibleActions = []
		for penguin in self.players[self.turn].getPenguins():
			for reachable in self.getReachableTiles(penguin.getPos()[0], penguin.getPos()[1]):
				possibleActions.append((penguin.getPos(), reachable))
		return possibleActions




