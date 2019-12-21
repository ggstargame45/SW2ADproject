from Tile import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time


class Stage(object):
    """
    맵과 구성요소들의 상호작용을 다룬다
    """
    def __init__(self, n):
        self.backLeft = QPixmap("Playerimg/BL.png").scaled(QSize(50,50))
        self.backRight = QPixmap("Playerimg/BR.png").scaled(QSize(50,50))
        self.frontLeft = QPixmap("Playerimg/FL.png").scaled(QSize(50,50))
        self.frontRight = QPixmap("Playerimg/FR.png").scaled(QSize(50,50))
        self.leftLeft = QPixmap("Playerimg/LL.png").scaled(QSize(50,50))
        self.leftRight = QPixmap("Playerimg/LR.png").scaled(QSize(50,50))
        self.rightLeft = QPixmap("Playerimg/RL.png").scaled(QSize(50,50))
        self.rightRight = QPixmap("Playerimg/RR.png").scaled(QSize(50,50))
        """
        음수는 무조건 막히는 타일
        -1=벽
        0=빈공간
        1~20는 플레이어와 플레이어+타일
        1=플레이어 2=플레이어+집 3=플레이어+빙판
        21~40대는 박스와 박스+타일
        21=박스 22=박스+집 23=박스+빙판
        41~은 단일 타일들
        41=집 42=빙판
        """
        self.gameSuccess = False
        self.stagenum = n
        self.tileObject = Tiles()
        self.tile = self.tileObject.mapStorage[self.stagenum]
        self.playerRowPos, self.playerColumnPos = self.tileObject.playerPosStorage[self.stagenum][0],self.tileObject.playerPosStorage[self.stagenum][1]
        self.tile=np.array(self.tile)
        self.displayScene = QGraphicsScene()
        self.displayimage = [[QGraphicsRectItem(p*50,i*50,50,50) for p in range(len(self.tile[i]))] for i in range(len(self.tile))]

        self._wallBrush = QBrush(Qt.GlobalColor.black)
        #self._playerBrush = QBrush(Qt.GlobalColor.red)
        self._boxBrush = QBrush(Qt.GlobalColor.darkRed)
        self._blankBrush = QBrush(Qt.GlobalColor.white)
        self._iceBrush = QBrush(Qt.GlobalColor.blue)
        self._houseBrush = QBrush(Qt.GlobalColor.gray)
        self._fillBrush = QBrush(Qt.GlobalColor.yellow)
        for m in range(len(self.tile)):
            for n in range(len(self.tile[m])):
                self.imgConvert(m,n,self.tile[m][n])

        for m in self.displayimage:
            for n in m:
                self.displayScene.addItem(n)

        self.playerRightpose = True
        self.playeritem = self.displayScene.addPixmap(self.frontRight)
        self.playerdisplaypos()
        self.starttime = time.time()

    def imgConvert(self,row,col,type):
        if type ==-1:
            self.displayimage[row][col].setBrush(self._wallBrush)
        elif type ==0:
            self.displayimage[row][col].setBrush(self._blankBrush)
        elif type ==1:
            self.displayimage[row][col].setBrush(self._blankBrush)
        elif type ==2:
            self.displayimage[row][col].setBrush(self._houseBrush)
        elif type ==3:
            self.displayimage[row][col].setBrush(self._iceBrush)
        elif type == 21:
            self.displayimage[row][col].setBrush(self._boxBrush)
        elif type == 22:
            self.displayimage[row][col].setBrush(self._fillBrush)
        elif type == 23:
            self.displayimage[row][col].setBrush(self._boxBrush)
        elif type == 41:
            self.displayimage[row][col].setBrush(self._houseBrush)
        elif type == 42:
            self.displayimage[row][col].setBrush(self._iceBrush)

    def playerLeft(self,Row,Col):
        if self.tile[Row][Col]==1:
            return 0
        elif self.tile[Row][Col]==2:
            return 41
        else:
            return -1

    def playerdisplaypos(self):
        self.playeritem.setOffset(self.playerColumnPos*50,self.playerRowPos*50)

    def playerpose(self,dx,dy):
        if self.playerRightpose:
            if dx>0 and dy==0:
                self.playeritem.setPixmap(self.rightLeft)
            elif dx<0 and dy==0:
                self.playeritem.setPixmap(self.leftLeft)
            elif dx==0 and dy>0:
                self.playeritem.setPixmap(self.frontLeft)
            elif dx==0 and dy<0:
                self.playeritem.setPixmap(self.backLeft)
            self.playerRightpose=False
        else:
            if dx>0 and dy==0:
                self.playeritem.setPixmap(self.rightRight)
            elif dx<0 and dy==0:
                self.playeritem.setPixmap(self.leftRight)
            elif dx==0 and dy>0:
                self.playeritem.setPixmap(self.frontRight)
            elif dx==0 and dy<0:
                self.playeritem.setPixmap(self.backRight)
            self.playerRightpose=True

    def rockGo(self,Row,Col):
        rGo = self.tile[Row][Col]
        if rGo==-1 or rGo==21 or rGo==22:
            return False
        else:
            if rGo==0:
                self.tile[Row][Col]=21
            elif rGo==41:
                self.tile[Row][Col]=22
            self.imgConvert(Row,Col,self.tile[Row][Col])
            return True

    def checkWin(self):
        for m in self.tile:
            for n in m:
                if n==41 or n==2:
                    return
        self.gameSuccess=True
        self.recordtime = time.time()-self.starttime

    def move(self, dx,dy):
        doesGo = self.tile[self.playerRowPos+dy][self.playerColumnPos+dx]
        self.playerpose(dx,dy)
        if doesGo==-1:
            return
        elif doesGo==0:
            self.tile[self.playerRowPos+dy][self.playerColumnPos+dx]=1
            self.tile[self.playerRowPos][self.playerColumnPos]=self.playerLeft(self.playerRowPos,self.playerColumnPos)
            self.imgConvert(self.playerRowPos+dy,self.playerColumnPos+dx,self.tile[self.playerRowPos+dy][self.playerColumnPos+dx])
            self.imgConvert(self.playerRowPos,self.playerColumnPos,self.tile[self.playerRowPos][self.playerColumnPos])
        elif doesGo==21:
            if self.rockGo(self.playerRowPos+dy+dy,self.playerColumnPos+dx+dx):
                self.tile[self.playerRowPos+dy][self.playerColumnPos+dx]=1
                self.tile[self.playerRowPos][self.playerColumnPos]=self.playerLeft(self.playerRowPos,self.playerColumnPos)
                self.imgConvert(self.playerRowPos+dy,self.playerColumnPos+dx,self.tile[self.playerRowPos+dy][self.playerColumnPos+dx])
                self.imgConvert(self.playerRowPos,self.playerColumnPos,self.tile[self.playerRowPos][self.playerColumnPos])
                self.checkWin()
            else:
                return
        elif doesGo==41:
            self.tile[self.playerRowPos+dy][self.playerColumnPos+dx]=2
            self.tile[self.playerRowPos][self.playerColumnPos]=self.playerLeft(self.playerRowPos,self.playerColumnPos)
            self.imgConvert(self.playerRowPos+dy,self.playerColumnPos+dx,self.tile[self.playerRowPos+dy][self.playerColumnPos+dx])
            self.imgConvert(self.playerRowPos,self.playerColumnPos,self.tile[self.playerRowPos][self.playerColumnPos])

        elif doesGo==22:
            if self.rockGo(self.playerRowPos+dy+dy,self.playerColumnPos+dx+dx):
                self.tile[self.playerRowPos+dy][self.playerColumnPos+dx]=2
                self.tile[self.playerRowPos][self.playerColumnPos]=self.playerLeft(self.playerRowPos,self.playerColumnPos)
                self.imgConvert(self.playerRowPos+dy,self.playerColumnPos+dx,self.tile[self.playerRowPos+dy][self.playerColumnPos+dx])
                self.imgConvert(self.playerRowPos,self.playerColumnPos,self.tile[self.playerRowPos][self.playerColumnPos])
                self.checkWin()
            else:
                return
        else:
            return
        self.playerRowPos+=dy
        self.playerColumnPos+=dx
        self.playerdisplaypos()

    def reset(self):
        self.gameSuccess = False
        self.tile = self.tileObject.mapStorage[self.stagenum]
        self.tile=np.array(self.tile)
        self.playerRowPos, self.playerColumnPos = self.tileObject.playerPosStorage[self.stagenum][0],self.tileObject.playerPosStorage[self.stagenum][1]
        for m in range(len(self.tile)):
            for n in range(len(self.tile[m])):
                self.imgConvert(m,n,self.tile[m][n])
        self.playerRightpose = True
        self.playeritem.setPixmap(self.frontRight)
        self.playerdisplaypos()

    def display(self):
        return str(self.tile)
