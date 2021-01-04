from board import Board
from Tile import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsItem, QGraphicsView, QStyleOptionGraphicsItem, QLabel
from PyQt5.QtGui import QPainter, QPen, QPolygon, QPainterPath, QBrush, QPolygonF, QMouseEvent, QColor, QImage
from PyQt5.QtCore import Qt, QPoint
from PyQt5 import QtSvg, QtGui
from PyQt5 import QtCore
import sys
import PIL
from PIL import Image, ImageQt, ImageDraw
# (left, upper, right, lower) = (20, 20, 100, 100)
# im = Image.open('pict_21.png')
# im = im.crop((left, upper, right, lower))
# im = im.convert('RGBA')
# png_info = im.info
# print(png_info)
# im.show()
import enum
from Penguin import *

tile_size = 50
xOffset = tile_size * 4
yOffset = tile_size
board_size = tile_size*3

points = [
	QPoint(0, board_size),
	QPoint(board_size, 0),
	QPoint(2 * board_size, 0),
	QPoint(3 * board_size, board_size),
	QPoint(2 * board_size, 2 * board_size),
	QPoint(board_size, 2 * board_size)
]
poly = QPolygon(points)

class FishScene(QGraphicsScene):
	def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
		print("hello")
		super(FishScene, self).mousePressEvent(event)
class FishView(QGraphicsView):
	# def mousePressEvent(self, event: 'QGraphicsViewMouseEvent') -> None:
	def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
		# clickPoint:  QPoint = QMouseEvent.pos()
		clickPoint = event.pos()
		# event.
		print("clicked")
		print(clickPoint)
		print(clickPoint.x()/tile_size, clickPoint.y()/tile_size)
		print("world")
		super(FishView, self).mousePressEvent(event)
class FishTile(QGraphicsItem):
	def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
		print("fasdkjfasjd")
		super(FishTile, self).mousePressEvent()


RED_PENGUIN = 'penguin_red.png'
BLACK_PENGUIN = 'penguin_black.png'
# BLACK_PENGUIN = 'penguinIconBlack.png'
# BLACK_PENGUIN = '/kirvin/Fish/Other/penguinIconBlack.png'
# BLACK_PENGUIN = '/kirvin/Fish/Other/penguinIconBlack.png'

BROWN_PENGUIN = 'penguin_brown.png'
WHITE_PENGUIN = 'penguin_white.png'


