import json
import enum
from state import State
class Request(enum.Enum):
	"""
	A Request identifies the type of message being sent between a referee and users or tournament managers, enabling
	the receiver to handle the message's data properly
	"""
	CreateGame = "CreateGame"
	PlaceAvatar = "PlaceAvatar"
	MoveAvatar = "MoveAvatar"
	UpdateState = "UpdateState"

class RefereeInterface:
	def __init__(self):
		"""
		This RefereeInterface object allows a referee to communicate with players, and a tournament manager in order
		to set up and run games of Fish.
		"""
		pass

	def sendRequest(self, requestDict, destination):
		"""
		Converts a dictionary to a Json Request and sends it to the referee
		:param requestDict: Dict a dictionary containing a Request field, and other relevant information fields
		:param destination: the destination of the message, such as a player, or a tournament manager
		"""
		msg = json.dumps(requestDict)
		#TODO: send data to destination
		pass


	def createGame(self, players, tileArray=None):
		"""
		Sets up a game of fish for a given list of players
		:param players: A list of players participating in a game of fish
		:param tileArray: An array of integers specifying the shape of a game board and
		                    the aomunt of fish for each tile on a board t
		"""
		if tileArray:
			self.gameState = State(players, tileArray)
		else:
			State(players)


	def listenForTournamentManager(self):
		"""
		Listens for the tournament manager to send a list of player
		:return:
		"""
		#TODO: connect to referee and tournament manager
		pass

	def listenForPlayer(self, player):
		"""
		Listens for the player who has the next turn, who is meant to send either a placement or move request
		:return:
		"""
		#TODO: connect referee to player
		pass

	def requestPlaceAvatar(self, player):
		"""
		Sends a request to a player asking them to place a penguin
		:param player: the player who's turn it is to place an avatar
		:return:
		"""
		placeAvatarRequest = {"PlaceAvatart": Request.PlaceAvatar}
		self.sendRequest(placeAvatarRequest, player)

	def requestMoveAvatar(self, player):
		"""
		Sends a request to a player asking them to move an avatar
		:param player: The player whos turn it is to move their penguin
		:return:
		"""
		moveAvatarRequest = {"Request": Request.MoveAvatar}
		self.sendRequest(moveAvatarRequest, player)

	def updateGameState(self, request: dict):
		"""
		Updates the state of the game to reflect a valid movement or placement
		:param request: a dictionary specifying either a movement or placement request, and information about
				how to affect the game state
		:return:
		"""
	def sendGameState(self):
		"""
		Sends the current gamestate to each player in the game
		:return:
		"""
		pass

	def assignPenguinInfo(self, player):
		"""
		Informs a player about their assigned penguin color, turn number,
		 and the amount of penguins they will get to place
		:param player: The player waiting to recieve an assignment of a color and penguins
		:return:
		"""
		pass


	def checkRequest(self, request: dict):
		"""
		Checks an incoming movement or placement request for validity
		Kicks a player in the event of an invalid request
		Updates the game state if the request is valid
		:param request: A dictionary containing information on the type of request, and how to affect a gamestate
		:return:
		"""
		#TODO: convert gamestate to
		pass

	def notifyGameOver(self):
		"""
		Informs all players that the game has ended, and give them info on the statuses of each players final score
		:return:
		"""
		pass

	def gameResults(self):
		"""
		Informs a tournament manager that a game has ended, and information of the winners
		losers, and cheaters of a game
		:return:
		"""
		pass

