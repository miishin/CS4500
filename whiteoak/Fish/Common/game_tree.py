#!/usr/bin/env python3
from fishexceptions import IllegalMoveException, InvalidStartStateException
import board
from state import GameState
from copy import deepcopy

class GameTree:

    # Creates a "complete" tree for a given starting game state
    # starting_state is a GameState where all the penguins have been placed
    # GameTree node consists of a GameState and Children nodes
    # children is a list of moves
    # a move is: ((x1, y1), (x2, y2))
    # a tuple of tuples denoting the starting and ending coordinates

    def __init__(self, starting_state):
        if starting_state.check_game_start():
            self.state = starting_state
        else:
            raise InvalidStartStateException()
        self.children = []

    # Generates the children for this node
    # Signature: None -> None
    def generate_children(self):
        if not self.children:
            # get_player_moves will return all the possible moves for the given player as a dict (penguin: [moves])
            # so we will need to flatten the dictionary into a list of moves
            moves = self.state.get_player_moves(self.state.turn)
            flattened_moves = []
            for avatar in moves:
                avatar_moves = moves[avatar]
                for move in avatar_moves:
                    flattened_moves.append((avatar.position, move))
            self.children = flattened_moves


    # Returns the children for this node
    # Signature: None -> Moves
    def get_children(self):
        self.generate_children()
        return self.children


    # Finds the child node reachable with a given move and returns that child node
    # Signature: Move -> GameTree
    # Throws an IllegalMoveException if given move is illegal
    def expand_node(self, move):
        if move in self.children:
            new_state = deepcopy(self.state)
            new_state.run_move(move)
            return GameTree(new_state)
        else:
            raise IllegalMoveException()

    # Finds the child node for the next turn
    # If the current game is not over and the current player is stuck
    # Then we just want a node where the state is the next turn
    # Signature: None -> GameTree
    def skip_node(self):
        self.generate_children()
        if not self.children:
            if not self.state.is_game_over():
                new_state = deepcopy(self.state)
                new_state.increment_turn()
                return GameTree(self.state)

# Generating a tree from a given state instead of searching in some
# massive "entire game" tree will have the same result IF
# there is no mutation occuring
# Generating a new tree is functionally the same as just going to that point in the "entire" tree

# Given a state S and evaluation function F, applies F to all states
# reachable from S (all the child nodes of S' node)
# basically a map over the children using func
# F has signature GameNode -> Any
# Signature; GameTree [GameNode -> Any] -> Dictionary(move : Any)
def apply_func(gtree, func):
    gtree.generate_children()
    results = {}
    for move in gtree.children:
        results[move] = func(gtree.expand_node(move))
    return results


# For a given game state (game tree node) S and action A, returns either:
# S1, the state reached from S after taking action A
# or signals that A is illegal
# A = a move
# Signature: GameTree Move -> GameTree
def check_action(gtree, action):
    gtree.generate_children()
    return gtree.expand_node(action)


