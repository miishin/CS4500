import sys
import json
from PlayerInfo import PlayerInfo
from state import State
from board import Board
from Penguin import PenguinColor
colorsMapToEnum = {"red":PenguinColor.red, "black":PenguinColor.black, "white":PenguinColor.white, "brown":PenguinColor.brown}
colorsMapToString = dict((v, k) for k, v in colorsMapToEnum.items())
def handleJson():
	jsonInput = sys.argv[1]
	s_json = jsonInput.lstrip()
	j = json.loads(s_json)
	tileArray = j['board']
	playersJsons = j['players']
	playerInfos = []
	playerIndex = 0
	for pj in playersJsons:
		playerInfos.append(PlayerInfo(color=colorsMapToEnum[pj["color"]], turnPriority=playerIndex, fish=pj["score"]))
		for penguinPos in pj["places"]:
			playerInfos[playerIndex].addPenguin((penguinPos[1], penguinPos[0]))
		playerIndex+=1
	board = Board(tiles=tileArray)
	return board, playerInfos


def sillyTurn(state: State):
	pTurn = state.turn
	targetPenguin = state.getPlayerPositions(pTurn)[0]
	pengFrom = targetPenguin
	pengFx = pengFrom[0]
	pengFy = pengFrom[1]

	turnWishlist = [
		Board.north(pengFx, pengFy, 1),
		Board.northEast(pengFx, pengFy, 1),
		Board.southEast(pengFx, pengFy, 1),
		Board.south(pengFx, pengFy, 1),
		Board.southWest(pengFx, pengFy, 1),
		Board.northWest(pengFx, pengFy, 1) ]
	validMoves = state.getReachableTiles(pengFx, pengFy)
	for turnRequest in turnWishlist:
		if turnRequest in validMoves:
			state.movePenguin(((pengFx, pengFy), turnRequest))
			return state
	return False
	# board = Board(tiles=tileArray)
	# return board, playerInfos

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
		playerJ = {"color" : color, "score": score, "places": places}
		playersJ.append(playerJ)

	fishArray = tileArrayToFishArray(state.getTiles())
	stateDict = {}
	stateDict["players"] = playersJ
	stateDict["board"] = fishArray
	outputStateJson = json.dumps(stateDict)
	return outputStateJson

board, playerInfos = handleJson()
gameState = State(playerInfos, board)

resultState = sillyTurn(gameState)
if not resultState:
	print("False", end="")
else:
	outJson = stateToJson(resultState)
	print(outJson, end="")
