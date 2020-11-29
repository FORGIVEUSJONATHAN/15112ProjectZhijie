import random

import buttons
from player import *
import pygame

from playerAI import playerAI
from tile import tile
def tileStack(type):
    # create a stack a tiles and shuffle them
    tileList1 = []
    tileList2 = []
    tileList3 = []
    if type == 3:
        tileList1 = ['3-1','3-2','3-3','3-4','3-5','3-6','3-7','3-8',
                     '3-9','3-10','3-11','3-12','3-13','3-14','3-15','3-16',
                     '3-17','3-18','3-19','3-20','3-21','3-22','3-23','3-24',
                     '3-25','3-26','3-27']
        # tileList 1 has Wan Tong Tiao
        tileList2 = ['3-28','3-29','3-30','3-31']
        # tileList 2 has Feng
        tileList3 = ['3-32','3-33','3-34']
        # tileList 3 has Zhong Fa Baiban

    elif type == 4:
        tileList1 = ['4-1', '4-2', '4-3', '4-4', '4-5', '4-6', '4-7', '4-8',
                     '4-9', '4-10', '4-11', '4-12', '4-13', '4-14', '4-15', '4-16',
                     '4-17', '4-18', '4-19', '4-20', '4-21', '4-22', '4-23', '4-24',
                     '4-25', '4-26', '4-27']
        # tileList 1 has Wan Tong Tiao
        tileList2 = ['4-28','4-29','4-30','4-31']
        # tileList 2 has Feng
        tileList3 = ['4-32','4-33','4-34']
        # tileList 3 has Zhong Fa Baiban


    tileList = tileList1 * 4 + tileList2 * 4 + tileList3 * 4
    random.shuffle(tileList)
    # get the shuffled list
    return tileList

# print(tileStack(3))

def tileSorting1(tilelist): #sort tiles for tile list as string
    for i in range(len(tilelist)):
        index = i
        min = int(tilelist[i][2:])
        for j in range(i+1,len(tilelist)):
            num = int(tilelist[j][2:])
            if num < min:
                min = num
                index = j
        tilelist[i],tilelist[index] = tilelist[index],tilelist[i]

    return tilelist
# print(tileSorting(['3-1', '3-12', '3-13', '3-14', '3-18', '3-2', '3-22', '3-23', '3-23', '3-29', '3-3', '3-30', '3-5', '3-8']))






def drawTile(tileStack,sequence):
    pTile = []
    if sequence == 1: # the first player need to draw 14 tiles
        for i in range(14):
            pTile.append(tileStack[0]) # add the first element into list
            tileStack.pop(0) #remove the first element of the list
    else:
        for i in range(13):
            pTile.append(tileStack[0])
            print(pTile)# add the first element into list
            tileStack.pop(0) #remove the first element of the list
    pTile = tileSorting1(pTile)
    return pTile

# tileStack111 = tileStack(3)
# print(drawTile(tileStack111,1))
# print(drawTile(tileStack111,2))
# print(drawTile(tileStack111,3))

def drawTileAll():
    tileStackAll = tileStack(3)
    sequenceList = [1,2,3,4]
    random.shuffle(sequenceList)
    print(sequenceList)
    ## a random list to determine the sequence
    pTile1 = drawTile(tileStackAll,sequenceList[0])
    pTile2 = drawTile(tileStackAll,sequenceList[1])
    pTile3 = drawTile(tileStackAll,sequenceList[2])
    pTile4 = drawTile(tileStackAll,sequenceList[3])
    player1 = playerAI("AA","HUMAN",sequenceList[0],pTile1,[],[],[])
    player2 = playerAI("BB","AI",sequenceList[1],pTile2,[],[],[])
    player3 = playerAI("CC","AI",sequenceList[2],pTile3,[],[],[])
    player4 = playerAI("DD","AI",sequenceList[3],pTile4,[],[],[])
    print(f"tile stack is {tileStackAll}")
    return tileStackAll, player1, player2, player3, player4
    # return the player objects and the remaining tileStack



