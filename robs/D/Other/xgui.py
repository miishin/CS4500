from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QPolygon
from PyQt5.QtCore import Qt, QPoint

import sys

size = sys.argv[1]
if not size.isnumeric():
    print("Error: not postive int")
    print("usage: ./xgui positive-integer")
    quit()
else:
    size = int(size)
    if size < 1:
        print("Error: not postive int")
        print("usage: ./xgui positive-integer")
        quit()


points = [
    QPoint(0, size),
    QPoint(size, 0),
    QPoint(2 * size, 0),
    QPoint(3 * size, size),
    QPoint(2 * size, 2 * size),
    QPoint(size, 2 * size)
]
poly = QPolygon(points)

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title= "D"
        self.top= 150
        self.left= 150
        self.width= 3*size
        self.height= 2*size
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 4, Qt.SolidLine))
        painter.drawPolygon(poly)

    def mousePressEvent(self, QMouseEvent):
        clickPoint = QMouseEvent.pos()
        if poly.containsPoint(clickPoint, Qt.WindingFill):
            exit()
        else:
            pass


App = QApplication(sys.argv)
window = window()
sys.exit(App.exec())
