#!/usr/bin/env python3
import unittest, board, jsoninterpreter
from fishexceptions import TileNotFoundException


class MyTestCase(unittest.TestCase):
    # Default constructor
    test_board = board.Board(4, 4, 1)
    test_board2 = board.Board(4, 4, 1)
    test_board3 = board.Board(4, 4, 1)
    test_board_no_moves = board.Board(1, 3, 1)
    test_remove_board = board.Board(2, 2, 1)
    test_get_tiles_board = board.Board(3, 1, 1)
    json_test_board = board.Board(3, 3, 5, [(2, 2), (3, 1)])
    json_test_board2 = board.Board(3, 1, 1)

    # Constructor given holes that can be removed
    def test_constructor(self):
        # constructor with holes
        test_holes_board = board.Board(4, 4, 1, [(1, 1), (3, 1)])
        self.assertEqual(self.test_board2.remove((1, 1)), 1)
        self.assertEqual(self.test_board2.remove((3, 1)), 1)
        self.assertCountEqual(test_holes_board.tiles, self.test_board2.tiles)

    # If given holes that cannot exist
    def test_constructor2(self):
        test_holes_board2 = board.Board(4, 4, 1, [(1, 1), (2, 4)])
        self.assertEqual(self.test_board3.remove((1, 1)), 1)
        self.assertCountEqual(test_holes_board2.tiles, self.test_board3.tiles)

    # If we remove, then the number of tiles should go down
    def test_remove(self):
        self.assertTrue(self.test_remove_board.remove((1, 1)))
        self.assertEqual(len(self.test_remove_board.tiles), 3)

    # Testing removing a tile that doesn't exist
    def test_illegal_remove(self):
        self.assertRaises(TileNotFoundException, self.test_remove_board.remove, (5, 5))

    # Testing returning JSON representation of Board
    def test_json(self):
        self.assertEqual(self.test_board.return_json(), [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])

    def test_json_to_board(self):
        json_test_array = [[5, 5, 5], [5, 0, 5], [5, 0, 5]]
        b = jsoninterpreter.json_to_board(json_test_array)
        self.assertCountEqual(self.json_test_board.tiles, b.tiles)

    def test_json_to_board2(self):
        json_test_array = [[1], [1], [1]]
        b = jsoninterpreter.json_to_board(json_test_array)
        self.assertCountEqual(self.json_test_board2.tiles, b.tiles)


if __name__ == '__main__':
    unittest.main()
