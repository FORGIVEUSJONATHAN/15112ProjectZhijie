class player:
    def __init__(self,name,type,sequence,initTile,hT,aT,dT):
        #hT means the tiles in the players hand
        #aT means the tiles have the actions of Peng, Chi, or Gang
        #dT means the tiles have been discard by the player
        self.initTile = initTile
        self.name = name
        self.type = type # type will be AI or HUMAN
        self.hT = hT
        self.aT = aT
        self.dT = dT
        self.sequence = sequence
    def __str__(self):
        return f"PlayerSequence: {self.sequence} Player name: {self.name} Player hT: {self.hT} Player dT: {self.dT}"

    def drawATile(self,tileStack): # draw a tile from the stack
        self.hT.append(tileStack[0])
        tileStack.pop(0)

    def disTile(self,Atile,indexofTile): # A tile is the tile the player discard
        self.dT.append(Atile)
        self.hT.pop(indexofTile)





