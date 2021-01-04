import math
from state import State
from game_tree import GameTree, GameNode

"""
The strategy class contains algorithms that a player can use to perform either a placement
or a movement turn.
"""


class Strategy:


		@staticmethod
		def getAvailablePlacement(gameState: State):
			tiles = gameState.getTiles()
			penguinPositions = gameState.getAllPenguinPositions()
			for y in range(0,len(tiles)):
				for x in range(0, len(tiles[y])):
					if (x, y) in penguinPositions:
						pass
					elif 0 <= x < len(tiles[0]) and 0 <= y < len(tiles) and tiles[y][x].getFish() == 0:
						pass
					else:
						return (x,y)

		@staticmethod
		def penguinPlacement(gameState: State):
			place = Strategy.getAvailablePlacement(gameState)
			if not place:
				return False
			gameState.placeAvatar(place)
			return gameState


		@staticmethod
		def penguinMovement(gamestate: State, depth: int):
			"""
			Performs the minimax strategy and applies the resulting move to a state
			:param gamestate: the current state of the game
			:param depth: how deep to search in a tree when performing minimax
			:return: the updated state of the game
			"""
			gameTree = GameTree(gamestate)
			move = Strategy.minimax(gameTree, depth)
			return gameTree.applyAction(gameTree.root, move).state

		@staticmethod
		def minimax(gameTree: GameTree, depth: int, state=None):
			"""
			Starting point for the minimax algorithm
			Returns None if no movement is found
			:param gameTree: a game tree containing the current state of the game in its root node
			:param depth: how deep to search in a tree
			:return: a movement or None
			"""
			if state is not None and state.allPossibleActions() == []:
				return False
			max = -math.inf
			action = None
			sortedMoves = gameTree.root.getAvailableMoves()
			# print(sortedMoves)
			if sortedMoves != [()]:
				sortedMoves.sort(key=Strategy._getMovementSortKey)
			# print("sorted moves", sortedMoves)

			for move in sortedMoves:
				val = Strategy._min_value(gameTree, gameTree.applyAction(gameTree.root, move), 1, depth - 1)
				# print("val", val, "move", move, "gametree turn", gameTree.root.getGameState().turn, "best action", action)
				if val > max:
					max = val
					action = move
			return action



		@staticmethod
		def _min_value(tree: GameTree, node: GameNode, ageInd, depth):
			totalPlayerFish = node.getGameState().players[0].getFish()
			if node.getGameState().gameOver():
				return totalPlayerFish
			if depth <= 0:
				return totalPlayerFish
			if len(node.getAvailableMoves()) == 0:
				return totalPlayerFish
			v = math.inf
			nextAgent = (ageInd + 1) % len(node.getGameState().players)
			for a in node.getAvailableMoves():
				if nextAgent == 0:
					v = min(v, Strategy._max_value(tree, tree.applyAction(node, a), nextAgent, depth - 1))
				else:
					v = min(v, Strategy._min_value(tree, tree.applyAction(node, a), nextAgent, depth))
			return v


		@staticmethod
		def _max_value(tree: GameTree, node: GameNode, ageInd, depth):
			totalPlayerFish = node.getGameState().players[0].getFish()
			if node.getGameState().gameOver():
				return totalPlayerFish
			if depth < 0:
				return totalPlayerFish
			if len(node.getAvailableMoves()) == 0:
				return totalPlayerFish
			v = -math.inf
			nextAgent = (ageInd + 1) % len(node.getGameState().players)
			for a in node.getAvailableMoves():
				if nextAgent == 0:
					v = max(v, Strategy._max_value(tree, tree.applyAction(node, a), nextAgent, depth - 1))
				else:
					v = max(v, Strategy._min_value(tree, tree.applyAction(node, a), nextAgent, depth))
			return v

		@staticmethod
		def _getMovementSortKey(move):
			"""
			Used to help sort a list of movements by the first y value of the tuple
			:param move: a movement
			:return: int the from y value of a tuple
			"""
			return (move[0][1] + 1)*100 + (move[0][0] + 1)*10 + (move[1][1] + 1) * 5 + move[1][0]
			# return move[0][1]



