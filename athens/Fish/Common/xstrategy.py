import sys
import json

sys.path.append('../')
sys.path.append('../Player')
# sys.path.append('../Player/strategy.py')
from PlayerInfo import PlayerInfo
from state import State
from board import Board
from Penguin import PenguinColor
from game_tree import GameTree
# sys.path.append("../Player")
# from Fish import gam
# from strategy import Strategy
# from kirvin.Fish.Player.strategy import Strategy
# import kirvin.Fish.Player.strategy
# import strategy
# from kirvin.Fish import Player
# from kirvin.Fish.Player import strategy
from strategy import Strategy

colorsMapToEnum = {"red":PenguinColor.red, "black":PenguinColor.black, "white":PenguinColor.white, "brown":PenguinColor.brown}
colorsMapToString = dict((v, k) for k, v in colorsMapToEnum.items())

def flipMovementXandY(move):
	newMove = ((move[0][1], move[0][0]), (move[1][1], move[1][0]))
	return newMove
# [D, State]
def handleJson():
	# print(sys.argv)
	jsonInput = sys.argv[1]
	s_json = jsonInput.lstrip()
	j = json.loads(s_json)

	# print("j", j)

	jstate = j[1]
	tileArray = jstate['board']
	jplayers = jstate['players']
	depth = j[0]
	# print("ta", tileArray)
	# print("p", jplayers)
	# playersJsons = j[0]['players']
	playerInfos = []
	playerIndex = 0
	for pj in jplayers:
		playerInfos.append(PlayerInfo(color=colorsMapToEnum[pj["color"]], turnPriority=playerIndex, fish=pj["score"]))
		for penguinPos in pj["places"]:
			playerInfos[playerIndex].addPenguin((penguinPos[1], penguinPos[0]))
		playerIndex+=1
	board = Board(tiles=tileArray)
	state = State(playerInfos, board=board)
	return depth, state

search_depth, state = handleJson()
tree = GameTree(state.copy())
# if state.allPossibleActions() == []:
# 	print("l;aksjfdlkjs")
# else:
# 	print(state.turn, state.players[state.turn].getColor(), state.allPossibleActions())
best_move = Strategy.minimax(tree, search_depth, state=state)

# sys.path.append('../Other')
# from devtools import DevTools
# print(state.players[state.turn].getColor())
# DevTools.visualizeTree(tree)

# print("tilarr", state.getTiles())
# print("depth", search_depth)
# print("best move", best_move)

if best_move is False:
	out = json.dumps(False)
	print(out, end="")
else:
	best_move = flipMovementXandY(best_move)
	best_move = list(best_move)
	best_move[0] = list(best_move[0])
	best_move[1] = list(best_move[1])
	out = json.dumps(best_move)
	print(out, end="")


