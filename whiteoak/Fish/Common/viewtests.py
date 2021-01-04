#!/usr/bin/env python3
import board
from sys import argv
from fish_view import tk_view
import unittest
import fish_view as fv
import state


class TileTest(unittest.TestCase):

    def test_board1(self):
        # Basic board with 1 fish on every tile
        b = board.Board(4, 4, 1)
        print("Showing a 4x4 board with 1 fish on every tile")
        s = state.GameState(b, 1, [1])
        tk_view(s)

    def test_board2(self):
        # Basic board with 1 fish on every tile and two holes
        b = board.Board(4, 4, 1, [(1, 1), (3, 1)])
        print("Showing a 4x4 board with 1 fish on every tile & a hole at (1,1) and (3,1)")
        s = state.GameState(b, 1, [1])
        tk_view(s)

    def test_board3(self):
        # Smaller Board with 3 fish on every tile
        b = board.Board(2, 4, 3)
        print("Showing a 2x4 board with 3 fish on every tile")
        s = state.GameState(b, 1, [1])
        tk_view(s)

    def test_board4(self):
        # Smaller board with 3 fish on every tile and 1 hole
        b = board.Board(2, 4, 3, [(1, 1)])
        print("Showing a 2x4 board with 3 fish on every tile and a hole at (1,1)")
        s = state.GameState(b, 1, [1])
        tk_view(s)

    def test_board5(self):
        # 3x3 board with random # of fish on every tile
        b = board.Board(3, 3, None)
        print("Showing a 3x3 board with random # of fish on every tile")
        s = state.GameState(b, 1, [1])
        tk_view(s)
        
    def test_get_vertices(self):
        self.assertEqual(fv.get_hex_vertices((0,0)), \
                         [(95, 20), (170, 20), (245, 95), (170, 170), (95, 170), (20, 95)])
        self.assertEqual(fv.get_hex_vertices((1,0)), \
                         [(245, 20), (320, 20), (395, 95), (320, 170), (245, 170), (170, 95)])
        self.assertEqual(fv.get_hex_vertices((1,1)), \
                         [(245, 95), (320, 95), (395, 170), (320, 245), (245, 245), (170, 170)])
        self.assertEqual(fv.get_hex_vertices((2,0)), \
                         [(395, 20), (470, 20), (545, 95), (470, 170), (395, 170), (320, 95)])
        self.assertEqual(fv.get_hex_vertices((0,2)), \
                         [(95, 170), (170, 170), (245, 245), (170, 320), (95, 320), (20, 245)])
            
    def test_find_center(self):
        points1 = [(95, 20), (170, 20), (245, 95), (170, 170), (95, 170), (20, 95)]
        points2 = [(245, 20), (320, 20), (395, 95), (320, 170), (245, 170), (170, 95)]
        points3 = [(245, 95), (320, 95), (395, 170), (320, 245), (245, 245), (170, 170)]
        self.assertEqual(fv.find_center_of_tile(points1),(132.5, 95.0))
        self.assertEqual(fv.find_center_of_tile(points2),(282.5, 95.0))
        self.assertEqual(fv.find_center_of_tile(points3),(282.5, 170.0))
    
    def test_find_widthandheight(self):
        self.assertEqual(fv.find_widthandheight(0,0),(115, 115))
        self.assertEqual(fv.find_widthandheight(1,0),(415, 115))
        self.assertEqual(fv.find_widthandheight(0,1),(115, 190))
        self.assertEqual(fv.find_widthandheight(1,1),(415, 190))
        self.assertEqual(fv.find_widthandheight(2,3),(715, 340))
        self.assertEqual(fv.find_widthandheight(5,5),(1615, 490))
        self.assertEqual(fv.find_widthandheight(6,3),(1915, 340))




if __name__ == '__main__':
    unittest.main()
