#!/usr/bin/env python3
import unittest
from state import GameState
from board import Board
import game_tree
from fishexceptions import InvalidStartStateException, IllegalMoveException
from copy import deepcopy

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.board = Board(12, 2, 2, [])
        self.state = GameState(self.board, 2, [1, 2])
        self.state.place_for_player(0, (1, 3))
        self.state.place_for_player(0, (3, 1))
        self.state.place_for_player(0, (0, 6))
        self.state.place_for_player(0, (2, 8))
        self.state.place_for_player(1, (0, 0))
        self.state.place_for_player(1, (2, 4))
        self.state.place_for_player(1, (1, 11))
        self.state.place_for_player(1, (3, 11))
        self.tree = game_tree.GameTree(self.state)

    # If an invalid starting state is given we should error
    # Invalid = all avatars not placed
    def test_bad_start_state(self):
        self.board = Board(1, 1, 1)
        self.state = GameState(self.board, 1, [1])
        self.assertRaises(InvalidStartStateException, game_tree.GameTree, self.state)

    # Tests if generate children generates a new child for each possible move
    # For player 1
    def test_generate_children(self):
        # Should start with no child nodes
        self.assertFalse(self.tree.children)
        self.tree.generate_children()
        self.assertTrue(self.tree.children)
        self.assertEqual(len(self.tree.children), 26)

    # Tests if the right state for a given move is returned
    # Equality for states is just equality of JSON representation
    def test_expand_node(self):
        move = ((1, 3), (0, 2))
        self.tree.generate_children()
        next_node = self.tree.expand_node(move)
        self.state.run_move(move)
        self.assertDictEqual(self.state.return_json(), next_node.state.return_json())

    # Tests if illegal moves are caught
    def test_illegal_node(self):
        self.assertRaises(IllegalMoveException, self.tree.expand_node, ((1, 3), (9, 9)))

    # Tests checking an action A for a state S
    def test_check_action(self):
        next_node = game_tree.check_action(self.tree, ((2, 8), (3, 9)))
        self.state = deepcopy(self.state)
        self.state.run_move(((2, 8), (3, 9)))
        self.assertDictEqual(next_node.state.return_json(), self.state.return_json())


    # Tests checking an illegal action A for a state S
    def test_illegal_action(self):
        self.assertRaises(IllegalMoveException, game_tree.check_action, self.tree, ((1, 3), (2, 4)))


    # Tests example function (below) applied on children nodes
    def test_apply_function(self):
        results = game_tree.apply_func(self.tree, evaluate_state)
        for move in results:
            self.assertFalse(results[move])

# Test function F
def evaluate_state(node):
    state = node.state
    return state.is_game_over()

if __name__ == '__main__':
    unittest.main()
