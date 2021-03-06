
## Course Number: 15112
## Andrew ID: zhijiex
import random
import pygame
import setting
from tile import tile


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

    # draw a tile from the stack
    def drawATile(self,screen,tileStack):
        # check whether there is a tile in tile stack
        if tileStack == []:
            return False
        # when player holds certain number of tiles, they are not able to draw
        elif len(self.hT)+1 not in [1,2,5,8,11,12,14]:
            print( f"player{self.sequence}cannot draw, it has {len(self.hT)} tiles")

        # next part will add create a tile object for different players
        # move tile into the hand tile
        # remove tile from the stack
        elif self.sequence == 1: #create the tile object for player 1
            tileObj = tile(screen,tileStack[0], False) #creat the tile object
            tileObj.image = pygame.image.load("pic/tile_type3_300ppi/" + tileStack[0] + ".png") # load the tile image
            tileObj.image = pygame.transform.smoothscale(tileObj.image, (60, 75)) # transform the tile image
            tileObj.rect = tileObj.image.get_rect()
            tileObj.rect.x = self.hT[len(self.hT)-1].rect.x + 60 # set the x coordinate of the tile
            tileObj.rect.y = self.hT[0].rect.y # set the y coordinate of the tile
            tileObj.blitSelf()
            self.hT.append(tileObj) # add obj to the hand tile list
            tileStack.pop(0) # remove the tile from the stack

        elif self.sequence == 2: #create the tile object for player 2
            tileObj = tile(screen,tileStack[0], False)
            tileObj.image = pygame.image.load("pic/tile_type3_300ppi/3-b.png")
            tileObj.image = pygame.transform.smoothscale(tileObj.image, (48, 60))
            tileObj.image = pygame.transform.rotate(tileObj.image,90)
            tileObj.rect = tileObj.image.get_rect()
            tileObj.rect.x = self.hT[0].rect.x
            tileObj.rect.y = self.hT[len(self.hT)-1].rect.y - 48
            tileObj.blitSelf()
            self.hT.append(tileObj)
            tileStack.pop(0)

        elif self.sequence == 3: #create the tile object for player 3
            tileObj = tile(screen,tileStack[0], False)
            tileObj.image = pygame.image.load("pic/tile_type3_300ppi/3-b.png")
            tileObj.image = pygame.transform.smoothscale(tileObj.image, (48, 60))
            tileObj.image = pygame.transform.rotate(tileObj.image,180)
            tileObj.rect = tileObj.image.get_rect()
            tileObj.rect.x = self.hT[len(self.hT)-1].rect.x - 48
            tileObj.rect.y = self.hT[0].rect.y
            tileObj.blitSelf()
            self.hT.append(tileObj)
            tileStack.pop(0)

        elif self.sequence == 4: #create the tile object for player 4
            tileObj = tile(screen,tileStack[0], False)
            tileObj.image = pygame.image.load("pic/tile_type3_300ppi/3-b.png")
            tileObj.image = pygame.transform.smoothscale(tileObj.image, (48, 60))
            tileObj.image = pygame.transform.rotate(tileObj.image,270)
            tileObj.rect.x = self.hT[0].rect.x
            tileObj.rect.y = self.hT[len(self.hT)-1].rect.y + 48
            tileObj.blitSelf()
            self.hT.append(tileObj)
            tileStack.pop(0)
        self.tileSorting2(screen)


    def disTile(self,Atile,indexofTile): # A tile is the tile the player discard
        self.hT.pop(indexofTile)
        for i in self.hT[indexofTile:len(self.hT)]: # reset the rect of the tiles
            i.rect.x -= 60
        print(f"player{self.sequence} has {len(self.hT)} tiles")


    def disTileRandom(self,screen): # this is a function for Random AI
        ranTileIndex = random.randint(0,len(self.hT)-1)
        setting.creatDtile(screen, self.hT[ranTileIndex], self.dT, self.sequence)
        self.hT.pop(ranTileIndex)
        if self.sequence == 2:
            for i in self.hT[ranTileIndex:len(self.hT)]:
                i.rect.top += 48
                i.blitSelf()
        elif self.sequence == 3:
            for i in self.hT[ranTileIndex:len(self.hT)]:
                i.rect.left += 48
                i.blitSelf()
        elif self.sequence == 4:
            for i in self.hT[ranTileIndex:len(self.hT)]:
                i.rect.top -= 48
                i.blitSelf()
        return self.dT[-1]


    def tileSorting2(self,screen): #sort tiles for tile list as objects

        for i in range(len(self.hT)):
            index = i
            min = int(self.hT[i].name[2:])
            for j in range(i+1,len(self.hT)):
                num = int(self.hT[j].name[2:])
                if num < min:
                    min = num
                    index = j
            tempName = self.hT[i].name
            self.hT[i].name = self.hT[index].name
            self.hT[index].name = tempName
            tempImage = self.hT[i].image
            self.hT[i].image = self.hT[index].image
            self.hT[index].image = tempImage

    # get the list of all tiles in the hand tile list
    def get_hTNameList(self):
        hTNameList = []
        for i in self.hT:
            hTNameList.append(i.name)
        return hTNameList

    # get the list of all tiles in the discarded tile list
    def get_dTNameList(self):
        dTNameList = []
        for i in self.dT:
            dTNameList.append(i.name)
        return dTNameList

    # check whther cPlayer let other player win
    def checkHuCong(self,cPlayer):
        # a different type of win
        hTNameList = self.get_hTNameList()
        dTileName = cPlayer.dT[-1].name
        # new list contains other players hand tiles and Cplayer last dT
        hTNameList.append(dTileName)
        hTNameList = setting.tileSorting1(hTNameList)
        # check whether new list satisfy the winning condition
        return setting.checkwin(hTNameList)

    def checkPeng(self,cPlayer): # check peng
        # if Peng can happen return True
        # cPlayer == current player
        hTNameList = self.get_hTNameList()
        # count the number of last discarded tile in player's hand
        count = hTNameList.count(cPlayer.dT[-1].name)
        if count == 2:
            return True

    def checkGang(self,cPlayer):
        # if Gang can happen return True
        # cPlayer == current player
        hTNameList = self.get_hTNameList()
        count = hTNameList.count(cPlayer.dT[-1].name)
        if count == 3:
            return 1
        elif setting.getQura(setting.tNametoInt(self.get_hTNameList())) !=[]:
            return 2