def creatHtile(screen,pTile,playerNo): # will return a list of hand tile object
    tileObjList = []
    if playerNo == 1:
        for i in range(len(pTile)):
            tileObj = tile(screen,pTile[i],False)
            tileObj.image = pygame.image.load("pic/tile_type3_300ppi/"+pTile[i]+".png")
            tileObj.image = pygame.transform.smoothscale(tileObj.image,(60,75))
            tileObj.rect = tileObj.image.get_rect()
            tileObj.rect.left = 180 + i * 60
            tileObj.rect.top = 640

            tileObj.blitSelf()
            tileObjList.append(tileObj)


    elif playerNo == 2:
        for i in range(len(pTile)):
            tileObj = tile(screen, pTile[i], False)
            tileObj.image = pygame.image.load("pic/tile_type3_300ppi/3-b.png")
            tileObj.image = pygame.transform.smoothscale(tileObj.image, (48, 60))
            tileObj.image = pygame.transform.rotate(tileObj.image,90)
            tileObj.rect = tileObj.image.get_rect()

            tileObj.rect.bottom = 680 - i * 48
            tileObj.rect.left = 1060
            tileObj.blitSelf()
            tileObjList.append(tileObj)


    elif playerNo == 3:
        for i in range(len(pTile)):
            tileObj = tile(screen, pTile[i], False)
            tileObj.image = pygame.image.load("pic/tile_type3_300ppi/3-b.png")
            tileObj.image = pygame.transform.smoothscale(tileObj.image, (48, 60))
            tileObj.image = pygame.transform.rotate(tileObj.image,180)
            tileObj.rect = tileObj.image.get_rect()

            tileObj.rect.top = 140 - 60
            tileObj.rect.left = 940 - 48 - i*48
            tileObj.blitSelf()
            tileObjList.append(tileObj)


    elif playerNo == 4:
        for i in range(len(pTile)):
            tileObj = tile(screen, pTile[i], False)
            tileObj.image = pygame.image.load("pic/tile_type3_300ppi/3-b.png")
            tileObj.image = pygame.transform.smoothscale(tileObj.image, (48, 60))
            tileObj.image = pygame.transform.rotate(tileObj.image,270)
            tileObj.rect = tileObj.image.get_rect()
            tileObj.rect.top = 80 + i * 48
            tileObj.rect.left = 80
            tileObj.blitSelf()
            tileObjList.append(tileObj)

    return tileObjList


def creatDtile(screen,hTObj,dTlist,playerNo): # screen, handTile object, playerNo is the player sequence
    num = len(dTlist)
    hTObj.image = pygame.image.load("pic/tile_type3_300ppi/" + hTObj.name + ".png")
    hTObj.image = pygame.transform.smoothscale(hTObj.image, (30, 40))
    hTObj.rect = hTObj.image.get_rect()
    if playerNo == 1:
        if num < 8:
            hTObj.rect.top = 510+10
            hTObj.rect.left = 480+num*30
        elif num < 16:
            hTObj.rect.top = 510+40+10
            hTObj.rect.left = 480+(num-8)*30
        elif num < 24:
            hTObj.rect.top = 510+80+10
            hTObj.rect.left = 480+(num-16)*30

    elif playerNo == 2:
        hTObj.image = pygame.transform.rotate(hTObj.image,90)

        if num < 8:
            hTObj.rect.top = 510-20 - num * 30
            print(hTObj.rect.top)
            hTObj.rect.left = 720
        elif num < 16:
            hTObj.rect.top = 510-20 - (num-8)*30
            hTObj.rect.left = 720 + 40
        elif num < 24:
            hTObj.rect.top = 510-20 - (num-16)*30
            hTObj.rect.left = 720 + 80

    elif playerNo == 3:
        hTObj.image = pygame.transform.rotate(hTObj.image,180)

        if num < 8:
            hTObj.rect.top = 240
            hTObj.rect.left = 690 - num*30
        elif num < 16:
            hTObj.rect.top = 200
            hTObj.rect.left = 690 - (num-8)*30
        elif num < 24:
            hTObj.rect.top = 160
            hTObj.rect.left = 690 - (num-16)*30

    elif playerNo == 4:
        hTObj.image = pygame.transform.rotate(hTObj.image,270)

        if num < 8:
            hTObj.rect.top = 270+10 + num*30
            hTObj.rect.left = 440
        elif num < 16:
            hTObj.rect.top = 270+10 + (num-8)*30
            hTObj.rect.left = 400
        elif num < 24:
            hTObj.rect.top = 270+10 + (num-16)*30
            hTObj.rect.left = 360

    hTObj.blitSelf()
    dTlist.append(hTObj)

    return dTlist # return the discard tile list with new tile object hTObj

