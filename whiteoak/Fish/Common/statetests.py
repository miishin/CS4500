import unittest
import argparse
from sys import argv
from fishexceptions import TileNotFoundException
from board import Board
from state import GameState

render = True

class MyTestCase(unittest.TestCase):

    board = Board(2, 1, 5)
    state = GameState(board, 1, [1])
    test_board = Board(4, 4, 1)
    test_state = GameState(test_board, 1, [1])
    test_board_no_moves = Board(1, 3, 1)
    test_state_no_moves = GameState(test_board_no_moves, 1, [1])

    # Test whether a movement can lead to a game over state
    def test_game_over_movement(self):
        self.state.place_avatar(self.state.players[0].avatars[0], (0, 0))
        player = self.state.players[0]
        fish = self.state.move_avatar(player, player.avatars[0], ((0, 0), (1, 1)))
        self.assertTrue(self.state.is_game_over())
        self.assertEqual(fish, 5)

    # Testing game over for a board with no possible moves
    def test_game_over(self):
        b = Board(1, 1, 1)
        s = GameState(b, 1, [1])
        s.place_avatar(s.players[0].avatars[0], (0, 0))
        self.assertTrue(s.is_game_over())

    # Tests rendering - commented out bc running tests is annoying when GUI pops up
    """
    def test_state_render(self):
        if render:
            board_test = Board(4,4,0)
            gamestate_test = GameState(board_test,2,[14,3])
            gamestate_test.place_avatar(gamestate_test.players[0].avatars[0],2,0)
            gamestate_test.place_avatar(gamestate_test.players[0].avatars[1],1,1)
            gamestate_test.render_gamestate()
    """

    # Tests whether a game can start
    def test_game_start(self):
        b = Board(10, 10, 0)
        s = GameState(b, 2, [1, 2])
        for i in range(3):
            s.place_avatar(s.players[0].avatars[i], (i, i))
            s.place_avatar(s.players[1].avatars[i], (i + 2, i))
        self.assertFalse(s.check_game_start())
        s.place_avatar(s.players[0].avatars[3], (4, 4))
        s.place_avatar(s.players[1].avatars[3], (6, 4))
        self.assertTrue(s.check_game_start())

    def test_get_moves_1(self):
        self.assertCountEqual(self.test_state.get_moves((1, 1)), [(0, 0), (0, 2), (1, 3), (2, 2), (2, 0), (3, 3)])

    def test_get_moves_2(self):
        self.assertCountEqual(self.test_state.get_moves((0, 0)), [(1, 1), (2, 2), (3, 3), (0, 2)])

    def test_get_moves_3(self):
        self.assertCountEqual(self.test_state.get_moves((3, 1)), [(2, 0), (2, 2), (1, 3), (3, 3), (4, 2), (4, 0), (5, 3)])

    def test_get_moves_4(self):
        self.assertCountEqual(self.test_state_no_moves.get_moves((0, 0)), [])


    # Testing get_move from tile not on board
    def test_get_moves_error(self):
        self.assertRaises(TileNotFoundException, self.test_state.get_moves, (50, 50))



if __name__ == '__main__':
    unittest.main()
