#!/usr/bin/env python3
from sys import path

path.insert(0, "../Common")
from game_tree import GameTree
from state import GameState
from jsoninterpreter import json_to_state
from fishexceptions import IllegalPlacementException

class MinimaxStrategy:

    # A strategy holds onto a player_id to make decisions
    def __init__(self, player_id):
        self.player_id = player_id

    # Places a penguin in the next available free spot following a zig zag pattern that starts at the top left corner.
    # That is, the search goes from left to right in each row and moves down to the next row when one is filled up.
    # The first penguin that can be placed by the current player will be placed
    # Assumes that the referee sets up a board large enough to accommodate all penguins (as per assignment)
    # Returns where to place the penguin (to let the referee do the actual placement and validate it)
    # Signature: None -> Position
    def place_penguin(self, gamestate):
        if gamestate.check_game_start():
            raise IllegalPlacementException()
        invalid_tiles = gamestate.occupied_tiles()
        for tile in gamestate.board.tiles:
            if tile not in invalid_tiles:
                return tile
        raise IllegalPlacementException()


    # Returns the action with the greatest maximum gain (score)
    # within N turns for player P (N turns = P going N times).
    # N > 0
    # Assumes that every other player will take the action that minimizes P's score
    # The output is a move (Tuple of Position)
    # Signature: GameState Integer Integer -> Move
    def choose_action(self, curr_state, num_turns):
        curr_tree = GameTree(curr_state)
        best_move = None
        curr_max = float("-inf")
        moves = curr_tree.get_children()
        for move in moves:
            child = curr_tree.expand_node(move)
            score = self.minimax(child, 1, num_turns)
            if score > curr_max:
                curr_max = score
                best_move = move
            elif score == curr_max:
                best_move = self.break_tie(best_move, move)
        return best_move

    # Breaks ties (multiple moves that go to the same place)
    # picks the penguin that has the lowest row number for the place from which the penguin is moved
    # and, within this row, the lowest column number
    # If this doesn't break the tie, repeat with the "to" move's positions.
    # Signature: Move Move -> Move
    def break_tie(self, move1, move2):
        from_pos1 = move1[0]
        from_pos2 = move2[0]
        to_pos1 = move1[1]
        to_pos2 = move2[1]

        if from_pos1[0] < from_pos2[0]:
            return move1
        elif from_pos2[0] < from_pos1[0]:
            return move2
        elif from_pos1[1] < from_pos2[1]:
            return move1
        elif from_pos2[1] < from_pos1[1]:
            return move2
        elif to_pos1[0] < to_pos2[0]:
            return move1
        elif to_pos2[0] < to_pos1[0]:
            return move2
        elif to_pos1[1] < to_pos2[1]:
            return move1
        else:
            return move2

    # Recursively runs the "minimax" adversarial search algorithm on the given state
    # and returns an integer representing the score of this state. See gamestate_evaluation for more score-info.
    # The player_id and depth are used to decide whether the game is over or whether min/max should be used.
    # Signature GameSTree curr_node, Integer player_idx, Integer depth -> Integer score
    def minimax(self, curr_node, depth, max_depth):
        if curr_node.state.is_game_over() or depth == max_depth:
            return self.gamestate_evaluation(curr_node, self.player_id)

        children = curr_node.get_children()
        if curr_node.state.turn == self.player_id:
            if children:
                return max([self.minimax(curr_node.expand_node(move), depth + 1, max_depth) \
                        for move in children])
            else:
                return self.minimax(curr_node.skip_node(), depth + 1, max_depth)
        else:
            if children:
                return min([self.minimax(curr_node.expand_node(move), depth, max_depth) \
                        for move in children])
            else:
                return self.minimax(curr_node.skip_node(), depth, max_depth)

    # Takes in a gameState and player representation and returns a score that
    # represents how 'good' the state is for the given player. This score is calculated
    # by taking the sum of the best move for each penguin of the player.  Higher scores mean
    # that the state is better for the player.
    # Signature: GameTree curr_node Integer player -> Integer score
    def gamestate_evaluation(self, curr_node, player_id):
        state = curr_node.state
        return state.get_score(player_id)