def refreshTileImage(t1,t2,t3,t4):
    for i in t1.hT: # display the player 1 hand tiles on screen
        i.blitSelf()
    for i in t2.hT: # display the player 2 hand tiles on screen
        i.blitSelf()
    for i in t3.hT: # display the player 3 hand tiles on screen
        i.blitSelf()
    for i in t4.hT: # display the player 4 hand tiles on screen
        i.blitSelf()
    for i in t1.dT: # display the player 1 discarded tiles on screen
        i.blitSelf()
    for i in t2.dT: # display the player 2 discarded tiles on screen
        i.blitSelf()
    for i in t3.dT: # display the player 3 discarded tiles on screen
        i.blitSelf()
    for i in t4.dT: # display the player 4 discarded tiles on screen
        i.blitSelf()
    for i in t1.aT: # display the player 1 discarded tiles on screen
        i.blitSelf()
    for i in t2.aT: # display the player 2 discarded tiles on screen
        i.blitSelf()
    for i in t3.aT: # display the player 3 discarded tiles on screen
        i.blitSelf()
    for i in t4.aT: # display the player 4 discarded tiles on screen
        i.blitSelf()


def tNametoInt(tileNameList): # this is a function which convert the tile name to int value
    for i in range(len(tileNameList)):
        tileNameList[i] = int(tileNameList[i][2:])
    return tileNameList


def getDouble(numList):
    double = []
    listCopy = numList[:]
    for i in numList:
        if listCopy.count(i) == 2:
            double.append(i)
            while i in listCopy:
                listCopy.remove(i) # tList1 No double
    return double


def getTriple(numList):
    triple = []
    listCopy = numList[:]
    for i in numList:
        if listCopy.count(i) == 3:
            triple.append(i)
            while i in listCopy:
                listCopy.remove(i) # tList1 No triple
    return triple


def getQura(numList):
    qura = []
    listCopy = numList[:]
    for i in numList:
        if listCopy.count(i) == 4:
            qura.append(i)
            while i in listCopy:
                listCopy.remove(i) # tList1 No Qura
    return qura
# print(getQura([1,2,1,1,3,2,1])) # testing for getQura

def getMulti(numList):
    multi = []
    listCopy = numList[:]
    for i in numList:
        if listCopy.count(i) >= 2:
            multi.append(i)
            while i in listCopy:
                listCopy.remove(i) # tList1 No double
    return multi

def checkSequence(numList):
    # check whether the list can be separate as sequences
    # 223344, 233445, 234456,223344456
    numListCopy = numList[:]
    if len(numListCopy) not in [3, 6, 9, 12]:
        return False
    while len(numListCopy) in [3,6,9,12]:
        # constraint for the length of number list
        if numListCopy[0]+1 in numListCopy and numListCopy[0]+2 in numListCopy:
            numListCopy.remove(numListCopy[0]+2)
            numListCopy.remove(numListCopy[0]+1)
            numListCopy.remove(numListCopy[0])
        else:
            return False
    return True

