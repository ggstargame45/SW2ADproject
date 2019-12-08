import numpy as np

class Tiles(object):
    """
    맵 정보만 줌
    """
    stageRow = 8
    stageColumn = 8
    #def stageMaker(self, stageNum)
    #def __init__(self, stageNum)
    def __init__(self):

        #-1=벽 1=플레이어 2=플레이어+집 3=박스 4=집 5=박스+집
        self.tile = [
            [-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,0,0,0,0,0,0,-1],
            [-1,0,4,4,0,0,0,-1],
            [-1,0,4,4,3,0,0,-1],
            [-1,0,0,0,3,0,0,-1],
            [-1,0,0,1,0,0,0,-1],
            [-1,0,0,0,0,0,0,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1]
            ]
        self.playerRowPos, self.playerColumnPos = 5, 3
        self.tile=np.array(self.tile)


    def playerLeft(self,Row,Col):
        if self.tile[Row][Col]==1:
            return 0
        elif self.tile[Row][Col]==2:
            return 4
        else:
            return -1

    def rockGo(self,Row,Col):
        rGo = self.tile[Row][Col]
        if rGo==-1 or rGo==3 or rGo==5:
            return False
        else:
            if rGo==0:
                self.tile[Row][Col]=3
            elif rGo==4:
                self.tile[Row][Col]=5
            return True
    #-1=벽 1=플레이어 2=플레이어+집 3=박스 4=집 5=박스+집
    def move(self, dx,dy):
        doesGo = self.tile[self.playerRowPos+dy][self.playerColumnPos+dx]
        if doesGo==-1:
            return
        elif doesGo==0:
            self.tile[self.playerRowPos+dy][self.playerColumnPos+dx]=1
            self.tile[self.playerRowPos][self.playerColumnPos]=self.playerLeft(self.playerRowPos,self.playerColumnPos)
        elif doesGo==3:
            if self.rockGo(self.playerRowPos+dy+dy,self.playerColumnPos+dx+dx):
                self.tile[self.playerRowPos+dy][self.playerColumnPos+dx]=1
                self.tile[self.playerRowPos][self.playerColumnPos]=self.playerLeft(self.playerRowPos,self.playerColumnPos)
            else:
                return
        elif doesGo==4:
            self.tile[self.playerRowPos+dy][self.playerColumnPos+dx]=2
            self.tile[self.playerRowPos][self.playerColumnPos]=self.playerLeft(self.playerRowPos,self.playerColumnPos)

        elif doesGo==5:
            if self.rockGo(self.playerRowPos+dy+dy,self.playerColumnPos+dx+dx):
                self.tile[self.playerRowPos+dy][self.playerColumnPos+dx]=2
                self.tile[self.playerRowPos][self.playerColumnPos]=self.playerLeft(self.playerRowPos,self.playerColumnPos)
            else:
                return
        self.playerRowPos+=dy
        self.playerColumnPos+=dx

    def display(self):
        return str(self.tile)
