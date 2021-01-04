from unittest import TestCase
from board import Board
from state import State
from PlayerInfo import PlayerInfo
from Penguin import PenguinColor
from strategy import Strategy
from game_tree import GameTree
from devtools import DevTools


class Teststrategy(TestCase):
	def setUp(self) -> None:
		# for testing minimax
		tileArr1 = [
			[1, 1, 2],
			[3, 4, 5],
			[0, 1, 2],
			[3, 4, 5]]
		board1 = Board(tiles=tileArr1)
		players10 = PlayerInfo(PenguinColor.white, 0)
		players11 = PlayerInfo(PenguinColor.red, 1)
		playersGS1 = [players10, players11]
		gameState1 = State(playersGS1, board1)
		gameState1.placeAvatar((0, 0))
		gameState1.placeAvatar((2, 0))
		gameState1.placeAvatar((1, 1))
		gameState1.placeAvatar((2, 2))
		gameState1.placeAvatar((2, 3))
		gameState1.placeAvatar((1, 0))
		gameState1.placeAvatar((1, 3))
		gameState1.placeAvatar((2, 1))
		self.gs1 = gameState1
		self.gt1 = GameTree(gameState1)

		tileArr2 = [[1,2,3],[5,4],[1,0,3],[0,4],[1,2,3],[5,4],[1,2,0],[5,4],[1,0,3]]
		board2 = Board(tiles=tileArr2)

		player20 = PlayerInfo(PenguinColor.white, 0)
		player21 = PlayerInfo(PenguinColor.red, 1)
		player22 = PlayerInfo(PenguinColor.black, 2)
		player23 = PlayerInfo(PenguinColor.brown, 3)
		playersGS2 = [player20, player21, player22, player23]
		gameState2 = State(playersGS2, board2)
		gameState2.placeAvatar((0, 0))
		gameState2.placeAvatar((2, 0))
		gameState2.placeAvatar((1, 4))
		gameState2.placeAvatar((0, 8))
		gameState2.placeAvatar((1, 1))
		gameState2.placeAvatar((2, 2))
		gameState2.placeAvatar((0, 6))
		gameState2.placeAvatar((1, 7))
		self.gs2 = gameState2
		self.gt2 = GameTree(gameState2)

		# Very small state for
		tileArrMini0 = [ [5,0],[1,5], [1,2], [1, 1]]
		boardMini0 = Board(tiles=tileArrMini0)
		playerMini00 = PlayerInfo(PenguinColor.black, 0)
		playerMini01 = PlayerInfo(PenguinColor.red, 1)
		gameStateMini0  = State([playerMini00, playerMini01], boardMini0)
		gameStateMini0.placeAvatar((0, 2))
		gameStateMini0.placeAvatar((1, 2))
		self.gsMini0 = gameStateMini0
		self.gtMini0 = GameTree(gameStateMini0)

		# For testing the placement strategy
		board3 = Board(tiles=tileArr2)
		playerE0 = PlayerInfo(PenguinColor.white, 0)
		playerE1 = PlayerInfo(PenguinColor.red, 1)
		playerE2 = PlayerInfo(PenguinColor.black, 2)
		playerE3 = PlayerInfo(PenguinColor.brown, 3)
		playersGS3 = [playerE0, playerE1, playerE2, playerE3]
		gameStateEmpty1 = State(playersGS3, board3)
		self.gse = gameStateEmpty1

		# For testing the placement strategy
		tileArr3 = [[0,1,1], [1,0,1], [0,0,1], [1,0,1],[0,1,0]]
		board4 = Board(tiles=tileArr3)
		playerE10 = PlayerInfo(PenguinColor.white, 0)
		playerE11 = PlayerInfo(PenguinColor.red, 1)
		playerE12 = PlayerInfo(PenguinColor.black, 2)
		playersGSE1 = [playerE10, playerE11, playerE12]
		gameStateEmpty1 = State(playersGSE1, board4)
		self.gse1 = gameStateEmpty1

		# For testing Movement tie breaking
		tileArr4 = [[1,1,1,1],[1,1,1],[1,1,1,1],[1,1,1],[1,1,1,1]]
		board5 = Board(tiles=tileArr4)
		playerTB0 = PlayerInfo(PenguinColor.black, 0)
		playerTB1 = PlayerInfo(PenguinColor.red, 1)
		playersTB = [playerTB0, playerTB1]
		self.gsTB = State(playersTB, board5)
		# self.gtTB = GameTree(gameStateTieBreakTest)

		flatArr = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
				   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
		flatBoard = Board(tiles=flatArr)
		self.flatGS = State(playersTB, flatBoard)

		skinnyArr = [[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],
					 [1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]
		skinnyBoard = Board(tiles=skinnyArr)
		self.skinnyGS = State(playersTB, skinnyBoard)


	def test_get_available_placement(self):
		self.assertEqual((1,0), Strategy.getAvailablePlacement(self.gse1))
		self.gse1.placeAvatar((1, 0))
		self.assertEqual((2,0), Strategy.getAvailablePlacement(self.gse1))
		self.gse1.placeAvatar((2, 0))
		self.assertEqual((0, 1), Strategy.getAvailablePlacement(self.gse1))
		self.gse1.placeAvatar((0, 1))
		self.assertEqual((2,1), Strategy.getAvailablePlacement(self.gse1))
		self.gse1.placeAvatar((2, 1))
		self.assertEqual((2,2), Strategy.getAvailablePlacement(self.gse1))


	def test_penguin_placement(self):
		state0 = self.gse1
		self.assertEqual([], state0.getAllPenguinPositions())

		state1 = Strategy.penguinPlacement(state0)
		self.assertEqual([(1,0)], state1.getAllPenguinPositions())
		self.assertEqual((1,0), state1.players[0].getPenguins()[0].getPos())

		state2 = Strategy.penguinPlacement(state1)
		self.assertEqual([(1,0), (2, 0)], state2.getAllPenguinPositions())
		self.assertEqual((1,0), state2.players[0].getPenguins()[0].getPos())
		self.assertEqual((2,0), state2.players[1].getPenguins()[0].getPos())

		state3 = Strategy.penguinPlacement(state2)
		self.assertEqual([(1,0), (2, 0), (0,1)], state3.getAllPenguinPositions())

	def test_illegal_penguin_placement(self):
		state = self.gse1
		self.assertEqual([], state.getAllPenguinPositions())

		for n in range(8):
			state = Strategy.penguinPlacement(state)

		self.assertFalse(Strategy.penguinPlacement(state)) # If no penguin can be placed then we should know

	def test_penguin_movement(self):

		miniState0 = self.gsMini0
		self.assertEqual( [ [5,0],[1,5], [1,2], [1, 1]], DevTools.tileToIntArray(miniState0.getTiles()))
		self.assertEqual(0, miniState0.players[0].getFish())
		self.assertEqual(0, miniState0.players[1].getFish())
		miniState1 = Strategy.penguinMovement(miniState0, 3)
		self.assertEqual( [ [5,0],[1,5], [0,2], [1, 1]], DevTools.tileToIntArray(miniState1.getTiles()))
		self.assertEqual(1, miniState1.players[0].getFish())
		self.assertEqual(0, miniState1.players[1].getFish())
		miniState2 = Strategy.penguinMovement(miniState1, 3)
		self.assertEqual( [ [5,0],[1,5], [0,0], [1, 1]],  DevTools.tileToIntArray(miniState2.getTiles()))
		self.assertEqual(1, miniState2.players[0].getFish())
		self.assertEqual(2, miniState2.players[1].getFish())

	def test_minimax(self):

		# Strategy.
		self.assertEqual(((0, 2), (0, 0)), Strategy.minimax(self.gtMini0, 1))
		# DevTools.visualizeTree(self.gtMini0)
		self.assertEqual(((0, 2), (0, 1)), Strategy.minimax(self.gtMini0, 3))

	def test_minimax2(self):
		# Mini max of a 2 player game on a mini board with more than enough depth to explore whole board
		# DevTools.visualizeTree(self.gtMini0)
		self.assertEqual(((0, 2), (0, 1)), Strategy.minimax(self.gtMini0, 3))
		# DevTools.visualizeTree(self.gtMini0)

	def test_minimax3(self):
		# 2 players, 4 penguins each, only three tiles remain open
		self.assertEqual(((1,1),(0,3)), Strategy.minimax(self.gt1, 5))

	def test_minimax4(self):
		#  4 players, 2 penguins each, large board, 1 depth
		# DevTools.visualizeTree(self.gt2)
		self.assertEqual(((1, 1), (1, 0)), Strategy.minimax(self.gt2, 1))

	def test_minimax_big(self):
		#  4 players, 2 penguins each, large board, 2 depth. Tests tie breaking across rows
		# from devtools import DevTools
		# DevTools.visualizeTree(self.gt2)
		#TODO: are the next two actually the best actions?
		self.assertEqual(((0, 0), (0, 1)), Strategy.minimax(self.gt2, 2))
		# self.assertEqual(((1, 1), (1, 0)), Strategy.minimax(self.gt2, 2))

	def test_minimax_depth3(self):
		self.assertEqual(((1, 1), (1, 3)), Strategy.minimax(self.gt2, 3))

	def test_minimax_no_move_found(self):
		DevTools.visualizeState(self.gsMini0)
		self.gsMini0.movePenguin(((0, 2), (0, 0)))
		self.gsMini0.movePenguin(((2, 2), (0, 1)))
		self.assertEqual((), Strategy.minimax(GameTree(self.gsMini0), 1))

	def test_movement_priority(self):
		# DevTools.visualizeTree(self.gtTB)
		self.gsTB.placeAvatar((0,0))
		self.gsTB.placeAvatar((1,3))
		self.gsTB.placeAvatar((3,0))
		self.gsTB.placeAvatar((2,3))
		DevTools.visualizeState(self.gsTB)
		p0Moves = GameTree(self.gsTB).root.getAvailableMoves()
		# print(p0Moves)
		p0MovesSorted = p0Moves.copy()
		p0MovesSorted.sort(key=Strategy._getMovementSortKey)
		self.assertEqual( [((0,0), (0, 1)), ((0,0), (0, 2)), ((0, 0), (1, 2)), ((0,0), (0, 4)), ((3, 0), (2, 1)), ((3, 0), (2, 2)), ((3, 0), (3, 2)), ((3, 0), (3, 4))], p0MovesSorted)
		# DevTools.visualizeTree(GameTree(self.gsTB))

	def test_movement_priority_flat_case(self):
		DevTools.visualizeState(self.flatGS)
		self.flatGS.placeAvatar((0, 0))
		self.flatGS.placeAvatar((5, 1))
		self.flatGS.placeAvatar((11, 0))
		self.flatGS.placeAvatar((5, 0))
		moves = GameTree(self.flatGS).root.getAvailableMoves()
		moves.sort(key=Strategy._getMovementSortKey)
		self.assertEqual([((0, 0), (0, 1)), ((11, 0), (10, 1)), ((11, 0), (11, 1))], moves)

	def test_movement_priority_skinny_case(self):
		DevTools.visualizeState(self.skinnyGS)
		self.skinnyGS.placeAvatar((0, 0))
		self.skinnyGS.placeAvatar((0, 3))
		self.skinnyGS.placeAvatar((0, 24))
		self.skinnyGS.placeAvatar((0, 5))
		moves = GameTree(self.skinnyGS).root.getAvailableMoves()
		moves.sort(key=Strategy._getMovementSortKey)
		self.assertEqual([((0, 0), (0, 1)), ((0, 0), (0, 2)), ((0, 0), (0, 4)), ((0, 0), (0, 6)), ((0, 0), (0, 8)),
						  ((0, 0), (0, 10)), ((0, 0), (0, 12)), ((0, 0), (0, 14)), ((0, 0), (0, 16)), ((0, 0), (0, 18)),
						  ((0, 0), (0, 20)), ((0, 0), (0, 22)), ((0, 24), (0, 2)), ((0, 24), (0, 4)), ((0, 24), (0, 6)),
						  ((0, 24), (0, 8)), ((0, 24), (0, 10)), ((0, 24), (0, 12)), ((0, 24), (0, 14)), ((0, 24), (0, 16)),
						  ((0, 24), (0, 18)), ((0, 24), (0, 20)), ((0, 24), (0, 22)), ((0, 24), (0, 23))], moves)

# def test_benchmark_minimax(self):
	# 	from devtools import DevTools
	# 	DevTools.visualizeTree(self.gt2)
	# 	a = Strategy.minimax(self.gtMini0, 20)
		# a = Strategy.minimax(self.gt2, 20)
		# print(a)

