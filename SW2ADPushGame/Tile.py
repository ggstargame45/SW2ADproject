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
        """
        음수는 무조건 막히는 타일
        -1=벽
        0=빈공간
        1~20는 플레이어와 플레이어+타일
        1=플레이어 2=플레이어+집
        21~40대는 박스와 박스+타일
        21=박스 22=박스+집
        41~은 단일 타일들
        41=집 
        """
        self.tile = [
            [-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,0,0,0,0,0,0,-1],
            [-1,0,41,41,0,0,0,-1],
            [-1,0,41,41,21,0,0,-1],
            [-1,0,0,0,21,0,0,-1],
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
            return 41
        else:
            return -1

    def rockGo(self,Row,Col):
        rGo = self.tile[Row][Col]
        if rGo==-1 or rGo==21 or rGo==22:
            return False
        else:
            if rGo==0:
                self.tile[Row][Col]=21
            elif rGo==41:
                self.tile[Row][Col]=22
            return True
    """
    음수는 무조건 막히는 타일
    -1=벽
    0=빈공간
    1~20는 플레이어와 플레이어+타일
    1=플레이어 2=플레이어+집
    21~40대는 박스와 박스+타일
    21=박스 22=박스+집
    41~은 단일 타일들
    41=집 
    """
    def move(self, dx,dy):
        doesGo = self.tile[self.playerRowPos+dy][self.playerColumnPos+dx]
        if doesGo==-1:
            return
        elif doesGo==0:
            self.tile[self.playerRowPos+dy][self.playerColumnPos+dx]=1
            self.tile[self.playerRowPos][self.playerColumnPos]=self.playerLeft(self.playerRowPos,self.playerColumnPos)
        elif doesGo==21:
            if self.rockGo(self.playerRowPos+dy+dy,self.playerColumnPos+dx+dx):
                self.tile[self.playerRowPos+dy][self.playerColumnPos+dx]=1
                self.tile[self.playerRowPos][self.playerColumnPos]=self.playerLeft(self.playerRowPos,self.playerColumnPos)
            else:
                return
        elif doesGo==41:
            self.tile[self.playerRowPos+dy][self.playerColumnPos+dx]=2
            self.tile[self.playerRowPos][self.playerColumnPos]=self.playerLeft(self.playerRowPos,self.playerColumnPos)

        elif doesGo==22:
            if self.rockGo(self.playerRowPos+dy+dy,self.playerColumnPos+dx+dx):
                self.tile[self.playerRowPos+dy][self.playerColumnPos+dx]=2
                self.tile[self.playerRowPos][self.playerColumnPos]=self.playerLeft(self.playerRowPos,self.playerColumnPos)
            else:
                return
        self.playerRowPos+=dy
        self.playerColumnPos+=dx

    def display(self):
        return str(self.tile)
