from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Tile import *
from Process import *
import sys


class menu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.gameWindow = QTextEdit()
        self.gameWindow.setReadOnly(True)
        self.gameWindow.setAlignment(Qt.AlignLeft)

        gameLayout = QGridLayout()
        gameLayout.addWidget(self.gameWindow, 0, 0)
        menuLayout = QGridLayout()

        self.level = QComboBox()
        self.level.addItem('stage1')
        self.level.addItem('stage2')
        self.level.addItem('stage3')
        self.level.setCurrentIndex(0)
        menuLayout.addWidget(self.level, 0, 2)


        self.ruleButton = QToolButton()
        self.ruleButton.setText('rule')
        self.ruleButton.clicked.connect(self.ruleClicked)
        menuLayout.addWidget(self.ruleButton, 0, 1)


        self.escButton = QToolButton()
        self.escButton.setText('exit')
        self.escButton.clicked.connect(self.escGame)
        menuLayout.addWidget(self.escButton, 0, 4)

        self.newGameButton = QToolButton()
        self.newGameButton.setText('start')
        self.newGameButton.clicked.connect(self.startGame)
        menuLayout.addWidget(self.newGameButton, 0, 3)

        mainLayout = QGridLayout()
        mainLayout.addLayout(gameLayout, 0, 0)
        mainLayout.addLayout(menuLayout, 1, 0)
        self.setLayout(mainLayout)
        self.setWindowTitle('pushpush')




    def ruleClicked(self):
        self.gameWindow.setPlaceholderText(

"""
 ‿︵‿︵‿ヽ(゜□゜ )ノ︵‿︵‿
**************************
공을 밀어서 집에 넣어주세요!
**************************          
공을 움직이다 벽에 붙어버리면 
더 이상 움직일 수 없습니다
**************************
        """)

    def startGame(self):
        pass
        #self.map.gameStart(self.level.currentIndex())



    def escGame(self,QCloseEvent):
        ans = QMessageBox.question(self,"종료확인","종료하시겠습니까?",QMessageBox.No| QMessageBox.Yes)
        if ans == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = menu()
    a.show()
    sys.exit(app.exec())