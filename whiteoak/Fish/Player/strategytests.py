#!/usr/bin/env python3
from sys import path
import unittest

from strategy import MinimaxStrategy

path.insert(0, "../Common")

import referee, board, game_tree, state

from fishexceptions import IllegalPlacementException


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.board = board.Board(3, 4, 1, [])
        self.state = state.GameState(self.board, 2, [1, 2])
        self.referee = referee.Referee(self.state)
        self.state.place_for_player(0, (6, 0))
        self.state.place_for_player(1, (0, 0))
        self.state.place_for_player(0, (6, 2))
        self.state.place_for_player(1, (1, 1))
        self.state.place_for_player(0, (7, 1))
        self.state.place_for_player(1, (0, 2))
        self.state.place_for_player(0, (5, 1))
        self.state.place_for_player(1, (2, 0))
        self.strategy = MinimaxStrategy(self.state.turn)

    # Test that a penguin is placed in the right place when possible
    def test_penguin_placement(self):
        p = self.state.players[0].avatars[0]
        self.state.place_avatar(p, None)
        place = self.strategy.place_penguin(self.state)
        self.assertEqual(place, (4, 0))

    # Test that an error is raised when no penguins can be placed
    def test_bad_penguin_placement(self):
        self.assertRaises(IllegalPlacementException, self.strategy.place_penguin, self.state)

    # Tests getting the next action at depth 1
    def test_choose_action(self):
        move = self.strategy.choose_action(self.state, 1)
        self.assertCountEqual(move, ((5, 1), (4, 0)))

    # Tests getting the next action at depth 2
    def test_choose_action2(self):
        move = self.strategy.choose_action(self.state, 2)
        self.assertCountEqual(move, ((5, 1), (4, 0)))

if __name__ == '__main__':
    unittest.main()
