import sys
import pygame
import setting
import buttons
class wnd1:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("麻将")
        icon = pygame.image.load("pic/tile_type4_300ppi/4-33.png")
        pygame.display.set_icon(icon)
        screen = pygame.display.set_mode((1200, 800),pygame.RESIZABLE)
        start = pygame.image.load("pic/Start.png")
        start = pygame.transform.scale(start, (200, 100))
        startRect = start.get_rect()
        startRect.centerx = screen.get_rect().centerx
        startRect.centery = screen.get_rect().centery
        running = True
        while running:
            screen.fill((146, 168, 209))
            screen.blit(start, startRect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(startRect)
                    print(event.pos)
                    if startRect.collidepoint(event.pos):
                        print("1")
                        wnd2(screen)
                    else:
                        print("2")
            pygame.display.update()


class wnd2:
    def __init__(self,screen):
        self.screen = screen
        pygame.display.set_caption("麻将")
        screen = pygame.display.set_mode((1200,800))
        screenRect = screen.get_rect()
        tile = pygame.image.load("pic/tile_type3_300ppi/3-1.png")
        tile = pygame.transform.smoothscale(tile,(80,110))
        tileRect = tile.get_rect()
        print(tileRect)
        tileRect.x = 100
        tileRect.y = 700
        print(tileRect)
        listofPlayer = setting.drawTileAll()
        tileRemain = listofPlayer[0]
        player1 = listofPlayer[1]
        player2 = listofPlayer[2]
        player3 = listofPlayer[3]
        player4 = listofPlayer[4]
        player1.hT = setting.creatHtile(screen, player1.initTile, player1.sequence)
        player2.hT = setting.creatHtile(screen, player2.initTile, player2.sequence)
        player3.hT = setting.creatHtile(screen, player3.initTile, player3.sequence)
        player4.hT = setting.creatHtile(screen, player4.initTile, player4.sequence)
        print(player1)
        print(player2)
        print(player3)
        print(player4)
        running = True

        countOfClick = 0
        while running:
            screen.fill((244, 244, 255))


            setting.refreshTileImage(player1,player2,player3,player4)
            square = buttons.square(screen)
            square.blitSelf()
            chi = buttons.chi(screen)
            chi.blitSelf()
            peng = buttons.peng(screen)
            peng.blitSelf()
            gang = buttons.gang(screen)
            gang.blitSelf()
            hu = buttons.hu(screen)
            hu.blitSelf()
            guo = buttons.guo(screen)
            guo.blitSelf()
            runindexList = [1,2,3,4]
            runindex = 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if runindex == 1: # change to player sequence later
                        print(player1.hT)
                        print(len(player1.hT))
                        for i in range(len(player1.hT)):
                            if player1.hT[i].rect.collidepoint(event.pos) and player1.hT[i].status:
                                player1.hT[i].rect.y -= 30
                                player1.hT[i].blitSelf()
                            elif player1.hT[i].rect.collidepoint(event.pos):
                                player1.disTile(player1.hT[i],i)

                                break

                    if tileRect.collidepoint(event.pos):
                        tileRect.y -= 30

            screen.blit(tile, tileRect)
            pygame.display.update()

wnd1()