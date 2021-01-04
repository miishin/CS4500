from state import State
from board import Board
from Penguin import PenguinColor
from PlayerInfo import PlayerInfo
from game_tree import GameTree
import random
import signal

"""
This file contains the data representation of a Referee that manages a single game of fish.

A Referee contains information pertaining to the state of a game, a Players who are 
participating in the game, and a dict with information about the winners, losers, and cheaters of a game

state:
A State object, which contains the game Board, and information about each players pieces on the board, and scores

list of Players:
INTERPRETATION: A list of Player_Interface objects. Sorted in the order from the object that belongs to 
the youngest player to the object that belongs to the oldest player

Referee-results: {"winners":[...], "Losers":[...], "Cheaters":[...]}
A dictionary with the fields "Winners", "Losers", "Cheaters", where each list contains the game participants
who won, lost, or cheated in the game, respectively. To be used by a tournament manager
"""


def player_interactoin_timeout_lhandler(signum, frame):
	# print('Signal handler called with signal', signum)
	raise OSError("Player took too long to respond")
def try_fn_with_timeout(fn, duration, *args):
	signal.signal(signal.SIGALRM, player_interactoin_timeout_lhandler)
	signal.alarm(duration)
	try:
		result =  fn(*args)
	except OSError:
		#TODO: what should we return if players take too long?
		result = None
	signal.alarm(0)
	return result


class Referee:
	def __init__(self, players, amtRow, amtCol, fish=1, randomize=True, randomSeed=None):
		"""
		Creates a referee with enough players to play a game of fish
		:param players: Player_Interface object that play the game
		:param amtRow: int the amount of rows on a game board
		:param amtCol: int the amount of columns on a game board
		:param fish: int The amount of fish per tile in a non-randomized game
		:param randomize: Boolean whether a game board should have randomized amounts of fish and holes
		:param: randomSeed: int the seed for random number generation.
			By default uses unpredictable seed. refer to pythons Random.seed() documentation for details
		"""
		self.gameResult = {"winners":[], "losers":[], "cheaters":[]}
		holes = []
		if randomize:
			amtTiles = amtRow * amtCol
			amtPlayers = len(players)
			amtPenguins =  (6-amtPlayers)*amtPlayers
			random.seed(randomSeed)
			amtFreeTiles = amtTiles - amtPenguins
			maxHoles =  random.randint(0, amtFreeTiles) // 2
			# We wanted to keep the number of holes down, so there are never more holes than free tiles after placement
			amtHoles = 0
			tileArr = []
			for row in range(amtRow):
				tileArr.append([])
				for col in range(amtCol):
					if amtHoles < maxHoles:
						fishInTile = random.randint(0,5)
					else:
						fishInTile = random.randint(1,5)
					tileArr[-1].append(fishInTile)
			self.board = Board(fish=fish,tiles=tileArr)
		else:
			self.board = Board(fish=fish,holes=holes, width=amtCol, height=amtRow)
		self.players = players
		remainingColors = [color for color in PenguinColor]
		playerInfos = []
		turnPriority = 0
		for player in players:
			playerInfos.append(PlayerInfo(remainingColors[turnPriority], turnPriority))
			turnPriority+=1
		self.state = State( playerInfos, self.board)
		self.tree = None

	def sendGameState(self):
		"""
		Sends a copy of the current game state to each players in a game
		"""
		for player in self.players:
			player.updateGameState(self.state)


	def placementPhase(self):
		"""
		Iteratively asks each player in order of youngest age for a position (row, colummn) to place a penguin at,
		and places a penguin on that players behalf if the position was valid
		Kicks a player if the placement is not valid
		:return:
		"""
		rounds = 6-len(self.players)
		for i in range(0, rounds):
			for player in self.players:
				#TODO: Set timout limit
				placement = player.placeAvatar(self.state)
				if not self.checkValidPlacement(placement):
					self.kickPlayer(self.state.turn)
				self.state.placeAvatar(placement)
		self.tree = GameTree(self.state)

	def checkValidPlacement(self, placement):
		"""
		Checks if a given placement tuple (row, column) is valid for the current state of the game
		:param placement: tuple (row, column) position representing a position on a game board
		:return: Boolean indicating whether a placement is legal
		"""
		s = self.state.copy()
		if not s.placeAvatar(placement):
			return False
		return True

	def runMovementRound(self):
		"""
		Runs one round of the game in the movement phase
		:return: None
		"""
		for player in self.players:
			if not self.state.gameOver():
				#TODO: Set timout limit
				movement = player.moveAvatar(self.state)
				if not movement:
					self.state.nextTurn()
					self.tree = GameTree(self.state)
					continue
				if not self.checkValidMovement(movement):
					self.kickPlayer(self.state.turn)
				else:
					self.state.movePenguin(movement)
					# nextNode = self.tree.applyAction(self.tree.root, movement)
					# self.state = nextNode.getGameState()

	def movePhase(self):
		"""
		Iteratively asks each player in order of youngest age for a Movement ((fromRow, fromColummn), (fromRow, fromColummn))
		to move a penguin, and moves a penguin at the specified from position on the players behalf if the movement iss valid
		Kicks a player if the movement is not valid
		:return:
		"""
		while not self.state.gameOver():
			self.runMovementRound()

	def checkValidMovement(self, move):
		"""
		Checks if a given movement is valid for the given state
		:param move: a Movement
		:return: Boolean indicating if the movement is valid
		"""
		s = self.state.copy() #TODO change referee to use a game tree instead of state
		tree = GameTree(s)
		if move not in tree.root.availableActions:
			return False
		return True

	def determineResults(self):
		"""
		Determines the winners and losers of this finished game
		:return: None, mutates self.gameResult
		"""
		winners = []
		losers = []
		highscore = max([player.getFish() for player in self.state.players])
		for i in range(len(self.players)):
			player_info = self.state.players[i]
			player = self.players[i]
			if player_info.getFish() == highscore:
				winners.append(player.id)
			else:
				losers.append(player.id)
		self.gameResult["winners"] = winners
		self.gameResult["losers"] = losers


	def gameOverPhase(self):
		"""
		Sends the results of the game to each player.
		:return: Referee-results
		"""
		for i in range(0, len(self.players)):
			score = self.state.players[i].getFish()
			# self.players[i].notifyTournamentUpdate()
			self.players[i].endOfGame(score)

	def kickPlayer(self, playerIndex):
		"""
		Removes a player's penguins from a game board, and adds them to a list of kicked players
		:param playerIndex: the position of the player in the Referee's player list
		:return: None, mutates self.gameResult and self.state
		"""
		cheater = self.players[playerIndex]
		self.players = self.players[:playerIndex] + self.players[playerIndex + 1:]
		self.gameResult["cheaters"].append(cheater.id)
		self.state.deletePlayer(self.state.players[playerIndex].getColor())

	def play(self):
		"""
		Main loop of referee, executes the placement, movement, and game over phases'
		:return: Referee-results
		"""
		self.placementPhase()
		self.movePhase()
		self.gameOverPhase()
		self.determineResults()
		return self.gameResult
		# return self.state
		# return self.state
