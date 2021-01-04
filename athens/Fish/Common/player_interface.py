import json
import enum
from Penguin import PenguinColor
from state import State
from enum import Enum

"""
TournamentUpdate:		{ type: TournamentUpdateType , body: String }
INTERPRETATION: Represents a message received from a tournament manager. 
	A Dictionary with fields for the message type and a string message
	type is a TournamentUpdateType enum that informs a player about what kind of information it is receiving.
	body is the actual data being sent to the player in a String format
"""

class TournamentUpdateType(Enum):
	TournamentStart = "TournamentStart"
	RoundWin = "RoundWin"
	RoundLoss = "RoundLoss"
	TournamentWin = "TournamentWin"
	TournamentLoss = "TournamentLoss"

class PlayerInterface:
	"""
	Defines the functionality expected of a Player component.
	Referees create games with a list of these Players that will actually do the actions
	required to play the game (placing penguins, moving penguins).
	"""
	def assignColor(self, color: PenguinColor):
		"""
		Informs a player about their Penguin color on the board
			specified by the  PenguinColor enum
		:param color: PenguinColor enum
		:return: None. Sets the player's color field
		"""
		pass

	def updateGameState(self, state: State):
		"""
		Updates the players information about hte current state of the game
		:return: None.
		"""
		pass

	def placeAvatar(self, state: State):
		"""
		Gets desired placement position on a board as a tuple of (column, row)
		:param state: State the current state of the game
		:return Position (column, row)
		"""
		pass

	def moveAvatar(self, state: State):
		"""
		Gets the desired Movement from a player
		:param state: State the current state of the game
		:return: Movement ( (fromColumn, fromRow), (toColumn, toRow))
		"""
		pass

	def notifyTournamentUpdate(self, msg):
		"""
		Informs a player of information relevant to a tournament.
			messages have the TournamentUpdate format where the message types are specified by TournamentUpdateType enums
		:param msg: TournamentUpdate the message from a tournament manager
		:return: The response to the message
		"""
		pass

