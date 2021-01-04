import json
import enum
class Request(enum.Enum):
	"""
	A Request identifies the type of message being sent between a user and a referee, enabling
	the receiver to handle the message's data properly
	"""
	Join = "Join"
	PlaceAvatar = "PlaceAvatar"
	MoveAvatar = "MoveAvatar"

class PlayerInterface:
	def __init__(self, age, name):
		"""
		This PlayerInterface object allows a player create, send, and recieve Json request needed to
		communicate with a referee
		:param age: int the age of the player
		:param name: string the name of the player
		"""
		self.age = age
		self.ID = name

	def sendRequest(self, requestDict):
		"""
		Converts a dictionary to a Json Request and sends it to the referee
		:param requestDict: Dict a dictionary containing a Request field, and other relevant information fields
		"""
		json.dumps(requestDict)
		#TODO: send data to referee
		pass


	def joinGame(self):
		"""
		Sends a request to join a new game of Fish
		:return:
		"""
		joinRequest = {"Request": Request.Join, "ID":self.ID, "age":self.age}
		self.sendRequest(joinRequest)

	def listenForReferee(self):
		"""
		Listens for the referee to send instructions and game State information
		:return:
		"""
		#TODO: connect to referee and recieve incoming data
		pass

	def placeAvatar(self, y: int, x: int):
		"""
		Sends a request to place an avatar at the location specified by the given y, and x coordinates
		:param y: int Y coordinate of the tile to place an avatar on
		:param x: int X coordinate of the tile to place an avatar on
		:return:
		"""
		placeAvatarRequest = {"Request":Request.PlaceAvatar, "Y":y, "X":x}
		self.sendRequest(placeAvatarRequest)

	def moveAvatar(self, fromY: int, fromX: int, toY: int, toX: int):
		"""
		Sends a request to move an one of your avatars, determined by the fromY, fromX coordinate, to the tile specified
		by the toY, toX coordinates
		:param fromY: int Y coordinate of the avatar a player wishes to move
		:param fromX: int X coordinate of the avatar a player wishes to move
		:param toY: int Y coordinate a player wishes to move their avatar to
		:param toX: int X coordinate a player wishes to move their avatar to
		:return:
		"""
		moveAvatarRequest = {"Request": Request.MoveAvatar, "fromY":fromY, "fromX":fromX, "toY":toY, "toX":toX}
		self.sendRequest(moveAvatarRequest)

