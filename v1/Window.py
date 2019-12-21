from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import time
from Stage import *

class Window(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.mapTest = Stage(0)
        self.setScene(self.mapTest.displayScene)
        self.inGame = False

        """
        self.testLayout = QGridLayout()
        self.testLayout.addWidget(self.StageTest,0,0)
        self.mainLayout = QGridLayout()
        self.mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.mainLayout.addLayout(self.testLayout, 0, 0)
        self.sucessImg = QPixmap("success.jpg")
        self.setLayout(self.mainLayout)
        """

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
        elif key == Qt.Key_R:
            self.mapTest.reset()
        else:
            print(key)


    def success(self):
        pass

    def arrowTest(self,dx,dy):
        self.mapTest.move(dx,dy)
        print(self.mapTest.display())
        time.sleep(0.1)
        if self.mapTest.gameSuccess:
            print('success')
            self.success()
