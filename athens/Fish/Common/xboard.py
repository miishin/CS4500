from board import*
import sys
import json

def handleJson():
	jsonInput = sys.argv[1]
	s_json = jsonInput.lstrip()
	j = json.loads(s_json)
	targetPosition = j['position']
	tileArray = j['board']
	board = Board(tiles=tileArray)
	return board, tuple(targetPosition)
board, targetPos = handleJson()

print(len(board.getReachableTiles(targetPos[1], targetPos[0])), end="")

