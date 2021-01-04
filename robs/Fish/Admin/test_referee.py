from unittest import TestCase
from referee import Referee
from board import Board
from Tile import Tile
from game_tree import GameTree
from PlayerInfo import PlayerInfo
from state import State
from Penguin import PenguinColor
from player import Player
from devtools import DevTools

#TODO: turn off randomness for existing tests.
#TODO: add tests for random generation with fixed seeds

class TestReferee(TestCase):
	def setUp(self) -> None:
	# for testing minimax
		tileArr1 = [[1, 1, 2], [3, 4, 5], [0, 1, 2], [3, 4, 5]]
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
		gs1 = gameState1
		gt1 = GameTree(gameState1)

		tileArr2 = [[1, 2, 3], [5, 4], [1, 0, 3], [0, 4], [1, 2, 3], [5, 4], [1, 2, 0], [5, 4], [1, 0, 3]]
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
		tileArrMini0 = [[5, 0], [1, 5], [1, 2], [1, 1]]
		boardMini0 = Board(tiles=tileArrMini0)
		playerMini00 = PlayerInfo(PenguinColor.black, 0)
		playerMini01 = PlayerInfo(PenguinColor.red, 1)
		gameStateMini0 = State([playerMini00, playerMini01], boardMini0)
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
		tileArr3 = [[0, 1, 1], [1, 0, 1], [0, 0, 1], [1, 0, 1], [0, 1, 0]]
		board4 = Board(tiles=tileArr3)
		playerE10 = PlayerInfo(PenguinColor.white, 0)
		playerE11 = PlayerInfo(PenguinColor.red, 1)
		playerE12 = PlayerInfo(PenguinColor.black, 2)
		playersGSE1 = [playerE10, playerE11, playerE12]
		gameStateEmpty1 = State(playersGSE1, board4)
		gse1 = gameStateEmpty1

		tpl1 = Player(21, "dan")
		tpl2 = Player(22, "danny")
		tpl3 = Player(23, "otherdan")
		tpl4 = Player(24, "bot")
		LoP = [tpl1, tpl2, tpl3, tpl4]
		self.testref = Referee(LoP, 4, 5, fish=1, randomize=False)

		mp1 = Player(1, "mp1")
		mp2 = Player(2, "mp2")
		mps = [mp1, mp2]
		self.miniRef = Referee(mps, 3, 3, fish=1, randomize=False)
		self.twoplayers = mps


	def test_placement_phase(self):
		self.testref.placementPhase()
		self.assertEqual([(0, 0), (4, 0)], self.testref.state.getPlayerPositions(0))
		self.assertEqual([(1, 0), (0, 1)], self.testref.state.getPlayerPositions(1))
		self.assertEqual([(2, 0), (1, 1)], self.testref.state.getPlayerPositions(2))
		self.assertEqual([(3, 0), (2, 1)], self.testref.state.getPlayerPositions(3))
		#self.fail()

	def test_run_movement_round(self):
		self.miniRef.placementPhase()
		self.assertEqual([(0, 0), (2, 0), (1, 1), (0, 2)], self.miniRef.state.getPlayerPositions(0))
		self.miniRef.runMovementRound()
		self.assertEqual([(0, 0), (2, 2), (1, 1), (0, 2)], self.miniRef.state.getPlayerPositions(0))

		self.testref.runMovementRound()
		self.assertEqual([], self.testref.state.getPlayerPositions(0))

		self.testref.placementPhase()
		DevTools.visualizeState(self.testref.state)
		# print("\n movement rounf")
		self.testref.runMovementRound()
		self.assertEqual(set([(0, 2), (4, 0)]), set(self.testref.state.getPlayerPositions(0)))
		self.assertEqual(set([(1, 2), (0, 1)]), set(self.testref.state.getPlayerPositions(1)))
		self.assertEqual(set([(2, 2), (1, 1)]), set(self.testref.state.getPlayerPositions(2)))
		self.assertEqual(set([(3, 1), (2, 1)]), set(self.testref.state.getPlayerPositions(3)))
		DevTools.visualizeState(self.testref.state)
		self.testref.runMovementRound()
		DevTools.visualizeState(self.testref.state)
		self.assertEqual(set([(0, 2), (4, 1)]), set(self.testref.state.getPlayerPositions(0)))
		self.assertEqual(set([(1, 2), (0, 3)]), set(self.testref.state.getPlayerPositions(1)))
		self.assertEqual(set([(2, 2), (1, 3)]), set(self.testref.state.getPlayerPositions(2)))
		self.assertCountEqual([(3, 1), (3, 2)], self.testref.state.getPlayerPositions(3))

	def test_move_phase(self):
		# DevTools.visualizeState(self.testref.state)
		self.testref.movePhase()
		# DevTools.visualizeState(self.testref.state)
		self.assertEqual([], self.testref.state.getPlayerPositions(0))
		self.testref.placementPhase()
		# DevTools.visualizeState(self.testref.state)
		self.assertEqual([(0, 0), (4, 0)], self.testref.state.getPlayerPositions(0))
		self.testref.movePhase()
		# DevTools.visualizeState(self.testref.state)
		# self.assertEqual([(0, 2), (4, 3)], self.testref.state.getPlayerPositions(0))
		self.assertEqual([(0, 3), (4, 3)], self.testref.state.getPlayerPositions(0))
		#self.fail()

	def test_game_over_phase(self):
		self.testref.movePhase()
		self.assertEqual([], self.testref.state.getPlayerPositions(0))
		self.testref.placementPhase()
		self.assertEqual([(0, 0), (4, 0)], self.testref.state.getPlayerPositions(0))
		self.testref.movePhase()
		self.assertEqual([(0, 3), (4, 3)], self.testref.state.getPlayerPositions(0))
		self.testref.gameOverPhase()
		self.assertEqual([(0, 3), (4, 3)], self.testref.state.getPlayerPositions(0))
		#self.fail()


	def test_play(self):
		#self.testref.play()
		stateCopy = self.testref.state.copy()
		self.testref.play()
		scoreList = [i.getFish() for i in stateCopy.players]
		self.assertEqual([0, 0, 0, 0], scoreList)
		otherList = [i.getFish() for i in self.testref.state.players]
		self.assertEqual([4, 2, 2, 4], otherList)


	def test_results(self):
		self.assertDictEqual(self.miniRef.gameResult, {"winners":[], "losers":[], "cheaters":[]})
		self.miniRef.placementPhase()
		self.miniRef.determineResults()
		self.assertDictEqual(self.miniRef.gameResult, {"winners": ["mp1", "mp2"], "losers": [], "cheaters": []})
		self.miniRef.movePhase()
		self.miniRef.determineResults()
		self.assertDictEqual(self.miniRef.gameResult, {"winners":["mp1"], "losers":["mp2"], "cheaters":[]})

	# Just testing that for a given seed Ref will always make the same board
	def test_random_generation(self):
		ref = Referee(self.twoplayers, 4, 4, randomSeed=3)
		self.assertCountEqual(DevTools.tileToIntArray(ref.state.board.tiles), [[4, 4, 1, 2],
													  [4, 3, 5, 4],
													  [0, 4, 0, 3],
													  [2, 4, 1, 1]])

	def test_placement_phase_for_random(self):
		ref = Referee(self.twoplayers, 4, 4, randomSeed=3)
		ref.placementPhase()
		DevTools.visualizeState((ref.state))
		self.assertCountEqual(ref.state.getPlayerPositions(0), [(0, 0), (2, 0), (0, 1), (2, 1)])
		self.assertCountEqual(ref.state.getPlayerPositions(1), [(1, 0), (3, 0), (1, 1), (3, 1)])

	def test_movement_phase_for_random(self):
		ref = Referee(self.twoplayers, 4, 4, randomSeed=3)
		ref.placementPhase()
		ref.movePhase()
		self.assertCountEqual(ref.state.getPlayerPositions(0), [(0, 0), (2, 0), (0, 3), (2, 3)])
		self.assertCountEqual(ref.state.getPlayerPositions(1), [(1, 2), (3, 0), (1, 3), (3, 3)])