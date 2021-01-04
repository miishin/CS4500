from unittest import TestCase
from board import Board
from PlayerInfo import PlayerInfo
from Penguin import *
from state import *
import unittest
# from devtools import DevTools


class TestGameState(TestCase):
	def setUp(self) -> None:
		default_board = Board(holes=[])
		removed_board = Board(5, [(1, 1), (0, 0), (0, 1)], 3, 4)
		removed_boardB = Board(5, [(1, 1), (0, 1)], 3, 4)
		removed_boardC = Board(5, [(1, 1)], width=3, height=4)
		square_board7 = Board(3, width=5, height=15)
		tileArrayA = [[0, 1, 2],
		              [3, 4, 5],
		              [0, 1, 2],
		              [3, 4, 5]]
		pOne = PlayerInfo(PenguinColor.red, 0)
		pTwo = PlayerInfo(PenguinColor.black, 1)
		pThree = PlayerInfo(PenguinColor.brown, 2)
		pFour = PlayerInfo(PenguinColor.white, 3)
		allPlayers = [pOne, pTwo, pThree, pFour]
		self.default_gamestate = State(allPlayers, default_board)

	def test_place_avatar(self):
		self.assertEqual([], self.default_gamestate.getAllPenguinPositions())
		self.default_gamestate.placeAvatar((0, 0))
		self.assertEqual([(0, 0)], self.default_gamestate.getAllPenguinPositions())
		self.assertEqual(0, len(self.default_gamestate.players[1].getPenguins()))

		self.default_gamestate.placeAvatar((1, 1))

		expectedPositions = [(0, 0), (1, 1)]
		expectedPositions.sort(key=hash)
		actualPositions = self.default_gamestate.getAllPenguinPositions()
		actualPositions.sort(key=hash)
		self.assertEqual(expectedPositions, actualPositions)
		self.assertEqual(1, len(self.default_gamestate.players[1].getPenguins()))
		self.assertEqual((1, 1), self.default_gamestate.players[1].getPenguins()[0].getPos())

	def test_invalid_placement(self):
		self.assertEqual([], self.default_gamestate.getAllPenguinPositions())
		self.assertTrue(self.default_gamestate.placeAvatar((0,0)))

		self.assertFalse(self.default_gamestate.placeAvatar((5, 5))) # off board

		self.assertEqual([(0,0)],self.default_gamestate.getAllPenguinPositions())
		self.assertEqual(2, self.default_gamestate.turn)

		self.assertFalse(self.default_gamestate.placeAvatar((0,0))) # on existing penguin

		self.assertEqual([(0,0)],self.default_gamestate.getAllPenguinPositions())
		self.assertEqual(3, self.default_gamestate.turn)
		self.default_gamestate.turn = 0
		self.default_gamestate.movePenguin(((0,0), (0,1)))
		self.assertEqual([(0,1)],self.default_gamestate.getAllPenguinPositions())
		self.assertFalse(self.default_gamestate.placeAvatar((0,0))) # Place at hole
		self.assertEqual([(0,1)],self.default_gamestate.getAllPenguinPositions())

	def test_get_player_positions(self):
		self.assertEqual([], self.default_gamestate.getPlayerPositions(0))
		self.default_gamestate.placeAvatar((0, 0))
		self.default_gamestate.placeAvatar((1, 1))
		self.default_gamestate.placeAvatar((2, 2))
		self.default_gamestate.placeAvatar((2, 3))
		self.assertEqual([(0, 0)], self.default_gamestate.getPlayerPositions(0))
		self.default_gamestate.placeAvatar((1, 3))
		expectedPositions = [(0, 0), (1, 3)]
		expectedPositions.sort(key=hash)
		actualPositions = self.default_gamestate.getPlayerPositions(0)
		actualPositions.sort(key=hash)
		self.assertEqual(expectedPositions, actualPositions)

	def test_game_over(self):
		self.default_gamestate.placeAvatar((0, 0))  #red
		self.default_gamestate.placeAvatar((1, 1))  #black
		self.default_gamestate.placeAvatar((2, 2))  #brown
		self.default_gamestate.placeAvatar((2, 3))  #white
		self.assertEqual(False, self.default_gamestate.gameOver())
		self.default_gamestate.movePenguin(((0, 0), (1, 2)))
		self.assertEqual(False, self.default_gamestate.gameOver())
		self.default_gamestate.movePenguin(((1, 1), (2, 0)))
		self.assertEqual(False, self.default_gamestate.gameOver())
		self.default_gamestate.movePenguin(((2, 2), (2, 1)))
		self.assertEqual(False, self.default_gamestate.gameOver())

		# White ran out of moves, skip turn
		self.default_gamestate.nextTurn()
		self.default_gamestate.movePenguin(((1, 2), (1, 3)))
		self.assertEqual(True, self.default_gamestate.gameOver())

	def test_move_penguin(self):
		self.default_gamestate.placeAvatar((0, 0))
		self.default_gamestate.placeAvatar((1, 1))
		self.default_gamestate.placeAvatar((2, 2))
		self.default_gamestate.placeAvatar((2, 3))

		self.assertEqual([(0, 0)], self.default_gamestate.getPlayerPositions(0))
		self.assertEqual(0, self.default_gamestate.players[0].getFish())

		self.default_gamestate.movePenguin(((0, 0), (1, 3)))
		self.assertEqual([(1, 3)], self.default_gamestate.getPlayerPositions(0))
		self.assertEqual(1, self.default_gamestate.players[0].getFish())


	def test_incorrect_movement_wrong_penguin(self):
		# Testing moving another player's penguin
		self.default_gamestate.placeAvatar((0, 0))
		self.default_gamestate.placeAvatar((1, 1))
		self.default_gamestate.placeAvatar((2, 2))
		self.default_gamestate.placeAvatar((2, 3))
		self.assertEqual((1, 1), self.default_gamestate.players[1].getPenguins()[0].getPos())
		self.assertEqual((0, 0), self.default_gamestate.players[0].getPenguins()[0].getPos())
		self.assertEqual(0, self.default_gamestate.turn)
		self.assertFalse(self.default_gamestate.movePenguin(((1, 1), (1, 0))))
		self.assertEqual((1, 1), self.default_gamestate.players[1].getPenguins()[0].getPos())
		self.assertEqual((0, 0), self.default_gamestate.players[0].getPenguins()[0].getPos())
		self.assertEqual(1, self.default_gamestate.turn)

	def test_incorrect_movement_move_to_hole(self):
		# Testing moving another player's penguin
		self.default_gamestate.placeAvatar((0, 0))
		self.default_gamestate.placeAvatar((1, 1))
		self.default_gamestate.placeAvatar((2, 2))
		self.default_gamestate.placeAvatar((2, 3))
		self.assertEqual((1, 1), self.default_gamestate.players[1].getPenguins()[0].getPos())
		self.assertEqual((0, 0), self.default_gamestate.players[0].getPenguins()[0].getPos())
		self.assertEqual(0, self.default_gamestate.turn)

		self.default_gamestate.nextTurn()

		self.assertTrue(self.default_gamestate.movePenguin(((1, 1), (1, 0))))
		self.assertFalse(self.default_gamestate.movePenguin(((2, 2), (1, 1))))

	def test_incorrect_movement_move_off_board(self):
		# Testing moving another player's penguin
		self.default_gamestate.placeAvatar((0, 0))
		self.default_gamestate.placeAvatar((1, 1))
		self.default_gamestate.placeAvatar((2, 2))
		self.default_gamestate.placeAvatar((2, 3))
		self.assertEqual((1, 1), self.default_gamestate.players[1].getPenguins()[0].getPos())
		self.assertEqual((0, 0), self.default_gamestate.players[0].getPenguins()[0].getPos())
		self.assertEqual(0, self.default_gamestate.turn)

		self.assertFalse(self.default_gamestate.movePenguin(((0,0), (2, 4))))

	def test_incorrect_movement_not_straight_line(self):
		# Testing moving another player's penguin
		self.default_gamestate.placeAvatar((0, 0))
		self.default_gamestate.placeAvatar((1, 1))
		self.default_gamestate.placeAvatar((2, 2))
		self.default_gamestate.placeAvatar((2, 3))
		self.assertEqual((1, 1), self.default_gamestate.players[1].getPenguins()[0].getPos())
		self.assertEqual((0, 0), self.default_gamestate.players[0].getPenguins()[0].getPos())
		self.assertEqual(0, self.default_gamestate.turn)

		self.assertFalse(self.default_gamestate.movePenguin(((0,0), (0, 3))))

	def test_incorrect_movement_move_into_player(self):
		# Testing moving another player's penguin
		self.default_gamestate.placeAvatar((0, 0))
		self.default_gamestate.placeAvatar((1, 1))
		self.default_gamestate.placeAvatar((2, 2))
		self.default_gamestate.placeAvatar((0, 1))
		self.assertEqual((1, 1), self.default_gamestate.players[1].getPenguins()[0].getPos())
		self.assertEqual((0, 0), self.default_gamestate.players[0].getPenguins()[0].getPos())
		self.assertEqual(0, self.default_gamestate.turn)

		self.assertFalse(self.default_gamestate.movePenguin(((0,0), (0, 1))))
		self.default_gamestate.turn = 0
		self.assertFalse(self.default_gamestate.movePenguin(((0,0), (1, 2))))

	def test_turn_order_wrapping(self):
		# Tests that the turn following the last player is 0 ( the first players turn )

		self.default_gamestate.placeAvatar((2, 1))
		self.default_gamestate.placeAvatar((2, 0))
		self.default_gamestate.placeAvatar((2, 2))
		self.default_gamestate.placeAvatar((2, 3))

		self.assertEqual(0, self.default_gamestate.turn)# Reds turn
		self.assertEqual([], self.default_gamestate.allPossibleActions())
		self.assertEqual([(2,1), (2,0), (2,2), (2,3)], self.default_gamestate.getAllPenguinPositions())
		self.default_gamestate.nextTurn()
		self.assertEqual([(2,1), (2,0), (2,2), (2,3)], self.default_gamestate.getAllPenguinPositions())
		self.assertEqual(1, self.default_gamestate.turn)
		self.default_gamestate.movePenguin(((2,0), (1,1)))
		self.assertEqual([(2,1), (1,1), (2,2), (2,3)], self.default_gamestate.getAllPenguinPositions())
		self.assertEqual(2, self.default_gamestate.turn)

		self.default_gamestate.movePenguin(((2,2), (1,3)))
		self.assertEqual([(2,1), (1,1), (1,3), (2,3)], self.default_gamestate.getAllPenguinPositions())
		self.assertEqual(3, self.default_gamestate.turn)

		self.assertEqual([], self.default_gamestate.allPossibleActions())
		self.default_gamestate.nextTurn()

		self.assertEqual(0, self.default_gamestate.turn)








	# self.fail()

	def test_get_all_penguin_positions(self):
		self.assertEqual([], self.default_gamestate.getAllPenguinPositions())
		self.default_gamestate.placeAvatar((0, 0))
		self.default_gamestate.placeAvatar((1, 1))
		self.default_gamestate.placeAvatar((2, 2))
		self.default_gamestate.placeAvatar((2, 3))
		expectedPositions = [(0, 0), (1, 1), (2, 2), (2, 3)]
		expectedPositions.sort(key=hash)
		actualPositions = self.default_gamestate.getAllPenguinPositions()
		actualPositions.sort(key=hash)
		self.assertEqual(expectedPositions, actualPositions)

	# self.fail()

	# def test_handle_illegal_move(self):
	# 	self.fail()

	def test_get_reachable_tiles(self):
		self.default_gamestate.placeAvatar((0, 0))
		self.default_gamestate.placeAvatar((1, 1))
		self.default_gamestate.placeAvatar((2, 1))
		self.default_gamestate.placeAvatar((1, 2))

		expected_reachable = [(0, 1), (0, 2)]
		expected_reachable.sort(key=hash)
		reachable = self.default_gamestate.getReachableTiles(0, 0)
		reachable.sort(key=hash)
		self.assertEqual(expected_reachable, reachable)

	if __name__ == '__main__':
		unittest.main()