def checkwin(hTNameList):
    # hu = buttons.hu(screen)
    hTNameList = tNametoInt(hTNameList)
    if len(hTNameList) == 3: # HU1 three tiles are the same
        if hTNameList [0] == hTNameList [1] and hTNameList [1] == hTNameList [2]:
            print("Hu")
            # hu.blitSelf()
            return True

    # find all the pairs
    double = getDouble(hTNameList) # tile appear 2 times fix the head of tile 固定麻将头
    multiTile = getMulti(hTNameList) #tile appear 2,3,4 times


    if len(double) == 7: # HU2 the player have 14 hand tiles which can form seven pairs
        # hu.blitSelf()
        return True

    if len(double) == 1: # only 1 double
        tList1 = hTNameList[:]
        tList1.remove(double[0])
        tList1.remove(double[0])
        tList2 = hTNameList[:]
        for i in tList1: # tList will only have tile can only have 1, 3, 4
            if tList2.count(i) == 3: # 3 tiles are the same
                while i in tList2:
                    tList2.remove(i) # tList 2 No double and No Triple
        countSeq = 0
        if len(tList2) == [3,6,9,12] :
            for i in range(2,len(tList2),3):
                if tList2[i] not in [1,2,10,11,19,20,28,29,30,31,32,33,34]:# HU 3 AA BCD EFG HIJ
                    if tList2[i] - 1 == tList2[i-1] and tList2[i] - 2 == tList2[i-2]: # check tiles are in sequence
                        countSeq += 1
            if countSeq == len(tList2)//3:
                print("Hu")
                # hu.blitSelf()
                return True

    elif len(multiTile) == 5 and len(double) == 1:
        return True
    elif len(multiTile) == 4 and len(double) == 1:
        tList2 = hTNameList[:]
        if len(tList2) == 11: #AA BBB CCC DDD EEE
            return True
        elif len(tList2) == 14:
            for i in multiTile:
                while i in tList2:
                    tList2.remove(i)
            if tList2[2] not in [1,2,10,11,19,20,28,29,30,31,32,33,34]: # AA BBB CCC DDD with sequence
                if tList2[2]-1 == tList2[1] and tList2[2]-2 == tList2[0]:
                    return True

    if multiTile != []:
        tList2 = hTNameList[:]
        for i in multiTile:
            tList2.remove(i)
            tList2.remove(i) # remove a double from the list
            if checkSequence(tList2): #去掉麻将头之后检查是否组成sequence
                return True
            elif len(getTriple(tList2))!=0: # 还存在三个麻将是一样的
                tripleList = getTriple(tList2) # the length of triple list will only be maximum two, already checked 3 and 4
                if len(tripleList) == 1:
                    tList3 = tList2[:]
                    for i in range(3):
                        tList3.remove(tripleList[0]) # remove all the triples in the list
                    if checkSequence(tList3):
                        return True
                elif len(tripleList) == 2:
                    tList3 = tList2[:]
                    for i in tripleList:
                        for x in range(3):
                            tList3.remove(i)
                        if checkSequence(tList3): # check if remove one triple, whether the rest can form sequence
                            return True
                        else:
                            tList3 = tList2[:]

                    for i in tripleList:
                        for x in range(3):
                            tList3.remove(i)
                    if checkSequence(tList3): # check if remove both triple, whether the rest can form sequence
                        return True

            tList2 = hTNameList[:]
    return False

# assert (checkwin([1,1,2,3,4]) == True)
# assert (checkwin([1,2,2,3,4])== False)
# assert (checkwin([2,2,3,3,4,4,4,5,6,7,7])== True)
# assert (checkwin([2,2,3,3,4,4,4,5,6,7])== False)
# print(checkwin([2,2,3,3,4,4,4,5,6,7]))
# print(checkwin(['3-1', '3-6', '3-13', '3-14', '3-14', '3-15', '3-16', '3-17', '3-17', '3-22', '3-24', '3-27', '3-29', '3-31']))
print(checkwin(['3-1', '3-2', '3-3', '3-19', '3-20', '3-21', '3-24', '3-25', '3-26', '3-28', '3-28', '3-28', '3-31', '3-31']))

