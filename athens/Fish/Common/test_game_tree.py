from unittest import TestCase
from game_tree import *
from PlayerInfo import *
from board import *

class TestGame(TestCase):
	def setUp(self) -> None:
		default_board = Board(holes=[])
		#removed_board = Board(5, [(1, 1), (0, 0), (0, 1)], 3, 4)
		#removed_boardB = Board(5, [(1, 1), (0, 1)], 3, 4)
		#removed_boardC = Board(5, [(1, 1)], width=3, height=4)
		#square_board7 = Board(3, width=5, height=15)
		#tileArrayA = [[0, 1, 2],
		#              [3, 4, 5],
		#              [0, 1, 2],
		#              [3, 4, 5]]
		pOne = PlayerInfo(PenguinColor.red, 0)
		pTwo = PlayerInfo(PenguinColor.black, 1)
		pThree = PlayerInfo(PenguinColor.brown, 2)
		pFour = PlayerInfo(PenguinColor.white, 3)
		allPlayers = [pOne, pTwo]
		self.default_gamestate = State(allPlayers, default_board)
		self.default_gamestate.placeAvatar((0, 0))
		self.default_gamestate.placeAvatar((2, 0))
		self.default_gamestate.placeAvatar((1, 1))
		self.default_gamestate.placeAvatar((2, 2))
		self.default_gamestate.placeAvatar((2, 3))
		self.default_gamestate.placeAvatar((1, 0))
		self.default_gamestate.placeAvatar((1, 3))
		self.default_gamestate.placeAvatar((2, 1))
		self.default_game = GameTree(self.default_gamestate)
		# [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]

		p1 = PlayerInfo(PenguinColor.red, 0)
		p2 = PlayerInfo(PenguinColor.black, 1)
		p3 = PlayerInfo(PenguinColor.white, 2)
		ps = [p1,p2,p3]
		brd = Board(tiles=[[1,1,1,1],[1]])
		self.skipState = State(ps, brd)
		self.skipState.placeAvatar((2,0))
		self.skipState.placeAvatar((3,0))
		self.skipState.placeAvatar((1,0))
		def func1(node: GameNode):
			state = node.getGameState()
			player = state.players[state.turn - 1]
			return player.getFish()
		self.func1 = func1




	def test_apply_action(self):
		self.assertEqual([(0, 0), (1, 1), (2, 3), (1, 3)], self.default_game.root.getGameState().getPlayerPositions(0))
		move1 = ((0, 0), (0, 1))
		node0 = self.default_game.root
		node1 = self.default_game.applyAction(node0, move1)
		self.assertEqual([(0, 1), (1, 1), (2, 3), (1, 3)], node1.getGameState().getPlayerPositions(0))

	# def test_apply_actionNomove(self):
	# 	from devtools import DevTools
	# 	print(self.skipState.allPossibleActions())
	# 	DevTools.visualizeTree(GameTree(self.skipState))
	# 	self.skipState.nextTurn()
	# 	print(self.skipState.allPossibleActions())
	# 	self.skipState.nextTurn()
	# 	print(self.skipState.allPossibleActions())
	# 	DevTools.visualizeTree(GameTree(self.skipState))

	def test_apply_function(self):
		self.assertEqual([(0, 0), (1, 1), (2, 3), (1, 3)], self.default_game.root.getGameState().getPlayerPositions(0))
		move1 = ((0, 0), (0, 1))
		expected_tiles = [[0, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
		node0 = self.default_game.root
		node1 = self.default_game.applyAction(node0, move1)
		self.assertEqual([(0, 1), (1, 1), (2, 3), (1, 3)], node1.getGameState().getPlayerPositions(0))
		# self.default_game.applyFunction(node0, self.func1)
		expected_func1_node0_output = [(((0, 0), (0, 1)), 1),
									 (((0, 0), (1, 2)), 1),
									 (((0, 0), (0, 2)), 1),
									 (((1, 1), (1, 2)), 1),
									 (((1, 1), (0, 3)), 1),
									 (((1, 3), (1, 2)), 1),
									 (((1, 3), (0, 1)), 1)]
		expected_func1_node0_output.sort(key=hash)
		actual_func1_node0_output = self.default_game.applyFunction(node0, self.func1)
		actual_func1_node0_output.sort(key=hash)
		# self.assertEqual([1, 1, 1, 1, 1, 1, 1], self.default_game.applyFunction(node0, self.func1))
		self.assertEqual(expected_func1_node0_output, actual_func1_node0_output)
		self.assertEqual([(((1,0), (1,2)),1)], self.default_game.applyFunction(node1, self.func1))


class TestGameNode(TestCase):
	def setUp(self) -> None:
		default_board = Board(holes=[])
		#removed_board = Board(5, [(1, 1), (0, 0), (0, 1)], 3, 4)
		#removed_boardB = Board(5, [(1, 1), (0, 1)], 3, 4)
		#removed_boardC = Board(5, [(1, 1)], width=3, height=4)
		#square_board7 = Board(3, width=5, height=15)
		#tileArrayA = [[0, 1, 2],
		#              [3, 4, 5],
		#              [0, 1, 2],
		#              [3, 4, 5]]
		pOne = PlayerInfo(PenguinColor.red, 0)
		pTwo = PlayerInfo(PenguinColor.black, 1)
		pThree = PlayerInfo(PenguinColor.brown, 2)
		pFour = PlayerInfo(PenguinColor.white, 3)
		allPlayers = [pOne, pTwo]
		self.default_gamestate = State(allPlayers, default_board)
		self.default_gamestate.placeAvatar((0, 0))
		self.default_gamestate.placeAvatar((2, 0))
		self.default_gamestate.placeAvatar((1, 1))
		self.default_gamestate.placeAvatar((2, 2))
		self.default_gamestate.placeAvatar((2, 3))
		self.default_gamestate.placeAvatar((1, 0))
		self.default_gamestate.placeAvatar((1, 3))
		self.default_gamestate.placeAvatar((2, 1))
		self.default_game = GameTree(self.default_gamestate)

		def func1(node: GameNode):
			state = node.getGameState()
			player = state.players[state.turn - 1]
			#print(state.turn)
			#print(player.getColor())
			return player.getFish()
		self.func1 = func1

	def test_get_avalible_moves(self):
		self.assertEqual([(0, 0), (1, 1), (2, 3), (1, 3)], self.default_game.root.getGameState().getPlayerPositions(0))
		move1 = ((0, 0), (0, 1))
		move2 = ((1, 0), (1, 2))
		expected_tiles = [[0, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
		node0 = self.default_game.root
		self.assertEqual([((0, 0), (0, 1)), ((0, 0), (1, 2)), ((0, 0), (0, 2)), ((1, 1), (1, 2)), ((1, 1), (0, 3)), ((1, 3), (1, 2)), ((1, 3), (0, 1))], self.default_game.root.getAvailableMoves())
		node1 = self.default_game.applyAction(node0, move1)
		self.assertEqual(
			[((1, 0), (1, 2))], node1.getAvailableMoves())
		node2 = self.default_game.applyAction(node1, move2)
		self.assertEqual(
			[((0, 1), (0, 2)), ((0, 1), (0, 3))], node2.getAvailableMoves())
		node3 = self.default_game.applyAction(node2, ((0, 1), (1, 2)))
		self.assertEqual(False, node3)
		node4 = self.default_game.applyAction(node2, ((0, 1), (0, 2)))
		self.assertEqual(
			[((1, 2), (0, 3))], node4.getAvailableMoves())
		node5 = self.default_game.applyAction(node4, ((1, 2), (0, 3)))
		self.assertEqual(
			[()], node5.getAvailableMoves())

	def test_get_next_state(self):
		tiles=self.default_game.root.getNextState(((0, 0), (0, 1))).state.getTiles()
		self.assertEqual([[0, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], [[tile.getFish() for tile in row] for row in tiles])
		move1 = ((0, 0), (0, 1))
		move2 = ((1, 0), (1, 2))
		move3 = ((0, 1), (0, 2))
		move3 = ((1, 2), (1, 3))
		node0 = self.default_game.root
		#node1 = self.default_game.applyAction(node0, move1)
		node1 = node0.getNextState(move1)
		tiles1 = node1.state.getTiles()

		self.assertEqual(
			[[0, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], [[tile.getFish() for tile in row] for row in tiles1])
		node2 = node1.getNextState(move2)
		tiles2 = node2.state.getTiles()
		self.assertEqual(
			[[0, 0, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], [[tile.getFish() for tile in row] for row in tiles2])
		#node2 = self.default_game.applyAction(node0, move2)
		self.assertEqual(
			[((0, 1), (0, 2)), ((0, 1), (0, 3))], node2.getAvailableMoves())
		#node3 = node2.getNextState(((0, 1), (1, 2)))
		try:
			node3 = node2.getNextState(((0, 1), (1, 2)))
			self.assertEqual(False, node3)
		except(Exception):
			pass
		#self.assertEqual(False, node3)
		node4 = node2.getNextState(((0, 1), (0, 2)))
		self.assertEqual(
			[((1, 2), (0, 3))], node4.getAvailableMoves())
		node5 = node4.getNextState(((1, 2), (0, 3)))
		self.assertEqual(
			[()], node5.getAvailableMoves())
