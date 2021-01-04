import unittest
from board import Board
from state import State
from PlayerInfo import PlayerInfo
from Penguin import *
from unittest import TestCase

class Test_IntegrationBoardGamesState(TestCase):
	def setUp(self) -> None:
		self.default_board = Board(holes=[])
		self.removed_board = Board(5, [(1, 1), (0, 0), (0, 1)], 3, 4)
		self.removed_boardB = Board(5, [(1, 1), (0, 1)], 3, 4)
		self.removed_boardC = Board(5, [(1, 1)],width=3, height=4)
		self.square_board = Board(3, width=5, height=15)
		pOne = PlayerInfo(PenguinColor.red, 0)
		pTwo = PlayerInfo(PenguinColor.black, 1)
		pThree = PlayerInfo(PenguinColor.brown, 2)
		pFour = PlayerInfo(PenguinColor.white, 3)
		allPlayers = [pOne, pTwo, pThree, pFour]
		self.default_gamestate = State(allPlayers, self.default_board)
		pass
	@staticmethod
	def tilesToFish(tileArray):
		return [[tile.getFish() for tile in row] for row in tileArray]
	def test_getReachableTiles(self):
		# reachable tiles from a Board's perspective
		expected_reachable = [(0, 1), (1, 3), (1, 2), (0, 2)]
		expected_reachable.sort(key=hash)
		reachable = self.default_gamestate.board.getReachableTiles(0, 0)
		reachable.sort(key=hash)
		self.assertEqual(expected_reachable, reachable)

		self.default_gamestate.placeAvatar((0, 0))
		self.default_gamestate.placeAvatar((1, 1))
		self.default_gamestate.placeAvatar((2, 1))
		self.default_gamestate.placeAvatar((1, 2))
		# reachable tiles from a gamestate's perpective. Should exclude paths that avatars block.
		expected_reachable = [(0, 1), (0, 2)]
		expected_reachable.sort(key=hash)
		reachable = self.default_gamestate.getReachableTiles(0, 0)
		reachable.sort(key=hash)
		self.assertEqual(expected_reachable, reachable)

	def test_movePenguinRemoveTiles(self):
		# print(self.tilesToFish(self.default_gamestate.board.getTiles()))

		# The default board should have one fish in every position
		self.assertEqual([[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], self.tilesToFish(self.default_gamestate.board.getTiles()))

		# Placing an avatar should not remove a tile or any fish
		self.default_gamestate.placeAvatar((0, 0))
		self.assertEqual(0, self.default_gamestate.players[0].getFish())
		self.assertEqual((0, 0), self.default_gamestate.players[0].getPenguins()[0].getPos())
		self.assertEqual([[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], self.tilesToFish(self.default_gamestate.board.getTiles()))

		# Moving an avatar should result in a tile being removed from a Board, and a PlayerInfo should gain fish

		# Since we only placed
		self.default_gamestate.nextTurn()
		self.default_gamestate.nextTurn()
		self.default_gamestate.nextTurn()
		self.default_gamestate.movePenguin(((0, 0), (1, 2)))
		self.assertEqual(1, self.default_gamestate.players[0].getFish())
		self.assertEqual((1, 2), self.default_gamestate.players[0].getPenguins()[0].getPos())
		self.assertEqual([[0, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], self.tilesToFish(self.default_gamestate.board.getTiles()))

	if __name__ == '__main__':
		unittest.main()
