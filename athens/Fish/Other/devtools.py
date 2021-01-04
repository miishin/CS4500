from Tile import Tile, NoTile
from board import Board
from state import State
from game_tree import GameTree, GameNode
from Penguin import Penguin, PenguinColor
from PlayerInfo import PlayerInfo
"""
DevTools contains functions to assist in debugging code and visualizing different
aspects of a game
These functions are meant to be used in for testing purposes only and should not be pushed in
any actual solutions
"""
def sampleState1():
	p1 = PlayerInfo(PenguinColor.black, 0)
	p2 = PlayerInfo(PenguinColor.brown, 1)
	p3 = PlayerInfo(PenguinColor.white, 2)
	p4 = PlayerInfo(PenguinColor.red, 3)
	gs = State([p1, p2, p3, p4], board=Board())
	gs.placeAvatar((0, 0))
	gs.placeAvatar((1, 0))
	gs.placeAvatar((2, 0))
	gs.placeAvatar((0, 3))
	# print(gs.getAllPenguinPositions())
	return gs

def sampleState2():
	tileArr = [
		[0,5,5,3],
		[1,2,3,4],
		[3,0,0,2],
		[1,1,1,1],
		[0,5,5,0]
	]
	p1 = PlayerInfo(PenguinColor.black, 0)
	p2 = PlayerInfo(PenguinColor.brown, 1)
	p3 = PlayerInfo(PenguinColor.red, 2)
	p4 = PlayerInfo(PenguinColor.white, 3)
	gs = State([p1, p2, p3, p4], board=Board(tiles=tileArr))
	gs.placeAvatar((0, 0))
	gs.placeAvatar((2, 2))
	gs.placeAvatar((2, 4))
	gs.placeAvatar((3, 2))
	return gs

def sampleTree1():
	return GameTree(sampleState1())

class DevTools:



	@staticmethod
	def tileToIntArray(tileArray):
		"""
		Converts an array of Tiles to an array of integers. (Integers can be printed, Tiles cannot)
		:param tileArray: List of List of Tile
		:return: List of List of Integer
				where each Integer is a value from between 0 and 5, representing the amount of fish in a tile
		"""
		return [[tile.getFish() for tile in row] for row in tileArray]

	# represent State as JSON
	# State is:
	# {"players": Player*,
	# "board": Board}
	# Player* is [Player, ..., Player]
	# State -> JSON
	@staticmethod
	def returnJSON(gamestate):
		jsonState = {"players": [], "board": []}
		for player in gamestate.players:
			jsonState["players"].append(player.returnJSON())
		jsonState["board"] = DevTools.tileToIntArray(gamestate.board.tiles)

		return jsonState

	@staticmethod
	def visualizeState(gameState: State):
		"""
		Prints an ascii diagram representing a game State.
			Players are represented on the board as the letters R (red), B (black), W (white), and O (brown)
			the numbers in a tile represent the amount of fish in a tile
		:param gameState: State the state of the game to be printed
		:return: None, prints a dagram to stdout

		The printed output will look somehting like this:
			  /W5\__/--\
			  \__/R3\__/-2\
			  /  \__/  \__
		"""

		def printRow(row, rowInt, penguins, gameState: State):
			if rowInt%2 == 1:
				rowStr = "\\__"
			else:
				rowStr = ""
			x = 0
			for fishNum in row:
				if fishNum  == 0:
					rowStr += "    __"
				else:
					if (x, rowInt) in penguins:
						rowStr +=  "/{color}{fish}\\__".format(color=colors[gameState.getColorOfPenguinAtPosition((x, rowInt))], fish=fishNum)
					else:
						rowStr += "/-{fish}\\__".format(fish=fishNum)
				x+=1
			# rowStr=rowStr[:-2]
			print(rowStr)
			# return rowStr

		penguins = gameState.getAllPenguinPositions()
		tiles = DevTools.tileToIntArray(gameState.getTiles())
		colors = {PenguinColor.red: "R", PenguinColor.black: "B", PenguinColor.brown:"O", PenguinColor.white: "W"}

		for y in range(0, len(tiles)):
			printRow(tiles[y], y, penguins, gameState)
		if len(tiles)%2 == 0:
			bottomRow = "   "
		else:
			bottomRow = ""
		for x in range(0, len(tiles[0])):
			bottomRow += "\\__/  "

		print(bottomRow)



	@staticmethod
	def visualizeTree(tree: GameTree):
		"""
		Creates a one layer deep tree based off of the current state of the game
			Prints out the state of a game before a player makes a move, then
			prints out all resulting states reachable by valid Movement for the current
			state's Player turn
		:param tree: GameTree a tree containing the current state of a game as its root node
		:return: None, prints diagrams to stdout
		"""
		DevTools.visualizeState(tree.root.state)
		tree.root.generateChildren()
		print ("____________________", len(tree.root.children))
		for action in tree.root.getAvailableMoves():
			print(action)
			DevTools.visualizeState(tree.root.getNextNode(action).state)
			print("\n")
		pass

# DevTools.visualizeState(sampleState1())
# print("\n\n")
# DevTools.visualizeState(sampleState2())
# print("\n\n")
# DevTools.visualizeTree(sampleTree1())
