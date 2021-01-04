import json
import enum
from Penguin import PenguinColor
from state import State
from referee import Referee

class Manager_Interface:
	# 	"""
	# 	This ManagerInterface object allows a manager to create a game, assemble lists of players from the queue, sort player lists, and recieve Json request needed to
	# 	communicate with the referee
	# 	:param age: int the age of the player
	# 	:param name: string the name of the player
	# 	"""

	def getPlayers(self):
		"""
		Gets the players from the queue of potential players
		:returns list: list of players sorted by age
		"""
		pass

	def ageSort(self, playerList):
		"""
		helper method for the get player method
		:param playerList: list of players taken from the queue of potential players
		:return: playerlist that has been sorted on there age parameter
		"""
		pass

	def createRef(self, players, amtRow, amtCol):
		"""
		Creates the referees which will then create the game
		:param Players: list of players
		:param amtRow: rows of the game board
		:param amtCol: collumns of the game board
		:return Ref: Referee object
		"""
		pass

	def runTournament(self):
		"""
		Main method for the tournument manager which starts the game
		:return List of List of Dict where each inner list represents a round of the tournament, and each Dict
			represents the results from a single game of Fish
		"""
		pass

	def getRoundResults(self):
		"""
		runs getResults on the referees of each game in the round and sets up the next round if applicable
		:return nextRound: next round or False
		"""
		pass

	def getResults(self, ref: Referee):
		"""
		gets the results of the game from the referee of the game and adds
		:return : Referee-results info
		"""
		pass


