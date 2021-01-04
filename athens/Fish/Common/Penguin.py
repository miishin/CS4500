import enum

class PenguinColor(enum.Enum):
	red = "red"
	white = "white"
	brown = "brown"
	black = "black"

class Penguin:
	def __init__(self, color: PenguinColor, pos: tuple):
		self.posx = pos[0]
		self.posy = pos[1]
		self.color = color

	def getPos(self):
		"""
		Gets the position of this Penguin
		:return: Tuple  (x, y)
		"""
		return (self.posx, self.posy)

	def getColor(self):
		"""
		Gets the color associated with this Penguin
		:return: PenguinColor
		"""
		return self.color

	def setPos(self, pos):
		"""
		Changes the position values of a Penguin
		:param x: int the new x coordinate of a Penguin
		:param y: int the new y coordinate of a Penguin
		:return: None. Updates the posx and posy fields of this Penguin
		"""
		self.posx = pos[0]
		self.posy = pos[1]
