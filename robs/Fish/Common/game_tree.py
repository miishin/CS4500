from state import State

"""
This file contains our representation of a game tree

A GameTree contains a root node that begins a tree
INTERPRETATION: A root node contains a state where all penguins have been placed on a board already



A Gamenode contains a state, a list of valid actions for a player who has the turn in the state, and a mapping to all 
child nodes directly reachable from the state

list of valid actions includes any Movements that any penguins of the player who has the current turn can make. 
INTERPRETATION: a Movement is a tuple of tuples, where the first tuple specifies a location where an Penguin exists,
                    and the second tuple specifies where the Penguin is moving to. ((fromX, fromY), (toX, toY))
                    
children are stored in a map from valid Movements to GamesNodes
INTERPRETATION: A dictionary that maps each item from the list of valid actions (Movements), to the GameNode that
                 contains the state that results from applying that movement to the current node's state.
                 In the event that a player has no available moves, a single child entry will point to the node
                 containing the state where the next player has a turn.
                 
The game tree will check its state for if the game is over. In the event that the game is over, and no players have
any remaining moves, the node will have no child nodes.
"""


class GameNode:
	"""
	A GameNode is a wrapper for a game state that allows it to be used as a node in a tree structure
	:param state a single game-state of a Fish game where all penguins have been placed on the board
	"""
	def __init__(self, state: State):
		self.state = state
		"""
		while( not self.state.gameOver() and self.state.allPossibleActions() == []):
			# print("state:   ->   ", self.state)
			self.state.nextTurn()"""
		self.children = {}
		self.availableActions = []
		for penguin in self.state.players[self.state.turn].getPenguins():
			for reachableTile in self.state.getReachableTiles(penguin.getPos()[0], penguin.getPos()[1]):
				self.availableActions.append((penguin.getPos(), reachableTile))
		if not self.availableActions:
			self.availableActions.append(())

	def getGameState(self) -> State:
		"""
		Gives a copy of the state
		:return: state
		"""
		return self.state.copy()

	def getAvailableMoves(self):
		"""
		Gets a list of all valid movements that the player of the current turn can make
		:return: List of movements
		"""
		return self.availableActions

	def getNextState(self, move):
		"""
		Gets the resulting state of a board following a valid move
			the node uses its game state to determine who the turn belongs to
		:param Movment specifies the penguins starting and end location
		:raises Exception "Invalid Move"
		:return: GameNode the GameNode resulting from a
		"""
		if move in self.availableActions:
			nextState = self.state.copy()
			nextState.movePenguin(move)
			nextNode = GameNode(nextState)
			return nextNode
		else:
			raise Exception("Invalid Move")

	def getNextNode(self, move):
		"""
		Gets the child node of this node connected by the edge specified by move
		:param move: specifies the penguins starting and end location
		:return: GameNode the GameNode resulting from moveing down the edge of the tree indicated by the move
		"""
		if len(self.children) == 0 and not self.state.gameOver():
			self.generateChildren()
		return self.children[move]

	def generateChildren(self):
		"""

		:return:
		"""
		if self.state.gameOver():
			return
		for move in self.availableActions:
			nextState = self.state.copy()
			nextState.movePenguin(move)
			nextNode = GameNode(nextState)
			self.children[move] = nextNode

class GameTree:
	def __init__(self, state: State):
		"""
		A Game is a tree starting with a root GameNode who's state has all Penguins of all Players placed already
		:param state: The state of the root GameNode of a game tree
		"""
		self.root = GameNode(state)

	def applyAction(self, node: GameNode, action):
		"""
		Gets the child GameNode that results from an action being perfomed on a given GameNode
		:param node: GameNode The node that we wish to apply an action to
		:param action: A Movement indicating the change that takes the current node to the child node
		:return: GameNode the child GameNode resulting from applying a movement to a given GameNode.
					False if no resulting child node exists
		"""

		try:
			next_node = node.getNextNode(action)
		except:
			#print("Invalid Movement, cannot apply action: ", action)
			#print("StatesInfo", [(player.getColor().value, penguin.getPos()) for player in node.state.players for penguin in player.getPenguins()])
			next_node = False
		return next_node

	def applyFunction(self, node: GameNode, func):
		"""
		Applies an a function to all of the child GameNodes of a given GameNode, collects the outputs in a list
		:param node: GameNode the node who's children the given function is applied to
		:param func: A funtion object with the signature func(GameNode)
		:return: List of <Output>, where <Output> is left up to the function creator
		"""
		results = []
		for move in node.availableActions:
			child = node.getNextState(move)
			try:
				result = (move, func(child))
			except:
				raise Exception("bad function")
			results.append(result)
		return results
