from unittest import TestCase
import unittest
import board
from board import Board
from Tile import *

class TestBoard(TestCase):

	def setUp(self):
		# def setUp(self) -> None:
		self.default_board = Board(holes=[])
		self.removed_board = Board(5, [(1, 1), (0, 0), (0, 1)], 3, 4)
		self.removed_boardB = Board(5, [(1, 1), (0, 1)], 3, 4)
		self.removed_boardC = Board(5, [(1, 1)],width=3, height=4)
		self.square_board7 = Board(3, holes=[], width=5, height=15)
		self.tileArrayA = [[0, 1, 2],
		                   [3, 4, 5],
		                   [0, 1, 2],
		                   [3, 4, 5]]


	@staticmethod
	def tilesToFish(tileArray):
		return [[tile.getFish() for tile in row] for row in tileArray]

	def test_remove_tile(self):
		# [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
		# (1, 2)
		#
		# 3 width, 4 height
		# [[1,1,1],
		#  [1,1,1],
		#  [1,1,1],
		#  [1,1,1]]
		self.assertEqual([tile.getFish() for row in self.default_board.tiles for tile in row],
		                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
		self.default_board.removeTile((0, 0))
		self.assertEqual([tile.getFish() for row in self.default_board.tiles for tile in row],
		                 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
		self.default_board.removeTile((2, 2))
		self.assertEqual([tile.getFish() for row in self.default_board.tiles for tile in row],
		                 [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1])
		self.default_board.removeTile((2, 2))  # TODO: what should happen if we try to remove a non existant tile?
		self.assertEqual([tile.getFish() for row in self.default_board.tiles for tile in row],
		                 [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1])
		self.default_board.removeTile((1, 2))
		self.assertEqual([tile.getFish() for row in self.default_board.tiles for tile in row],
		                 [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1])

	def test_get_reachable_tiles(self):
		expected_reachable = [(0, 1), (1, 3), (1, 2), (0, 2)]
		expected_reachable.sort(key=hash)
		reachable = self.default_board.getReachableTiles(0, 0)
		reachable.sort(key=hash)
		self.assertEqual(expected_reachable, reachable)

		expected_reachable = [(0, 3), (1, 1), (2, 0), (0, 1), (0, 0), (1, 3), (1, 0)]
		expected_reachable.sort(key=hash)
		reachable = self.default_board.getReachableTiles(1, 2)
		reachable.sort(key=hash)
		self.assertEqual(expected_reachable, reachable)

		self.assertEqual([], self.default_board.getReachableTiles(-2, 5))

		self.assertEqual([(0, 3)], self.removed_board.getReachableTiles(0, 2))

		self.assertEqual([(0, 2)], self.removed_boardB.getReachableTiles(0, 0))

		self.removed_boardB.removeTile((0, 2))
		self.assertEqual([], self.removed_boardB.getReachableTiles(0, 0))

		self.removed_boardC.removeTile((0, 2))

		expected_reachable = [(0, 1), (1, 3), (1, 2)]
		expected_reachable.sort(key=hash)
		reachable = self.removed_boardC.getReachableTiles(0, 0)
		reachable.sort(key=hash)
		self.assertEqual(expected_reachable, reachable)

		expected_reachable = [(0, 0), (0, 2), (0, 3), (1, 2), (1, 3), (1, 0)]
		expected_reachable.sort(key=hash)
		reachable = self.default_board.getReachableTiles(0, 1)
		reachable.sort(key=hash)
		self.assertEqual(expected_reachable, reachable)

		expected_reachable = [(2, 6), (1, 5), (2, 8), (1, 9), (3, 6), (3, 8), (2, 5), (2, 9), (1, 4), (0, 3), (0, 2),
		                      (3, 5), (4, 4), (4, 3),
		                      (0, 11), (0, 12), (3, 9), (4, 10), (4, 11), (2, 13), (2, 11), (2, 3), (2, 1), (1, 10)]
		expected_reachable.sort(key=hash)
		reachable = self.square_board7.getReachableTiles(2, 7)
		reachable.sort(key=hash)
		self.assertEqual(expected_reachable, reachable)

		self.square_board7.removeTile((1, 3))
		self.square_board7.removeTile((1, 4))
		self.square_board7.removeTile((3, 9))
		self.square_board7.removeTile((3, 10))
		self.square_board7.removeTile((3, 5))
		self.square_board7.removeTile((1, 10))
		self.square_board7.removeTile((2, 3))
		self.square_board7.removeTile((2, 11))
		expected_reachable = [(2, 6), (1, 5), (2, 8), (1, 9), (3, 6), (3, 8), (2, 5), (2, 9)]
		expected_reachable.sort(key=hash)
		reachable = self.square_board7.getReachableTiles(2, 7)
		reachable.sort(key=hash)
		self.assertEqual(expected_reachable, reachable)

	def test_Directions(self):
		self.assertEqual((0, -1), Board.northEast(0, 0, 1))
		self.assertEqual((0, 1), Board.southEast(0, 0, 1))
		self.assertEqual((-1, 1), Board.southWest(0, 0, 1))
		self.assertEqual((-1, -1), Board.northWest(0, 0, 1))

		self.assertEqual((1, 0), Board.northEast(0, 1, 1))
		self.assertEqual((1, 2), Board.southEast(0, 1, 1))
		self.assertEqual((0, 2), Board.southWest(0, 1, 1))
		self.assertEqual((0, 0), Board.northWest(0, 1, 1))

		self.assertEqual((1, -2), Board.northEast(0, 0, 2))
		self.assertEqual((1, 2), Board.southEast(0, 0, 2))
		self.assertEqual((-1, 2), Board.southWest(0, 0, 2))
		self.assertEqual((-1, -2), Board.northWest(0, 0, 2))

	if __name__ == '__main__':
		unittest.main()
