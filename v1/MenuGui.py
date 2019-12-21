from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Tile import *
import sys
import pymysql


class menu(QWidget):
    stageList = [["stage1","stage2","stage3"]]

    def __init__(self):
        super().__init__()
        self.initUI()
        self.conn = pymysql.connect(host='localhost',user='root',password='devourstats@',db='pushgame',charset='utf8')

    def initUI(self):
        self.setGeometry(800,300,200,200)

        self.gameWindow = QTextEdit()
        self.gameWindow.setReadOnly(True)
        self.gameWindow.setAlignment(Qt.AlignLeft)

        gameLayout = QGridLayout()
        gameLayout.addWidget(self.gameWindow, 0, 0)
        menuLayout = QGridLayout()

        #self.worldBox = QComboBox

        self.stageBox = QComboBox()
        self.stageBox.addItem('stage1')
        self.stageBox.addItem('stage2')
        self.stageBox.addItem('stage3')
        self.stageBox.setCurrentIndex(0)
        menuLayout.addWidget(self.stageBox, 0, 2)

        self.stageBox.currentIndexChanged.connect(self.stageClicked)

        self.ruleButton = QToolButton()
        self.ruleButton.setText('rule')
        self.ruleButton.clicked.connect(self.ruleClicked)
        menuLayout.addWidget(self.ruleButton, 0, 1)

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
        ruleBox = QMessageBox()
        ruleBox.setWindowTitle("설명")
        ruleBox.setText("""
 ‿︵‿︵‿ヽ(゜□゜ )ノ︵‿︵‿
****************************************************
빨간색 플레이어를 이동시켜 갈색 상자를 밀어서
회색 상자를 채워 모두 노란색으로 만들어요!
****************************************************
adws를 눌러 플레이어를 각각
왼쪽,오른쪽,위쪽,아래쪽으로 이동 시킬 수 있어요!
****************************************************
공을 움직이다 벽에 붙어버리면
더 이상 움직일 수 없습니다
**************************
        """)
        ruleBox.exec()

    def startGame(self):
        self.close()
        pass
        #self.map.gameStart(self.level.currentIndex())

    def worldSelected(self):
        pass
    def stageClicked(self):
        curs = self.conn.cursor()
        curs.execute("select * from records")
        rows = curs.fetchall()
        n = self.stageBox.currentIndex()
        self.gameWindow.setPlaceholderText(f'스테이지 {n+1}의 기록 : {rows[n][3]}초')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = menu()
    a.show()
    sys.exit(app.exec())
