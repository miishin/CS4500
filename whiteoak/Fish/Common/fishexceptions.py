# Exception for when a tile is not found on the board
# ex: trying to remove a piece from a tile not on the board
class TileNotFoundException(Exception):

    def __init__(self, pos):
        self.pos = pos
        super().__init__()

    def __str__(self):
        return f'Tile not found at {self.pos}'


# Exception for when an illegal move is attempted
class IllegalMoveException(Exception):
    pass

# Exception for when an illegal placement is attempted
class IllegalPlacementException(Exception):
    pass

# Exception for when a GameTree is made without a fully initialized game state
# (ie all the avatars have not been placed)
class InvalidStartStateException(Exception):
    pass