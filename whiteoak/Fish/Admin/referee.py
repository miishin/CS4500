#!/usr/bin/env python3
from sys import path
path.insert(0, "../Common")

import board, state, game_tree

path.insert(0, "../Player")
import player, strategy

from enum import Enum

class Phases(Enum):
    SETUP = 0
    GAMEPLAY = 1
    GAME_OVER = 2

# A referee component which can run a complete Fish game for a sequence of players
# Abnormal conditions that will be caught:
#   - Illegal Placement
#   - Illegal Movement
#   - Idle Players

class Referee:

    # A Referee takes in the dimensions of the board along with the number of players and their ages
    # It will create a board along with the player objects to be used
    def __init__(self, numrows, numcols, num_players, player_ages):
        b = None
        b = board.Board(numrows, numcols, 0, [])
        self.state = state.GameState(b, num_players, player_ages)
        self.phase = Phases.SETUP
        self.players = []
        for i in self.state.scores:
            self.players.append(player.Player(i, strategy.MinimaxStrategy(i)))

    # Runs the entire game, going through each phase (setting up, playing, then ending)
    # Signature: None -> None
    def run_game(self):
        self.run_setup()
        self.run_gameplay()
        self.send_results()

    # Runs the set up phase (penguin placements)
    # Mutates self.state
    # Signature: None -> None
    def run_setup(self):
        while self.phase == Phases.SETUP:
            for player in self.players:
                pos = player.place_penguin(self.state)
                if self.state.is_valid_tile(pos):
                    self.state.place_for_player(player.player_id, pos)
                else:
                    self.kick_player(player)
            if self.is_setup_done():
                self.phase = Phases.GAMEPLAY

    # Runs the gameplay phase
    # Moving penguins, the bulk of the game
    # Mutates self.state
    # Signature: None -> None
    def run_gameplay(self):
        while self.phase == Phases.GAMEPLAY:
            for player in self.players:
                if player.player_id == self.state.turn:
                    move = player.choose_action(self.state, 1)
                    if move:
                        if not self.state.run_move(move):
                            self.kick_player(player)
                    else:
                        self.state.increment_turn()
            if self.is_gameplay_done():
                self.phase = Phases.GAME_OVER

    # Returns whether the gameplay phase is over
    # true if no more legal moves left
    # Signature: None -> Boolean
    def is_gameplay_done(self):
        return self.state.is_game_over()

    # Returns whether the setup phase is over
    # true if all penguins have been placed
    # Signature: None -> Boolean
    def is_setup_done(self):
        return self.state.check_game_start()

    # Sends our the results of the game
    # At the moment it just prints scores
    def send_results(self):
        for player_id, score in self.state.scores:
            print("Player " + player_id + " score: " + str(score))

    # Removes designated player from the game
    # Signature: Player -> None
    def kick_player(self, player):
        self.players.remove(player)
        self.state.remove_player(player.player_id)

