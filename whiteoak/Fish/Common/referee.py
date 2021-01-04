#!/usr/bin/env python3
import json
from game_tree import GameTree

class Referee:

    def __init__(self, state):
        self.state = state
        self.tree = None

    ### At any Time

    # If the current game has started, then we can initialize the tree
    # Returns whether initialization is alllowed
    # Signature: None -> Boolean
    def initialize_tree(self):
        if self.state.check_game_start():
            self.tree = GameTree(self.state)
            return True
        else:
            return False

    # Returns current game state as a JSON object
    # Signature: Self -> Dictionary
    def get_game(self):
        return self.state.return_json()

    # Returns player score as JSON object
    # Signature: Integer -> Integer
    def get_score(self, pid):
        ...

    ### Setting up Game

    # Places avatar at a given Position for player (pid) if possible
    # Returns JSON true if placed or false otherwise
    # Signature: Integer Position -> Boolean
    def place_avatar(self, pid, pos):
        return self.state.place_for_player(pid, pos)

    # Returns whether the game has been set up (all penguins have been placed)
    # and the game can start
    # Signature: None -> Boolean
    def is_game_set_up(self):
        ...

    ### Running the Game

    # Generates tree children and return as a JSON list of moves
    # Signature: Self -> JSONArray
    def get_children(self):
        self.tree.generate_children()
        return json.dumps(self.tree.children)

    # Expands the game tree and returns resulting GameState as JSON
    # Signature: Move -> Dictionary
    def expand_tree(self, move):
        next_node = self.tree.expand_node(move)
        return next_node.state.return_json()

    # Moves avatar according to a given move for player (pid) if possible
    # Returns JSON true if moved or false otherwise
    # False could be invalid move or moving other players piece
    # Signature: Integer Move -> Boolean
    def move_avatar(self, pid, move):
        ...

    # Kicks a player that has attempted to cheat
    # Signature: Integer -> None
    def kick_player(self, pid):
        ...

    ### Shutting down Game

    # Shuts the current Game down
    # Signature: None -> None
    def shut_down(self):
        ...

    # Sends results of the Game to Tournament Admin
    # Signature: None -> None
    def send_results(self):
        ...