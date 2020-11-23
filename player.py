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

    def drawATile(self,screen,tileStack): # draw a tile from the stack
        print(tileStack[0])
        if self.sequence == 1: #create the tile object for player 1
            tileObj = tile(screen,tileStack[0], False)
            tileObj.image = pygame.image.load("pic/tile_type3_300ppi/" + tileStack[0] + ".png")
            tileObj.image = pygame.transform.smoothscale(tileObj.image, (60, 75))
            tileObj.rect = tileObj.image.get_rect()
            tileObj.rect.y = self.hT[0].rect.y
            tileObj.rect.x = self.hT[len(self.hT)-1].rect.x + 60
            tileObj.blitSelf()
            self.hT.append(tileObj)
        tileStack.pop(0)
        self.tileSorting2(screen)
        # if self.sequence == 1:

    def disTile(self,Atile,indexofTile): # A tile is the tile the player discard
        self.hT.pop(indexofTile)
        for i in self.hT[indexofTile:len(self.hT)]: # reset the rect of the tiles
            i.rect.x -= 60

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

        # the algorithm below will cost more time to load image!!!!
        # tilenamelist = []
        # for i in self.hT:
        #     tilenamelist.append(i.name)
        # tilenamelist = setting.tileSorting1(tilenamelist)
        # print(tilenamelist)
        # self.hT = setting.creatHtile(screen,tilenamelist,1)
