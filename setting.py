import random

import pygame

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


def drawTile(tileStack,sequence):
    pTile = []
    if sequence == 1: # the first player need to draw 14 tiles
        for i in range(14):
            pTile.append(tileStack[0]) # add the first element into list
            tileStack.pop(0) #remove the first element of the list
    else:
        for i in range(13):
            pTile.append(tileStack[0]) # add the first element into list
            tileStack.pop(0) #remove the first element of the list
    pTile.sort()
    return pTile

# tileStack111 = tileStack(3)
# print(drawTile(tileStack111,1))
# print(drawTile(tileStack111,2))
# print(drawTile(tileStack111,3))

def showtile(screen,pTile,playerNo):
    tileObjList = []
    for i in range(len(pTile)):
        tileObj = tile(screen,pTile[i],False)
        if playerNo == 1:
            tileObj.image = pygame.image.load("pic/tile_type3_300ppi/"+pTile[i]+".png")
            tileObj.image = pygame.transform.smoothscale(tileObj.image,(80,100))
            tileObj.rect.inflate_ip(-124, -148)
            tileObj.rect.left = i * 80
            tileObj.screen_rect = screen.get_rect()
            tileObj.rect.bottom = tileObj.screen_rect.bottom
        tileObjList.append(tileObj)
