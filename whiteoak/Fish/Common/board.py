from tile import Tile
from json import dumps, load
import sys
from fishexceptions import TileNotFoundException


# Constants denoting the (x,y) change in the specified direction
TOP = (0, -2)
TOP_RIGHT = (1, -1)
BOTTOM_RIGHT = (1, 1)
BOTTOM = (0, 2)
BOTTOM_LEFT = (-1, 1)
TOP_LEFT = (-1, -1)
DIRECTIONS = [TOP, TOP_RIGHT, BOTTOM_RIGHT, BOTTOM, BOTTOM_LEFT, TOP_LEFT]

class Board:

    # X-axis is the axis going from the bottom left to the top right of the hexagon
    # Y-axis is the axis going from the top to the bottom of the hexagon
    # Z-axis is the axis going from the top left to the bottom right of the hexagon
    # The board is represented as a 2d grid, so these 3 "axis" are not actual axis, but rather
    # directions within the board. Rather than having a tile at every coordinate
    # ex. (0,0), (0, 1), (1, 0), (1, 1) we increment by 2 in a given row.
    # This means that in a row the coordinates can go (x, y), (x + 2, y), (x + 4, y)
    # This allows for hexagons that are "in-between".

    # https://www.redblobgames.com/grids/hexagons/#coordinates-doubled

    # numrows = number of rows of tiles
    # numcols = number of columns of tiles
    # holes = array of coordinates [(x,y),(x2,y2)...] for holes in board
    # numfish = number of fish on each tile. can use 0 for random #
    # Constructs the board with numrows rows, numcols columns, numfish fish on
    # each tile, and holes wherever specified
    def __init__(self, numrows, numcols, numfish, holes=[]):
        self.tiles = {}
        self.num_rows = numrows
        self.num_cols = numcols
        cur_x, cur_y = 0, 0
        for x in range(0, numrows):
            for y in range(0, numcols):
                if (cur_x, cur_y) not in holes:
                    self.tiles[(cur_x, cur_y)] = Tile(numfish)
                cur_x += 2
            cur_y += 1
            cur_x = cur_y % 2

    # Returns a list of possible movements from a given tile @(x, y)
    # as a list of coordinates
    # Possible movements are: in a straight line stopping at a hole/avatar
    def get_moves(self, x, y):
        if (x, y) in self.tiles:
            possible_moves = []
            for direction in DIRECTIONS:
                possible_moves += self.get_moves_in_direction(x, y, *direction)
        else:
            raise TileNotFoundException(x, y)
        return possible_moves

    # Helper for getting the list of possible movements from a given tile
    # Movement in the x axis will increment coords by (1, -1) or (-1, 1)
    # Movement in the y axis will increment coords by (0, 2) or (0, -2)
    # Movement in the z axis will increment coords by (1, 1) or (-1, -1)
    # This function takes in the increments to use and spits out all the valid
    # tiles that can be reached by incrementing by that value
    def get_moves_in_direction(self, x, y, incx, incy):
        possible_moves = []
        current_x = x + incx
        current_y = y + incy
        while (current_x, current_y) in self.tiles:
            cur_tile = self.tiles[(current_x, current_y)]
            possible_moves.append((current_x, current_y))
            current_x += incx
            current_y += incy
        return possible_moves

    # Takes in a list of coordinates (the list of possible moves from (x,y))
    # and sets those tiles to be highlighted or un-highlighted depending
    # on arg "switch". Run True while holding a piece, and False when not
    # Takes in the moves so get_moves will only need to be run once per piece
    def hightlight_moves(self, moves, switch):
        for move in moves:
            self.tiles[move].highlight = switch

    # Removes the tile at the given coordinates
    # Returns whether the tile was found (if it was found it was removed)
    # Signature: Position -> Boolean
    def remove(self, pos):
        if pos in self.tiles:
            del self.tiles[pos]
            return True
        else:
            raise TileNotFoundException(pos)

    # Returns the number of fish at a given coordinate
    # Returns None if there is no tile at the given coordinate
    # Signature: Position -> Integer
    def get_num_fish(self, pos):
        if pos in self.tiles:
            return self.tiles[pos].num_fish
        else:
            return None

    # Simulates moving a tile from (x1, y1) to (x2, y2)
    # This entails removing the tile at (x, y)
    # Does NOT check if it was a valid movement
    # Returns the number of fish consumed by the movement
    # Signature: Move -> Integer
    def run_movement(self, move):
        num_fish = self.get_num_fish(move[1])
        self.remove(move[0])
        return num_fish

    # Checks if given (x,y) position is on the board
    # Signature: Position -> Boolean
    def has_tile(self, pos):
        return pos in self.tiles

    # Returns a JSON representation of the board
    # Which is a 2d array; an array of rows, each containing
    # just the number of fish at every location, with 0 meaning a hole
    # Signature: -> Array[Array[Integer]]
    def return_json(self):
        result = []
        cx, cy = 0, 0
        for x in range(self.num_rows):
            current_row = []
            for y in range(self.num_cols):
                if (cx, cy) in self.tiles:
                    val = self.tiles[(cx, cy)].num_fish
                else:
                    val = 0
                current_row.append(val)
                cx += 2
            cy += 1
            cx = cy % 2
            result.append(current_row)
        return result

