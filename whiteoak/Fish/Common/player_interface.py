#!/usr/bin/env python3

# A Player Interface is defined as a connection to a Referee.
# Players can use this interface to communicate with the Referee
# and query information
# This may at first seem like just a wrapper for a referee but having a player
# interact with PI instead of a Referee limits what the player can ask for.
class PlayerInterface():

    def __init__(self, referee):
        self.referee = referee

    # Asks the referee for a JSON representation of the current game state
    # to be returned to the player
    # Signature: Self -> Dictionary
    def get_current_game(self):
        return self.referee.get_game()

    # Asks the referee for the next children from the current node in the tree
    # Signature: Self -> JSONArray
    def get_children(self):
        return self.referee.get_children()

    # Asks the referee for the node reached by executing a given move
    # Signature: Move -> Dictionary
    def expand_node(self, move):
        return self.referee.expand_node(move)

    # Asks the referee if player (pid) can place an avatar at a position
    # Returns JSON value true or false depending on answer (will be placed if true)
    # Signature: Integer Position -> Boolean
    def place_avatar(self, pid, pos):
        return self.referee.place_avatar(pid, pos)

    # Asks the referee if player (pid) can move an avatar (the input is the move)
    # Returns JSON value true or false depending on answer (will be moved if true)
    # Signature: Integer Move -> Boolean
    def move_avatar(self, pid, move):
        return self.referee.move_avatar(pid, move)

    # Asks the referee for player (pid)'s score at the moment
    # Returns JSON value of just a number
    # Signature: Integer -> Integer
    def get_score(self, pid):
        return self.referee.get_score(pid)


    # Attempt to have tree initialized once penguins have been placed
    def start_game(self):
        return self.referee.initialize_tree()