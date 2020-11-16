class player:
    def __init__(self,name,type,sequence,hT,aT,dT):
        self.name = name
        self.type = type # type will be AI or HUMAN
        self.hT = hT
        self.aT = aT
        self.dT = dT

    def drawTile(self,tileStack): # draw a tile from the stack
        self.hT.append(tileStack[0])
        tileStack.pop(0)