# def convertdTtohT(dTile,playerSequence): #A dTile, player sequence of hT
#     if playerSequence == 1:

def pengAction(screen,playerA,playerB):
    #action happened after the user clicked peng button 碰
    #player A will execute peng
    dTname = playerB.dT[-1].name
    if playerA.sequence == 1:
        for i in range(3):
            tileObj = tile(screen,dTname, False)
            tileObj.image = pygame.image.load("pic/tile_type3_300ppi/" + dTname + ".png")
            tileObj.image = pygame.transform.smoothscale(tileObj.image, (60, 75))
            tileObj.rect = tileObj.image.get_rect()
            tileObj.rect.left = 180 + len(playerA.aT) * 60
            tileObj.rect.top = 720
            tileObj.blitSelf()
            playerA.aT.append(tileObj)
        indexlist = []
        for i in range(len(playerA.hT)):
            if playerA.hT[i].name == dTname:
                indexlist.append(i)
        for i in range(2):
            playerA.hT.pop(indexlist[i]-i)
            for x in playerA.hT[indexlist[i]-i:len(playerA.hT)]:  # reset the rect of the tiles
                x.rect.x -= 60
        playerB.dT.remove(playerB.dT[-1])
        playerA.tileSorting2(screen)


def gangAction1(screen,playerA,playerB):
    dTname = playerB.dT[-1].name
    if playerA.sequence == 1:
        for i in range(4):
            tileObj = tile(screen,dTname, False)
            tileObj.image = pygame.image.load("pic/tile_type3_300ppi/" + dTname + ".png")
            tileObj.image = pygame.transform.smoothscale(tileObj.image, (60, 75))
            tileObj.rect = tileObj.image.get_rect()
            tileObj.rect.left = 180 + len(playerA.aT) * 60
            tileObj.rect.top = 720
            tileObj.blitSelf()
            playerA.aT.append(tileObj)
        indexlist = []
        for i in range(len(playerA.hT)):
            if playerA.hT[i].name == dTname:
                indexlist.append(i)
        for i in range(3):
            playerA.hT.pop(indexlist[i]-i)
            for x in playerA.hT[indexlist[i]-i:len(playerA.hT)]:  # reset the rect of the tiles
                x.rect.x -= 60
        playerB.dT.remove(playerB.dT[-1])
        playerA.tileSorting2(screen)

def gangAction2(screen,playerA):
    hTNameList = playerA.get_hTNameList()
    hTNameList = tNametoInt(hTNameList)
    tName = f"3-{str(getQura(hTNameList))}"
    if playerA.sequence == 1:
        for i in range(4):
            tileObj = tile(screen,tName, False)
            tileObj.image = pygame.image.load("pic/tile_type3_300ppi/" + tName + ".png")
            tileObj.image = pygame.transform.smoothscale(tileObj.image, (60, 75))
            tileObj.rect = tileObj.image.get_rect()
            tileObj.rect.left = 180 + len(playerA.aT) * 60
            tileObj.rect.top = 720
            tileObj.blitSelf()
            playerA.aT.append(tileObj)
        indexlist = []
        for i in range(len(playerA.hT)):
            if playerA.hT[i].name == tName:
                indexlist.append(i)
        for i in range(4):
            playerA.hT.pop(indexlist[i]-i)
            for x in playerA.hT[indexlist[i]-i:len(playerA.hT)]:  # reset the rect of the tiles
                x.rect.x -= 60
        playerA.tileSorting2(screen)

def getdTAll(playerA,playerB,playerC,playerD):
    dTAll = []
    dTAll = playerA.get_dTNameList() + playerB.get_dTNameList()+ playerC.get_dTNameList()+ playerD.get_dTNameList()
    return dTAll # ass "3-11","3-12"