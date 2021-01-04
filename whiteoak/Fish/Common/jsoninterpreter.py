#!/usr/bin/env python3
from board import Board
from state import GameState
from fish_player import FishPlayer

from json import loads

# Converts from the (row, col) form used by the JSON to the double-width system we use
# Signature: Position -> Position
def convert_pos_to_dw(pos):
    new_x = 0
    if pos[0] % 2 == 0:
        new_x = pos[1] * 2
    else:
        new_x = pos[1] * 2 + 1
    return (int(new_x), pos[0])

# Converts from the double-width system we use to the JSON format
# Signature: Position -> Position
def convert_dw_to_pos(dwpos):
    new_x = 0
    if dwpos[1] % 2 == 0:
        new_x = dwpos[0] / 2
    else:
        new_x = (dwpos[0] - 1) / 2
    return (dwpos[1], int(new_x))

# Converts a JSON list representation of a board to a Board object
# ex. of 3x3 board: [[a,b,c],[d,e,f],[g,h,i]] -> Board(...)
# Signature: Array -> Board
def json_to_board(jsonarray):
    numrows = len(jsonarray)
    numcols = len(max(jsonarray, key=len))
    board = Board(numrows, numcols, 1)
    cx, cy = 0, 0
    for x in range(numrows):
        for y in range(numcols):
            if y < len(jsonarray[x]) and jsonarray[x][y] != 0:
                board.tiles[(cx, cy)].num_fish = jsonarray[x][y]
            else:
                board.remove((cx, cy))
            cx += 2
        cy += 1
        cx = cy % 2
    return board

# Converts a JSON representation of a game state to a State
# Signature: Dictionary -> GameState
def json_to_state(jsonstate):
    players = jsonstate["players"]
    board = json_to_board(jsonstate["board"])
    ages = []
    for p in range(len(players)):
        ages.append(p)
    state = GameState(board, len(players), ages)
    new_players = []
    for player in players:
        x = len(new_players)
        p = FishPlayer(x, x, player["color"], len(player["places"]))
        state.add_score(x, player["score"])
        i = 0
        for avatar in player["places"]:
            state.place_avatar(p.avatars[i], tuple(convert_pos_to_dw(avatar)))
            i += 1
        new_players.append(p)
    state.players = new_players
    return state


# Converts a Move-Response-Query into a Tuple of GameState and Move
def json_mrq(mrq):
    state = json_to_state(mrq["state"])
    src = tuple(convert_pos_to_dw(mrq["from"]))
    dest = tuple(convert_pos_to_dw(mrq["to"]))
    move = (src, dest)
    return (state, move)