class FishGui(QMainWindow):
	def __init__(self, tileArray=[]):#, board):
		"""

		:param board: a Board object that represents that state of a game
		"""
		super().__init__()

		self.title = "Fish"
		# self.board = board
		# self.tileArray = self.board.tiles
		self.tileArray = tileArray
		self.straightLinesOrigin = (-1,-1)#(2,7)#(-1, -1)(0, 2)
		self.reachableFromOrigin = []#self.board.getReachableTiles(self.straightLinesOrigin[0], self.straightLinesOrigin[1])
		self.penguins = []
		#TODO: testing
		self.straightLinesOrigin = (3,4)
		self.reachableFromOrigin = Board.getReachableTilesInATileArray(tileArray, self.straightLinesOrigin[0], self.straightLinesOrigin[1], [penguin.getPos() for penguin in self.penguins])


		self.top = 150
		self.left = 150

		# self.width = (board.width)*tile_size*4 + tile_size
		# self.height = (board.height+1)*tile_size
		if len(self.tileArray) > 0:
			self.width = len(self.tileArray[0])*tile_size*4 + tile_size
			self.height = (len(self.tileArray)+1)*tile_size
		self.setBrushes()
		# self.InitWindow()

	def setBrushes(self):
		self.greenBrush = QBrush(Qt.green)
		self.grayBrush = QBrush(QColor(132, 238, 250))  # Qt.gray)
		self.cyanBrush = QBrush(QColor(2, 129, 165))  # Qt.cyan)
		self.darkCyanBrush = QBrush(QColor(3, 53, 62))
		self.lightCyanBrush = QBrush(QColor(106, 206, 217))
		self.redBrush = QBrush(QColor(193, 63, 61))  # Qt.red)
		self.pen = QPen(QColor(193, 63, 61))  # Qt.red)
		self.redPen = QPen(QColor(193, 63, 61))  # Qt.red)
		self.darkRedPen = QPen(Qt.darkRed)
		self.blackPen = QPen(Qt.black)

	def InitWindow(self):
		# self.width = len(self.tileArray[0])*tile_size*4 + tile_size
		# self.height = (len(self.tileArray)+1)*tile_size
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height*1)

		self.scene = QGraphicsScene()
		# self.scene = FishScene()
		self.createGraphicsView()

		self.show()
		# print("hello world")

	def setTiles(self, tiles):
		self.tileArray = tiles
		self.width = len(self.tileArray[0])*tile_size*4 + tile_size
		self.height = (len(self.tileArray)+1)*tile_size
	def setPenguins(self, penguins):
		self.penguins = penguins

	def setReachableOrigin(self, x, y):
		self.straightLinesOrigin = (x, y)
		self.setReachableTiles()
	def setReachableTiles(self):
		# self.reachableFromOrigin = reachableTiles
		self.reachableFromOrigin = Board.getReachableTilesInATileArray(self.tileArray, self.straightLinesOrigin[0], self.straightLinesOrigin[1], [penguin.getPos() for penguin in self.penguins])


	def getTileHexPoints(self, x, y):
		"""
		Creates the polygon point array that is mapped from a tile at position (x, y) in the game boards tile array
		:param x: The row of the board's tile array that contains the desired tile
		:param y: The index of the desired tile in tile row
		:return: a List of QPoint, representing the vertices of a hexagon
		"""
		xOff = xOffset
		yOff = yOffset
		shiftOff = 0
		if y%2 == 1:
			shiftOff = 2 * tile_size

		points = [
			QPoint(x*xOff + shiftOff, y*yOff+tile_size),
			QPoint(x*xOff+tile_size + shiftOff, y * yOff),
			QPoint(x*xOff + 2 * tile_size + shiftOff, y * yOff),
			QPoint(x*xOff + 3 * tile_size + shiftOff, y * yOff + tile_size),
			QPoint(x*xOff + 2 * tile_size + shiftOff, y * yOff +2 * tile_size),
			QPoint(x*xOff + tile_size + shiftOff, y * yOff + 2 * tile_size)
		]
		return points




	def drawFish(self, painter, tile):
		# painter.drawEllipse(tile[0].x(), tile[0].y(), 40, 20)
		painter.drawEllipse(tile[0].x(), tile[0].y(), tile_size, tile_size/2)

	def tileCoordinates(self, tile_array):
		tiles = []
		print(len(tile_array))
		print(len(tile_array[0]))
		for row in range(0, len(tile_array)):
			for tileInd in range(0, len(tile_array[row])):
				tilePoints = self.getTileHexPoints(row, tileInd)
				tiles.append(tilePoints)
		return tiles

	def mousePressEvent(self, QMouseEvent):
		clickPoint:  QPoint = QMouseEvent.pos()
		print("clicked")
		print(clickPoint)
		print(clickPoint.x()/tile_size, clickPoint.y()/tile_size)
		if poly.containsPoint(clickPoint, Qt.WindingFill):
			# self.reachableFromOrigin = self.board.getReachableTiles(self.straightLinesOrigin[0],
			#                                                         self.straightLinesOrigin[1])
			# self.tileArray = self.board.tiles

			# self.scene.update()
			# self.graphicsView.update()
			# self.update()
			self.scene.clear()
			self.createGraphicsView()

			# exit()
		else:
			pass
	def createGraphicsView(self):
		# self.scene = QGraphicsScene()
		# self.2, 149, 165

		# self.graphicsView = QGraphicsView(self.scene, self)
		self.graphicsView = FishView(self.scene, self)
		self.graphicsView.setBackgroundBrush(self.darkCyanBrush)
		self.graphicsView.setGeometry(0, self.height*0, self.width+tile_size*0, self.height+tile_size*0)
		self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		# self.shapes()

		self.drawTiles()
		tiles = []
		# tile_array = self.tileArray
		# for row in range(0, len(tile_array)):
		# 	for tileInd in range(0, len(tile_array[row])):
		# 		tilePoints = self.getTileHexPoints(tileInd, row)
		#
		# 		if type(tile_array[row][tileInd]) is Tile:
		# 			if (tileInd, row) in self.reachableFromOrigin:
		# 				tile = self.scene.addPolygon(QPolygonF(tilePoints), brush=self.lightCyanBrush)
		# 			elif (tileInd, row) == self.straightLinesOrigin:
		# 				tile = self.scene.addPolygon(QPolygonF(tilePoints), brush=self.grayBrush)
		# 			else:
		# 				tile = self.scene.addPolygon(QPolygonF(tilePoints), brush=self.cyanBrush)
		# 			tile.setFlag(QGraphicsItem.ItemIsSelectable)
		# 			tile.setFlag(QGraphicsItem.ItemIsMovable)
		# 			numFish = tile_array[row][tileInd].getFish()
		# 			self.drawFish(tile, numFish, tilePoints)

					# for fish in range(0, numFish):
					# 	tailX = tilePoints[1].x() + tile_size/3  - tile_size/3 * pow(-1, fish)
					# 	tailY = tilePoints[1].y() + fish * tile_size/2.5 + tile_size/12
					# 	triangleP = [QPoint(tailX,                  tailY +                  tile_size/16  ),
					# 	             QPoint(tailX,                  tailY + tile_size/10 +   tile_size/8  ),
					# 	             QPoint(tailX + tile_size/5,    tailY + tile_size/20 +   tile_size/12  )]
					# 	fish_body = self.scene.addEllipse(tailX + tile_size/10, tailY,
					# 	                                  tile_size/2, tile_size/4,
					# 	                                  pen=self.redPen, brush=self.redBrush)
					# 	fish_tail = self.scene.addPolygon(QPolygonF(triangleP), pen=self.redPen, brush=self.redBrush)
					# 	fish_body.setParentItem(tile)
					# 	fish_tail.setParentItem(fish_body)
					# 	# test = self.scene.addItem(pengQt)
	def drawTiles(self):
		tile_array = self.tileArray

		for row in range(0, len(tile_array)):
			for tileInd in range(0, len(tile_array[row])):
				tilePoints = self.getTileHexPoints(tileInd, row)

				if type(tile_array[row][tileInd]) is Tile:
					if (tileInd, row) in self.reachableFromOrigin:
						tile = self.scene.addPolygon(QPolygonF(tilePoints), brush=self.lightCyanBrush)
					elif (tileInd, row) == self.straightLinesOrigin:
						tile = self.scene.addPolygon(QPolygonF(tilePoints), brush=self.grayBrush)
					else:
						tile = self.scene.addPolygon(QPolygonF(tilePoints), brush=self.cyanBrush)
					# tile.
					# tile.mousePressEvent(QMouseEvent(windowPos=))
					# tile.isSelected().co
					# tile.setData(0, tileInd)
					# tile.setData(1, row)
					# tile.setFlag(QGraphicsItem.ItemIsPanel)
					# tile.setBrush(self.greenBrush)
					# print(tile.data(0))

					tile.setFlag(QGraphicsItem.ItemIsSelectable)
					# tile.setFlag(QGraphicsItem.ItemIsMovable)
					numFish = tile_array[row][tileInd].getFish()
					self.drawFish(tile, numFish, tilePoints)
					###
					# print(self.penguins)
					print([penguin.getPos() for penguin in self.penguins], (row, tileInd))
					for penguin in self.penguins:
						if (tileInd, row) == penguin.getPos():
						# if (row, tileInd) == penguin.getPos():
							self.drawPenguin(tilePoints[1].x(), tilePoints[1].y(), penguin.getColor())
					# if (row, tileInd) in [penguin.getPos() for penguin in self.penguins]:
					#
					# 	print("alsdkf")
					# 	self.drawPenguin(tilePoints[1].x(), tilePoints[1].y())


		# self.asdfalj()

	def drawFish(self, tile, numFish, tilePoints):
		for fish in range(0, numFish):
			tailX = tilePoints[1].x() + tile_size / 3 - tile_size / 3 * pow(-1, fish)
			tailY = tilePoints[1].y() + fish * tile_size / 2.5 + tile_size / 12
			triangleP = [QPoint(tailX, tailY + tile_size / 16),
			             QPoint(tailX, tailY + tile_size / 10 + tile_size / 8),
			             QPoint(tailX + tile_size / 5, tailY + tile_size / 20 + tile_size / 12)]
			fish_body = self.scene.addEllipse(tailX + tile_size / 10, tailY,
			                                  tile_size / 2, tile_size / 4,
			                                  pen=self.redPen, brush=self.redBrush)
			fish_tail = self.scene.addPolygon(QPolygonF(triangleP), pen=self.redPen, brush=self.redBrush)
			fish_body.setParentItem(tile)
			fish_tail.setParentItem(fish_body)
			# test = self.scene.addItem(pengQt)

	def drawPenguin(self, x, y, color):
		label_Image = QLabel(self.graphicsView)
		# image_path = 'pict_21.png'  # path to your image file
		# if color == Peng
		# image_path = Avatars.BLACK
		# image_path = Avatars.color
		if color == PenguinColor.brown:
			image_path = BROWN_PENGUIN
		elif color == PenguinColor.black:
			image_path = BLACK_PENGUIN
		elif color == PenguinColor.red:
			image_path = RED_PENGUIN
		elif color == PenguinColor.white:
			image_path = WHITE_PENGUIN

		image_profile = QImage(image_path)  # QImage object
		image_profile = image_profile.scaled(tile_size*3, tile_size*2, aspectRatioMode=QtCore.Qt.KeepAspectRatio,
		                                     transformMode=QtCore.Qt.SmoothTransformation)  # To scale image for example and keep its Aspect Ration
		# image_profile = image_profile.setColor(QColo, QColor.cyan())


		# label_Image.setGeometry(200,200,tile_size*3,tile_size*2)
		# label_Image.setGeometry(200,200,tile_size*3,tile_size*2)
		# print(x,y)
		# label_Image.move(x, y)
		label_Image.move(x+tile_size/7, y-tile_size/7)
		# label_Image.move(x+xOffset+tile_size, y+tile_size)
		label_Image.setPixmap(QtGui.QPixmap.fromImage(image_profile))

	# self.graphicsView.setSceneRect(0,0, self.scene.width(), self.scene.height())
	def asdfalj(self, x=0,  y=0):
		# label_Image = QtGui.QLabel(frame)
		label_Image = QLabel(self.graphicsView)
		image_path = 'pict_21.png'  # path to your image file
		# image_path = 'penguinIconBlack.png'  # path to your image file
		# label_Image.setGeometry(self.width,self.height,self.width,self.height)
		# label_Image.setGeometry(self.graphicsView.width(),self.graphicsView.height(),100,100)
		# label_Image.setGeometry(0,0,tile_size*3,tile_size*2)
		# label_Image.setGeometry(self.width/2,self.height/2,tile_size*3,tile_size*2)
		# label_Image.setGeometry(self.width/2,self.height/2,board_size*3,board_size*2)
		# label_Image.setAlignment(Qt_Alignment=Qt.LeftEdge)



		# image_profile = QtGui.QImage(image_path)  # QImage object
		image_profile = QImage(image_path)  # QImage object
		image_profile = image_profile.scaled(tile_size*3, tile_size*2, aspectRatioMode=QtCore.Qt.KeepAspectRatio,
		                                     transformMode=QtCore.Qt.SmoothTransformation)  # To scale image for example and keep its Aspect Ration
		# label_Image.setGeometry(200,200,tile_size*3,tile_size*2)
		# label_Image.setGeometry(200,200,tile_size*3,tile_size*2)
		print(x,y)
		label_Image.move(x, y)
		label_Image.setPixmap(QtGui.QPixmap.fromImage(image_profile))

	def shapes(self):
		# ellipse = self.scene.addEllipse(20, 20, 200, 200, self.pen, self.greenBrush)

		# ellipse = self.scene.addEllipse(20, 20, 40, 30)
		# rect = self.scene.addRect(-100, -100, 40, 40, self.pen, self.grayBrush)

		# ellipse.setParentItem(rect)
		painter = QPainter(self)
		# a = QStyleOptionGraphicsItem()
		# painter.setPen(QPen(Qt.red, 4, Qt.SolidLine))
		# painter.drawPolygon(points)
		# painter.drawPolygon(poly)
		# poly2 = QPolygon(points2)
		# painter.drawPolygon(poly2)
		# ellipse.paint(painter, a)

	# def paintEvent(self, event):
	# 	painter = QPainter(self)
	# 	painter.setPen(QPen(Qt.red, 4, Qt.SolidLine))
	# 	#painter.drawPolygon(poly)
	# 	# tiles = self.tileCoordinates(self.board.tiles)
	# 	tiles = self.board.tiles
	# 	# painter.drawPolygon(poly)
	# 	self.paintTileCoordinates(tiles, painter)

	# def paintTileCoordinates(self, tile_array, painter):
	# 	"""
	# 	Iteratively draws each tile in the board's tile array onto the gui
	# 	:param tile_array: a list of list of Tile that represents a game board's tiles
	# 	:param painter:
	# 	:return: None. Draws the game tiles and fish onto the game board
	# 	"""
	# 	tiles = []
	# 	# print(len(tile_array))
	# 	# print(len(tile_array[0]))
	# 	for row in range(0, len(tile_array)):
	# 		for tileInd in range(0, len(tile_array[row])):
	#
	# 			tilePoints = self.getTileHexPoints(row, tileInd)
	# 			tilePoly = QPolygon(tilePoints)
	#
	# 			if type(tile_array[row][tileInd]) is Tile:
	# 				# (255, 153, 51)
	# 				painter.setBrush(QBrush(Qt.cyan, Qt.SolidPattern))
	# 				painter.setPen(Qt.black)
	# 				painter.drawPolygon(tilePoly)
	# 				# self.scene.addPolygon(QPolygonF(tilePoints))
	# 				numFish = tile_array[row][tileInd].getFish()
	# 				painter.setPen(Qt.darkGreen)
	# 				painter.setBrush(QBrush(Qt.darkGreen, Qt.SolidPattern))
	# 				for fish in range(0, numFish):
	# 					triangleP = [QPoint(tilePoints[1].x() ,             tilePoints[1].y() +                fish*tile_size/2.5 + tile_size/16),
	# 					             QPoint(tilePoints[1].x(),              tilePoints[1].y() + tile_size/10 + fish*tile_size/2.5 + tile_size/8),
	# 					             QPoint(tilePoints[1].x()+tile_size/5, tilePoints[1].y() + tile_size/20 + fish*tile_size/2.5 + tile_size/12)]
	# 					painter.drawPolygon(QPolygon(triangleP))
	# 					painter.drawEllipse(tilePoints[1].x()+tile_size/10, tilePoints[1].y() +fish*tile_size/2.5, tile_size/2, tile_size/4)
	# 				# self.scene.addEllipse(tilePoints[1].x()+tile_size/10, tilePoints[1].y() +fish*tile_size/2.5, tile_size/2, tile_size/4)
	# 				# self.scene.addPolygon(QPolygonF(triangleP))
	#
	# 				# self.createGraphicsView()


# App = QApplication(sys.argv)
# # board = Board()
# board = Board(5, [(1,1), (0,0),(0,1)],[], 3, 4)
# window = FishGui(board)
# # window.
# sys.exit(App.exec())
