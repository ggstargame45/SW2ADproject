from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import time
from Tile import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.mapTest = Tiles()
        self.StageTest = QTextEdit()
        self.StageTest.setReadOnly(True)
        self.StageTest.setAlignment(Qt.AlignCenter)

        self.testLayout = QGridLayout()
        self.testLayout.addWidget(self.StageTest,0,0)
        self.mainLayout = QGridLayout()
        self.mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.mainLayout.addLayout(self.testLayout, 0, 0)

        self.setLayout(self.mainLayout)
        self.StageTest.setPlaceholderText(self.mapTest.display())

    def keyPressEvent(self, QKeyEvent):
        key = QKeyEvent.key()
        if key == Qt.Key_Up:
            print("Up")
            self.arrowTest(0,-1)
        elif key == Qt.Key_Down:
            print("Down")
            self.arrowTest(0,1)
        elif key == Qt.Key_Right:
            print("Right")
            self.arrowTest(1,0)
        elif key == Qt.Key_Left:
            print("Left")
            self.arrowTest(-1,0)

        elif key == Qt.Key_Enter or key == Qt.Key_Return:
            print("Enter")
            print(self.mapTest.display())

        elif key == Qt.Key_D:
            print("Right")
            self.arrowTest(1,0)
        elif key == Qt.Key_W:
            print("Up")
            self.arrowTest(0,-1)
        elif key == Qt.Key_A:
            print("Left")
            self.arrowTest(-1,0)
        elif key == Qt.Key_S:
            print("Down")
            self.arrowTest(0,1)
        else:
            print(key)

    def arrowTest(self,dx,dy):
        self.mapTest.move(dx,dy)
        self.StageTest.setPlaceholderText(self.mapTest.display())
        time.sleep(0.1)
