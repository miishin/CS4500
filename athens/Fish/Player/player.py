from player_interface import PlayerInterface
from Penguin import PenguinColor
from state import State
from strategy import Strategy
from game_tree import GameTree


class Player(PlayerInterface):
	def __init__(self, age, id, depth=1):
		self.age = age
		self.id = id
		self.depth = depth

	def assignColor(self, color: PenguinColor):
		self.color = color

	def updateGameState(self, state: State):
		self.gameState = state

	def placeAvatar(self, state: State):
		return Strategy.getAvailablePlacement(state)

	def moveAvatar(self, state: State):
		# A game board has a maximum of 25 tiles, there are a minimum of 5
		# penguins in any game, and a maximum of 20 moves in a game
		# which means minimax would never have to exceed a depth of 20
		# to explore an entire game
		return Strategy.minimax(GameTree(state), self.depth)

	def notifyTournamentUpdate(self, msg):
		return msg

