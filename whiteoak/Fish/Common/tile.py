from random import randint
class Tile:
    # The min and max number of fish possible on a tile
    MAX_NUM_FISH = 5
    MIN_NUM_FISH = 1

    # A Tile consists of:
    #   num_fish, the number of fish on this tile
    #       defaults to a random in range (MIN, MAX) if a bad value is given
    #   highlight = whether this tile is highlighted (used to show possible moves)
    def __init__(self, num_fish):
        self.highlight = False
        if num_fish is None or num_fish > self.MAX_NUM_FISH or num_fish < self.MIN_NUM_FISH:
            self.num_fish = randint(self.MIN_NUM_FISH, self.MAX_NUM_FISH)
        else:
            self.num_fish = num_fish
