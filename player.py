class player:
    def __init__(self,name,type,sequence,hT,aT,dT):
        #hT means the tiles in the players hand
        #aT means the tiles have the actions of Peng, Chi, or Gang
        #dT means the tiles have been discard by the player
        self.name = name
        self.type = type # type will be AI or HUMAN
        self.hT = hT
        self.aT = aT
        self.dT = dT

    def drawATile(self,tileStack): # draw a tile from the stack
        self.hT.append(tileStack[0])
        tileStack.pop(0)

    def disTile(self,Atile): # A tile is the tile the player discard
        self.dT.append(self.hT[0])
        self.hT.pop(0)




