import sys
import json
from PlayerInfo import PlayerInfo
from state import State
from board import Board
from Penguin import PenguinColor
from game_tree import GameTree, GameNode

colorsMapToEnum = {"red":PenguinColor.red, "black":PenguinColor.black, "white":PenguinColor.white, "brown":PenguinColor.brown}
colorsMapToString = dict((v, k) for k, v in colorsMapToEnum.items())

def flipMovementXandY(move):
	newMove = ((move[0][1], move[0][0]), (move[1][1], move[1][0]))
	return newMove
def handleJson() -> (GameTree, tuple):
	jsonInput = sys.argv[1]
	s_json = jsonInput.lstrip()
	j = json.loads(s_json)

	stateDict = j['state']
	tileArray = stateDict['board']
	playersJsons = stateDict['players']

	playerInfos = []
	playerIndex = 0
	for pj in playersJsons:
		playerInfos.append(PlayerInfo(color=colorsMapToEnum[pj["color"]], turnPriority=playerIndex, fish=pj["score"]))
		for penguinPos in pj["places"]:
			playerInfos[playerIndex].addPenguin((penguinPos[1], penguinPos[0]))
		playerIndex += 1
	board = Board(tiles=tileArray)
	gameState = State(playerInfos, board)

	moveFrom = tuple(j['from'])
	moveTo = tuple(j['to'])
	move = flipMovementXandY(((moveFrom, moveTo)))

	return GameTree(gameState), move

	move = []

	outJson = moveToAction(gameState, j['from'], j['to'])

	output = json.dumps(outJson)
	print(output)
	return output

def moveToAction(state: State, fromp: tuple, toP: tuple):
	if (toP[0], toP[1]) in state.getReachableTiles(fromp[0], fromp[1]):
		state.movePenguin(fromp, toP)

		for i in state.getPlayerPositions(state.turn):
			for j in adject_spots(toP[0], toP[1]):
				if (j[0], j[1]) in state.getReachableTiles(i[0], i[1]):
					return [(i[0], i[1]), (j[0], j[1])]
				else:
					pass
	else:
		return False
	pass

def adject_spots(x, y):
	adj = []
	adj.append(Board.north(x, y, 1))
	adj.append(Board.northEast(x, y, 1))
	adj.append(Board.southEast(x, y, 1))
	adj.append(Board.south(x, y, 1))
	adj.append(Board.southWest(x, y, 1))
	adj.append(Board.northWest(x, y, 1))
	return adj




def stateToJson(state: State):
	def tileArrayToFishArray(tileArray):
		return [[tile.getFish() for tile in row] for row in tileArray]
	playersJ = []
	for player in state.players:
		places = []
		for penguin in player.getPenguins():
			pengX, pengY = penguin.getPos()
			places.append([pengY, pengX])
		color = colorsMapToString[player.getColor()]
		score = player.getFish()
		playerJ = {"color": color, "score": score, "places": places}
		playersJ.append(playerJ)

	fishArray = tileArrayToFishArray(state.getTiles())
	stateDict = {}
	stateDict["players"] = playersJ
	stateDict["board"] = fishArray
	outputStateJson = json.dumps(stateDict)
	return outputStateJson

def nearestMove(target, node: GameNode):
	viableTiles = adject_spots(target[0], target[1])
	actions = node.getGameState().allPossibleActions()
	for tile in viableTiles:
		for action in actions:
			if tile == action[1]:
				return action
	return False

tree, move = handleJson()

#sys.path.append("../Fish/Other")
#from devtools import DevTools

#DevTools.visualizeTree(tree)

sys.path.append('../')
sys.path.append('../Fish')
sys.path.append('../Fish/Other')
sys.path.append('../Other')
sys.path.append('../Player')
# import
# from devtools import DevTools
# DevTools.visualizeTree(tree)


node1 = tree.applyAction(tree.root, move)

#DevTools.visualizeState(node1.getGameState())

outmove = nearestMove(move[1], node1)
if outmove is False:
	out = json.dumps(False)
	print(out, end="")
else:
	outmove = flipMovementXandY(outmove)
	outmove = list(outmove)
	outmove[0] = list(outmove[0])
	outmove[1] = list(outmove[1])
	out = json.dumps(outmove)
	print(out, end="")

