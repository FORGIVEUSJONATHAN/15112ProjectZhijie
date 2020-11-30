from player import *
from setting import *
class playerAI(player):
    def checkTiletype(self,tileNum):
        if tileNum <= 9:
            return 1 # type 1 indicates Wan
        elif tileNum <= 18:
            return 2 # type 2 indicates Tong
        elif tileNum <= 27:
            return 3 # type 3 indicates Tiao
        elif tileNum <= 31:
            return 4 # type 4 indicates Feng
        elif tileNum <= 34:
            return 5 # type 5 indicates ZFB

    def checkAdj(self,tileNum,hTNumList):
        if tileNum + 1 in hTNumList:
            return True
        elif tileNum - 1 in hTNumList:
            return True
        else:
            return False

    def checkGap(self,tileNum,hTNumList):
        if tileNum + 2 in hTNumList:
            return True
        elif tileNum - 2 in hTNumList:
            return True
        else:
            return False

    def checkSeq(self,tileNumList):# check whether the list contain a sequence like 123, 234 ....
        for i in tileNumList:
            if i+1 in tileNumList and i+2 in tileNumList:
                return True
        return False

    def disTileName(self,dT): # return the number of the tile which needs to be discarded
        hTNameList = self.get_hTNameList()
        hTNameList = setting.tNametoInt(hTNameList)
        doubleList = setting.getDouble(hTNameList)
        tripleList = setting.getTriple(hTNameList)
        mutiList = setting.getMulti(hTNameList)
        dTNameList = setting.tNametoInt(dT)
        if len(mutiList) >= 4 and len(hTNameList) >= 12:
            # if the num of hand tile is smaller than 12, it is not possible to have combination of AABBCCDDEEFFGG
            tListNoMulti = []
            tListNMNS = [] # no multi, no sequence option
            tListNMNA = [] # no multi, No adj
            tListNMNANG = [] # no multi, no adj, no gap
            for i in hTNameList:
                if i not in mutiList:
                    tListNoMulti.append(i)
            if tListNoMulti == []: # condition tiles all have duplicates
                if tripleList !=[]:
                    return f"3-{random.choice(tripleList)}" # AABBCCDDEEEFFF
                elif doubleList !=[]:
                    return f"3-{random.choice(doubleList)}" # AAAABBDDDDEEEE
            elif len(tListNoMulti) == 1: # only 1 tile does not have duplicates
                return f"3-{tListNoMulti[0]}"
            else: # more than 1 tile does not have duplicates
                for i in tListNoMulti:
                    if self.checkTiletype(i) in [4,5]:
                        tListNMNS.append(i)
                    else:
                        if self.checkAdj(i,hTNameList) == False:
                            tListNMNA.append(i)
                            if self.checkGap(i,hTNameList) == False:
                                tListNMNANG.append(i)
                if tListNMNS != []:
                    for i in tListNMNS:
                        if i in dTNameList:
                            return f"3-{i}"
                    return f"3-{random.choice(tListNMNS)}"
                else: # tListNMNS == []
                    if tListNMNANG !=[]:
                        for i in tListNMNANG:
                            if i in dTNameList:
                                return f"3-{i}"
                        return f"3-{random.choice(tListNMNANG)}"
                    else: # tListNMNANG ==[]
                        if tListNMNA != []:
                            for i in tListNMNA:
                                if i in dTNameList:
                                    return f"3-{i}"
                            return f"3-{random.choice(tListNMNA)}"
                        else:
                            return f"3-{random.choice(tListNoMulti)}"
        else:
            tListNoMulti = [] # tiles do not have duplicates
            for i in hTNameList:
                if i not in mutiList:
                    tListNoMulti.append(i)
            value = []
            if tListNoMulti != []:
                tListNMNS3 = tListNoMulti[:] # tiles do not have duplicates and tiles does not form a sequence of 3
                i = 0
                while setting.checkSequence(tListNMNS3):
                    if tListNMNS3[i]+1 in tListNMNS3 and tListNMNS3[i]+2 in tListNMNS3:
                        tListNMNS3.remove(tListNMNS3[i])
                        tListNMNS3.remove(tListNMNS3[i]+1)
                        tListNMNS3.remove(tListNMNS3[i]+2)
                if len(tListNMNS3) != 0: # 有牌既不是3个连续，也没有重复的牌
                    for i in tListNMNS3:
                        if i in dTNameList:
                            return f"3-{i}"
                    return f"3-{random.choice(tListNMNS3)}"
                else: # len(tListNMNS3) == 0
                    if len(doubleList)>=2:
                        for i in doubleList:
                            if i in dTNameList:
                                return f"3-{i}"
                        return f"3-{random.choice(doubleList)}"
                    else:
                        for i in tListNoMulti:
                            if i in dTNameList:
                                return f"3-{i}"
                        return f"3-{random.choice(tListNoMulti)}"
            else: #tListNoMulti == []
                if len(doubleList)>=2:
                    for i in doubleList:
                        if i in dTNameList:
                            return f"3-{i}"
                    return f"3-{random.choice(doubleList)}"
                else:
                    if tripleList!=[]:
                        for i in tripleList:
                            if i in dTNameList:
                                return f"3-{i}"
                        return f"3-{random.choice(tripleList)}"
                    else:
                        return f"3-{random.choice(doubleList)}"
    def disTileAct(self,screen,dTName):
        tileIndex = 0
        for i in range(len(self.hT)):
            if dTName == self.hT[i].name:
                tileIndex = i
                break
        setting.creatDtile(screen, self.hT[tileIndex], self.dT, self.sequence)
        self.hT.pop(tileIndex)
        if self.sequence == 2:
            for i in self.hT[tileIndex:len(self.hT)]:
                i.rect.top += 48
                i.blitSelf()
        elif self.sequence == 3:
            for i in self.hT[tileIndex:len(self.hT)]:
                i.rect.left += 48
                i.blitSelf()
        elif self.sequence == 4:
            for i in self.hT[tileIndex:len(self.hT)]:
                i.rect.top -= 48
                i.blitSelf()
        print(f"player{self.sequence} has {len(self.hT)} tiles")

        return self.dT[-1]
