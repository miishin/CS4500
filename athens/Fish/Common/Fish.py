from FishGui import FishGui
from board import*
from PyQt5.QtWidgets import QApplication
import sys
import json
from Penguin import *
from state import State
from PlayerInfo import PlayerInfo
# for i in sys.argv:
# 	print(i)

def handleJson():
	jsonInput = sys.argv[1]
	s_json = jsonInput.lstrip()
	decoder = json.JSONDecoder()
	n = 0
	s_lenth = len(s_json)
	jsons = []
	print(jsonInput)
	# print(json.dumps(jsonInput))
	j = json.loads(jsonInput)
	print(j)
	print(j['board'])
	targetPosition = j['position']
	print(targetPosition)
	tileArray = j['board']

	board = Board(tiles=tileArray)

	return board, tuple(targetPosition)
# board, targetPos = handleJson()
if True:
	# setup 1
	# board = Board(tiles=[[1, 1, 2],[3, 4, 5],[0, 1, 2],[3, 4, 5]])

	#setup 2
	board = Board(tiles=[[1,2,3],[5,4],[1,0,3],[0,4],[1,2,3],[5,4],[1,2,0],[5,4],[1,0,3]])

	# board = Board(tiles=[[1,1,0], [0,0,1], [0,1,0], [1, 1, 0]])

	# board = Board(width = 3, height = 9)
	# board = Board(5, [(1,2), (0,0)], [])
	# board = Board(5, [(1,1), (0,0), (0,1)], [], 3, 4)
	#
	# board = Board(5, [(1,2), (0,0)], [], 6, 10)
	# 2,7
	#
	# board = Board(5, width=5, height=15)
	# board.removeTile(1,3)
	# board.removeTile(1,4)
	# board.removeTile(3,9)
	# board.removeTile(3,10)
	# board.removeTile(3,5)
	# board.removeTile(1,10)
	# # board.removeTile(2, 3)
	# board.removeTile(2, 11)
	#
	# board = Board(width=3, height=9)
	# board.removeTile(2,5)
pOne = PlayerInfo(PenguinColor.white, 0)
pTwo = PlayerInfo(PenguinColor.red, 1)
pThree = PlayerInfo(PenguinColor.black, 2)
pFour = PlayerInfo(PenguinColor.brown, 3)
players = [pOne, pTwo, pThree, pFour]
gamestate = State(players, board)
# gamestate.placeAvatar(0,0,0)
# gamestate.placeAvatar(1,1,1)
# gamestate.placeAvatar(2,2,2)
# gamestate.placeAvatar(3,2,3)

# gamestate.placeAvatar(0, 1, 2)
# gamestate.placeAvatar(1, 0, 0)
# setup 2
gamestate.placeAvatar((1, 4))
gamestate.placeAvatar((0, 8))
gamestate.placeAvatar((0, 6))
gamestate.placeAvatar((1, 7))

gamestate.placeAvatar((0, 0))
gamestate.placeAvatar((2, 0))
gamestate.placeAvatar((1, 1))
gamestate.placeAvatar((2, 2))

# setup 1
# gamestate.placeAvatar(0, 2, 3)
# gamestate.placeAvatar(1, 1, 0)
# gamestate.placeAvatar(0, 1, 3)
# gamestate.placeAvatar(1, 2, 1)




# from xstate import stateToJson
# print(stateToJson(gamestate))

# gamestate.placeAvatar(0,0,1)




# p1 = Penguin(PenguinColor.black, 1, 1 )
# p2 = Penguin(PenguinColor.white, 0, 2 )
# p3 = Penguin(PenguinColor.brown, 0, 0 )
# p4 = Penguin(PenguinColor.red, 2, 2 )
# p12 = Penguin(PenguinColor.black, 2, 1 )
# window.setPenguins([p1,p2,p3,p4,p12])

App = QApplication(sys.argv)
window = FishGui(gamestate.getTiles())
# print("asking to set penguins")
window.setPenguins(gamestate.getPenguins())
# window.setReachableOrigin(targetPos[1], targetPos[0])
# print("asked to set penguins")

window.InitWindow() #TODO: does it make sense to move init window out of the init method? only way i can think to set tiles and the rachable/orgin arguments

# window.setTiles(board.getTiles())
# window.board.removeTile(2,3)
# board.removeTile(2,3)
window.scene.update()
sys.exit(App.exec())
