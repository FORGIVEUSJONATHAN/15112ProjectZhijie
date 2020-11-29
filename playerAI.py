from player import *
from setting import *
class playerAI(player):
    def disTileName(self): # return the name of the tile which needs to be discarded
        hTNameList = self.get_hTNameList()
        hTNameList = tNametoInt(hTNameList)
        doubleList = getDouble(hTNameList)
        tripleList = getTriple(hTNameList)
        mutiList = getMulti(hTNameList)

        if len(mutiList) >= 4:
            tlistCopy = hTNameList[:]

        for i in hTNameList():

