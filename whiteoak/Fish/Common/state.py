#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:14:26 2020

@author: andrewduffy
"""
import board
import fish_view
import fish_player
from fishexceptions import TileNotFoundException

# Constants denoting the (x,y) change in the specified direction
TOP = (0, -2)
TOP_RIGHT = (1, -1)
BOTTOM_RIGHT = (1, 1)
BOTTOM = (0, 2)
BOTTOM_LEFT = (-1, 1)
TOP_LEFT = (-1, -1)
DIRECTIONS = [TOP, TOP_RIGHT, BOTTOM_RIGHT, BOTTOM, BOTTOM_LEFT, TOP_LEFT]



class GameState:
    # Game over?
    COLORS = ['RED', 'WHITE', 'BROWN', 'BLACK']
    PHASES = ['PLACEMENT', 'GAMEPLAY', 'GAME_OVER']

    # Initializing a new game state only needs:
    # A board, the number of players, and the players' ages
    # All other info (penguins, players, etc.) are generated
    # The list of players is ordered by turn (ages are sorted and then players created off that sorting)
    # self.turn is the turn number
    def __init__(self, board, num_players, player_ages):
        self.board = board
        num_penguins = 6 - num_players
        self.num_players = num_players
        self.players = []
        # a mapping of player-id's to scores. 
        self.scores = {}
        # generate player objects and initialize score-mapping. For now, player-id's
        # will be assigned by their index in the list.
        for i in range(num_players):
            cur_player = fish_player.FishPlayer(i, player_ages[i], self.COLORS[i], num_penguins)
            self.players.append(cur_player)
            self.scores[i] = 0
        self.game_over = False
        self.turn = 0 # denotes the player who's turn it is (their index in self.players)

    # Returns score for a given player ID
    def get_score(self, player_id):
        return self.scores[player_id]

    # Returns a list of possible movements from a given tile @ a position
    # as a list of coordinates
    # Possible movements are: in a straight line stopping at a hole/avatar
    # Signature: Position -> Listof(Position)
    def get_moves(self, pos):
        if pos in self.board.tiles:
            possible_moves = []
            for direction in DIRECTIONS:
                possible_moves += self.get_moves_in_direction(pos, direction)
        else:
            raise TileNotFoundException(pos)
        return possible_moves

    # Helper for getting the list of possible movements from a given tile
    # Movement in the x axis will increment coords by (1, -1) or (-1, 1)
    # Movement in the y axis will increment coords by (0, 2) or (0, -2)
    # Movement in the z axis will increment coords by (1, 1) or (-1, -1)
    # This function takes in the increments to use and spits out all the valid
    # tiles that can be reached by incrementing by that value
    # Signature: Position Listof(Position) Tuple(X_Increment, Y_Increment) -> Listof(Move)
    def get_moves_in_direction(self, pos, direction):
        possible_moves = []
        current_x = pos[0] + direction[0]
        current_y = pos[1] + direction[1]
        while self.is_valid_tile((current_x, current_y)):
            possible_moves.append((current_x, current_y))
            current_x += direction[0]
            current_y += direction[1]
        return possible_moves


    # Returns all the positions of the tiles on the board that are occupied by penguins
    # Signature: Self -> Listof(Position)
    def occupied_tiles(self):
        tiles = []
        for player in self.players:
            for avatar in player.avatars:
                tiles.append(avatar.position)
        return tiles


    # Given a player ID, returns all the possible moves for that player
    # Signature: Integer -> Dictionary(Avatar: Listof(Position))
    def get_player_moves(self, pid):
        moves = {}
        player = self.players[pid]
        for avatar in player.avatars:
            moves_from_avatar = self.get_moves(avatar.position)
            if moves_from_avatar:
                moves[avatar] = moves_from_avatar
        return moves # all the possible moves

    # Player turn = their index in self.players
    # By using modulo self.turn always == the index of the current player who's turn it is
    # Signature: Self -> None
    def increment_turn(self):
        for idx, player in enumerate(self.players):
            if player.player_id == self.turn:
                if idx == self.num_players - 1:
                    self.turn = self.players[0].player_id
                else:
                    self.turn = self.players[idx + 1].player_id

    ### Placement Phase Functions (Placing penguins to start game)

    # Places an avatar for a player at a given position
    # picks the first unplaced avatar in their list
    # Signature: Integer Position -> None
    def place_for_player(self, pid, pos):
        player = self.players[pid]
        for avatar in player.avatars:
            if avatar.position is None:
                self.place_avatar(avatar, pos)
                return True
        return False

    # Places an avatar at a given position
    # Can also be used for movement (movement is just placing somewhere else)
    # Signature: Penguin Position -> None
    def place_avatar(self, avatar, pos):
        avatar.place(pos)
        self.increment_turn()

    # Returns whether a given position is valid (for placement or movement)
    # Signature: Position -> Boolean
    def is_valid_tile(self, pos):
        return pos not in self.occupied_tiles() and pos in self.board.tiles

    # Return whether all penguins have been placed - this means the real game can start
    # Signature: None -> Boolean
    def check_game_start(self):
        for player in self.players:
            for avatar in player.avatars:
                if avatar.position is None:
                    return False
        return True


    ### Gameplay Functions (Everything in a "Game" Tree) ###

    # add the value of score to the player id 'pid' in the score map.
    # Signature: Integer Integer -> None
    def add_score(self, pid, score):
        self.scores[pid] += score

    # Moves an avatar from (x1,y1) to (x2,y2)
    # Don't need to check for things like x1=x2 and y1=y2 bc
    # this should only be called after getting valid moves
    # Returns the # of fish consumed
    # Signature: Player Penguin Move -> Integer
    def move_avatar(self, player, avatar, move):
        start = move[0]
        end = move[1]
        avatar.place(end)
        fish = self.board.run_movement(move)
        self.add_score(player.player_id, fish)
        return fish


    # Executes a given move
    # Moves the avatar at the source to the destination
    # If the move is invalid (either position isn't on board or is invalid)
    # then return False, else return True
    # Signature: Move -> Boolean
    def run_move(self, move):
        player = self.players[self.turn]
        for avatar in player.avatars:
            if avatar.position == move[0] and self.is_valid_tile(move[1]):
                self.move_avatar(player, avatar, move)
                self.increment_turn()
                return True
        return False


    # Removes a player from the game
    # Takes in a player_id
    # Signature: Integer -> None
    def remove_player(self, player_id):
        self.increment_turn()
        self.scores.pop(player_id)
        for player in self.players:
            if player.player_id == player_id:
                self.players.remove(player)
        self.num_players -= 1

    ### Game Over ###

    # Determines if there are any legal moves left
    # (same as whether the game is over yet)
    # Signature: Self -> Boolean
    def is_game_over(self):
        for player in self.players:
            for avatar in player.avatars:
                if avatar.position and self.get_moves(avatar.position):
                    return False
        return True

    ### Render ###

    # Renders game state graphically
    def render_gamestate(self):
        fish_view.tk_view(self)


    ### JSON ###

    # Returns JSON representation of this GameState
    # State is:
    #   Players
    #   Board
    def return_json(self):
        json_state = {"players": []}
        for player in self.players:
            json_state["players"].append(player.return_json(self.scores[player.player_id]))
        json_state["board"] = self.board.return_json()
        return json_state

