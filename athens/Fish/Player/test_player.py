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

class TestPlayer(TestCase):
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
		self.gse1 = gameStateEmpty1

		tpl1 = Player(21, "dan")
		self.tpl1 = Player(21, "dan")
		self.tpl2 = Player(22, "danny")
		self.tpl3 = Player(23, "otherdan")
		self.tpl4 = Player(24, "bot")
		tpl2 = Player(22, "danny")
		tpl3 = Player(23, "otherdan")
		tpl4 = Player(24, "bot")
		LoP = [tpl1, tpl2, tpl3, tpl4]
		self.testref = Referee(LoP, 4, 5)

	def test_assign_color(self):
		self.tpl1.assignColor(PenguinColor.white)
		self.assertEqual(PenguinColor.white, self.tpl1.color)
		#self.fail()

	def test_place_avatar(self):
		placement1 = self.tpl1.placeAvatar(self.gse)
		self.assertEqual((0, 0), placement1)
		self.gse.placeAvatar(placement1)

		placement2 = self.tpl2.placeAvatar(self.gse)
		self.assertEqual((1, 0), placement2)
		#self.fail()

	def test_move_avatar(self):
		placement1 = self.tpl1.placeAvatar(self.gse1)
		self.gse1.placeAvatar(placement1)
		self.gse1.turn -= 1
		movement1 = self.tpl1.moveAvatar(self.gse1)
		self.assertEqual(((1,0), (0,1)), movement1)

	def test_end_of_game(self):
		self.gse.placeAvatar(self.tpl1.placeAvatar(self.gse))
		self.gse.placeAvatar(self.tpl2.placeAvatar(self.gse))
		self.gse.placeAvatar(self.tpl3.placeAvatar(self.gse))
		self.gse.placeAvatar(self.tpl4.placeAvatar(self.gse))
		# from devtools import DevTools
		# DevTools.visualizeState(self.gse)
		exp_placed_positions = [(0, 0), (1, 0), (2, 0), (0, 1)]
		exp_placed_positions.sort(key=hash)
		act_placed_positions = self.gse.getAllPenguinPositions()
		act_placed_positions.sort(key=hash)
		self.assertEqual(exp_placed_positions, act_placed_positions)

		# self.gse.placeAvatar(self.tpl1.moveAvatar(self.gse)[0], self.tpl1.moveAvatar(self.gse)[1])
		# self.gse.placeAvatar(self.tpl2.moveAvatar(self.gse)[0], self.tpl2.moveAvatar(self.gse)[1])
		# self.gse.placeAvatar(self.tpl3.moveAvatar(self.gse)[0], self.tpl3.moveAvatar(self.gse)[1])
		# self.gse.placeAvatar(self.tpl4.moveAvatar(self.gse)[0], self.tpl4.moveAvatar(self.gse)[1])
		# self.assertEqual(5, self.tpl1.endOfGame(self.gse.players[0].getFish()))

		#self.fail()
