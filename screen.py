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
        startRect.y = startRect.y+300

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
        global player4, player3, player2, player1
        self.screen = screen
        pygame.display.set_caption("麻将")
        screen = pygame.display.set_mode((1200,800))
        screenRect = screen.get_rect()

        listofPlayer = setting.drawTileAll()

        tileRemain = listofPlayer[0]
        for i in listofPlayer[1:5]: # assign player with corresponding sequence
            if i.sequence == 1:
                player1 = i
            elif i.sequence == 2:
                player2 = i
            elif i.sequence == 3:
                player3 = i
            elif i.sequence == 4:
                player4 = i

        player1.hT = setting.creatHtile(screen, player1.initTile, player1.sequence)
        player2.hT = setting.creatHtile(screen, player2.initTile, player2.sequence)
        player3.hT = setting.creatHtile(screen, player3.initTile, player3.sequence)
        player4.hT = setting.creatHtile(screen, player4.initTile, player4.sequence)

        print(player1)
        print(player2)
        print(player3)
        print(player4)
        running = True
        runindexList = [1, 2, 3, 4]
        runindex = 1
        count = 0
        checkPeng = False # indicator of Peng
        checkGang = 3 # indicator of Gang
        hu = buttons.hu(screen)
        peng = buttons.peng(screen)
        gang = buttons.gang(screen)
        dTListAll = []
        while running:
            screen.fill((244, 244, 255))


            setting.refreshTileImage(player1,player2,player3,player4)
            square = buttons.square(screen)
            square.blitSelf()
            # chi = buttons.chi(screen)
            # chi.blitSelf()

            # hu = buttons.hu(screen)
            # hu.blitSelf()
            # guo = buttons.guo(screen)
            # guo.blitSelf()

            dTListAll = setting.getdTAll(player1,player2,player3,player4)

            # check 自摸
            if runindex == 1 and setting.checkwin(player1.get_hTNameList()):
                hu.blitSelf()
            elif runindex == 2 and setting.checkwin(player2.get_hTNameList()):
                wnd5Lost(screen,"Player 2 won!!!")
            elif runindex == 3 and setting.checkwin(player3.get_hTNameList()):
                wnd5Lost(screen,"Player 3 won!!!")
            elif runindex == 4 and setting.checkwin(player4.get_hTNameList()):
                wnd5Lost(screen,"Player 3 won!!!")



            if runindex == 1 and player4.dT != []: # check the peng option
                if player1.checkPeng(player4):
                    peng.blitSelf()
                    checkPeng = True

                elif player2.checkPeng(player4):
                    print("要碰了")
                    runindex = 2
                    setting.pengAction(screen, player2, player4)


                elif player3.checkPeng(player4):
                    print("要碰了")
                    runindex = 3
                    setting.pengAction(screen, player3, player4)


            elif runindex == 2 and player1.dT != []:
                if player2.checkPeng(player1):
                    print("要碰了")
                    runindex = 2
                    setting.pengAction(screen, player2, player1)

                elif player3.checkPeng(player1):
                    print("要碰了")
                    runindex = 3
                    setting.pengAction(screen, player3, player1)


                elif player4.checkPeng(player1):
                    print("要碰了")
                    runindex = 4
                    setting.pengAction(screen, player4, player1)


            elif runindex == 3 and player2.dT != []:
                if player1.checkPeng(player2):
                    peng.blitSelf()
                    checkPeng = True

                elif player3.checkPeng(player2):
                    print("要碰了")
                    runindex = 3
                    setting.pengAction(screen, player3, player2)


                elif player4.checkPeng(player2):
                    print("要碰了")
                    runindex = 4


            elif runindex == 4 and player3.dT != []:
                if player1.checkPeng(player3):
                    peng.blitSelf()
                    checkPeng = True

                elif player2.checkPeng(player3):
                    print("要碰了")
                    runindex = 2
                    setting.pengAction(screen, player2, player3)


                elif player4.checkPeng(player3):
                    print("要碰了")
                    runindex = 4
                    setting.pengAction(screen, player4, player3)


            else:
                checkPeng = False

            if runindex == 1 and player4.dT != []:  # check the peng option
                if player1.checkGang(player4) in [1,2]:
                    print("能gang")
                    gang.blitSelf()
                    checkGang = player1.checkGang(player4)

                elif player2.checkGang(player4) == 1:
                    print("要杠了")
                    runindex = 2
                    setting.gangAction1(screen, player2, player4)
                    player2.drawATile(screen, tileRemain)

                elif player3.checkGang(player4) == 1:
                    print("要杠了")
                    runindex = 3
                    setting.gangAction1(screen, player3, player4)
                    player4.drawATile(screen, tileRemain)


            elif runindex == 2 and player1.dT !=[]:
                if player2.checkGang(player1) == 1:
                    print("要杠了")
                    runindex = 2
                    setting.gangAction1(screen, player2, player1)
                    player2.drawATile(screen, tileRemain)

                elif player3.checkGang(player1) == 1:
                    print("要杠了")
                    runindex = 3
                    setting.gangAction1(screen, player3, player1)
                    player3.drawATile(screen, tileRemain)

                elif player4.checkGang(player1) == 1:
                    print("要杠了")
                    runindex = 4
                    setting.gangAction1(screen, player4, player1)
                    player4.drawATile(screen, tileRemain)


            elif runindex == 3 and player2.dT != []:
                if player1.checkGang(player2) in [1,2] :
                    print("能gang")
                    gang.blitSelf()
                    checkGang = player1.checkGang(player2)

                elif player3.checkGang(player2) == 1:
                    print("要杠了")
                    runindex = 3
                    setting.gangAction1(screen, player3, player2)
                    player3.drawATile(screen, tileRemain)

                elif player4.checkGang(player2) == 1:
                    print("要杠了")
                    runindex = 4
                    setting.gangAction1(screen, player4, player2)
                    player4.drawATile(screen, tileRemain)


            elif runindex == 4 and player3.dT != []:
                if player1.checkGang(player3) in [1,2]:
                    print("能gang")
                    gang.blitSelf()
                    checkGang = player1.checkGang(player3)
                    player1.drawATile(screen, tileRemain)

                elif player2.checkGang(player3) == 1:
                    print("要杠了")
                    runindex = 2
                    setting.gangAction1(screen, player2, player3)
                    player2.drawATile(screen, tileRemain)

                elif player4.checkGang(player1) == 1:
                    print("要杠了")
                    runindex = 4
                    setting.gangAction1(screen, player4, player3)
                    player4.drawATile(screen, tileRemain)
            else:
                checkGang = 3


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if hu.rect.collidepoint(event.pos):
                        wnd3Win(screen)
                    if peng.rect.collidepoint(event.pos) and checkPeng == True: # 解决按空白处的问题
                        if runindex == 1:
                            setting.pengAction(screen,player1,player4)
                            runindex = 1
                            checkPeng = False
                        elif runindex == 3:
                            setting.pengAction(screen, player1, player2)
                            runindex = 1
                            checkPeng = False
                        elif runindex == 4:
                            setting.pengAction(screen, player1, player3)
                            runindex = 1
                            checkPeng = False

                    elif gang.rect.collidepoint(event.pos):
                        if checkGang == 1:
                            if runindex == 1:
                                setting.gangAction1(screen, player1, player4)
                                player1.drawATile(screen, tileRemain)
                                runindex = 1
                                checkGang = False
                            elif runindex == 3:
                                runindex = 1
                                checkGang = False
                            elif runindex == 4:
                                setting.gangAction1(screen, player1, player3)
                                runindex = 1
                                checkGang = False
                        elif checkGang == 2:
                                setting.gangAction2(screen,player1)
                        player1.drawATile(screen, tileRemain) # after gang player 1 need to draw a card to maintain the balance

                    elif runindex == 1: # change to player sequence later
                        # print(player1.hT)
                        # if len(player1.hT)<14:
                        #     player1.drawATile(screen, tileRemain)
                        for i in range(len(player1.hT)):
                            if player1.hT[i].rect.collidepoint(event.pos) and player1.hT[i].status == False: # selected a tile
                                player1.hT[i].rect.top -= 30
                                player1.hT[i].blitSelf()
                                player1.hT[i].status = True
                                for x in range(len(player1.hT)): # deselect other tile which have been selected
                                    if player1.hT[x].status == True and x!=i:
                                        player1.hT[x].rect.top += 30
                                        player1.hT[x].blitSelf()
                                        player1.hT[x].status = False
                                break
                            elif player1.hT[i].rect.collidepoint(event.pos) and player1.hT[i].status: # click on the selected tile and discard it
                                print(len(player1.dT))
                                setting.creatDtile(screen,player1.hT[i],player1.dT,1)
                                player1.disTile(player1.hT[i],i)
                                count = count + 1 # count the number of discarded tile

                                if player2.checkHuCong(player1):
                                    wnd5Lost(screen, "You let Player 2 win!!!")
                                elif player3.checkHuCong(player1):
                                    wnd5Lost(screen, "You let Player 3 win!!!")
                                elif player4.checkHuCong(player1):
                                    wnd5Lost(screen, "You let Player 4 win!!!")

                                runindex = 2
                                if player2.drawATile(screen,tileRemain) == False: # check for a tied game
                                    wnd4Tied(screen)
                                print(len(player1.hT))
                                break
                    elif runindex == 2:
                        dTname = player2.disTileName(dTListAll)
                        player2.disTileAct(screen,dTname)
                        # player2.disTileRandom(screen) # player 2 discard a card
                        if player1.checkHuCong(player2):
                            hu.blitSelf()
                        elif player3.checkHuCong(player2):
                            wnd5Lost(screen, "Player 2 let Player 3 win!!!")
                        elif player4.checkHuCong(player2):
                            wnd5Lost(screen, "Player 2 let Player 4 win!!!")

                        runindex = 3
                        if player3.drawATile(screen, tileRemain) == False:# check for a tied game
                            wnd4Tied(screen)

                    elif runindex == 3:
                        dTname = player3.disTileName(dTListAll)
                        player3.disTileAct(screen, dTname)
                        # player3.disTileRandom(screen) # player 3 discard a card
                        if player1.checkHuCong(player3):
                            hu.blitSelf()
                        elif player2.checkHuCong(player3):
                            wnd5Lost(screen, "Player 3 let Player 2 win!!!")
                        elif player4.checkHuCong(player3):
                            wnd5Lost(screen, "Player 3 let Player 4 win!!!")

                        runindex = 4
                        if player4.drawATile(screen, tileRemain) == False:# check for a tied game
                            wnd4Tied(screen)

                    elif runindex == 4:
                        dTname = player4.disTileName(dTListAll)
                        player4.disTileAct(screen, dTname)

                        # player4.disTileRandom(screen) # player 4 discard a card
                        if player1.checkHuCong(player4):
                            hu.blitSelf()
                        elif player2.checkHuCong(player4):
                            wnd5Lost(screen, "Player 4 let Player 2 win!!!")
                        elif player3.checkHuCong(player4):
                            wnd5Lost(screen, "Player 4 let Player 3 win!!!")

                        runindex = 1
                        if player1.drawATile(screen, tileRemain) == False: # check for a tied game
                            wnd4Tied(screen)

            pygame.display.update()

class wnd3Win:
    def __init__(self,screen):
        pygame.display.set_caption("麻将")
        win = pygame.image.load("pic/Congratulation.png")
        winRect = win.get_rect()
        winRect.centerx = screen.get_rect().centerx
        winRect.centery = screen.get_rect().centery
        restart = pygame.image.load("pic/restart.png")
        restartRect = restart.get_rect()
        restartRect.left = screen.get_rect().left
        restartRect.top = screen.get_rect().bottom - 115
        quit = pygame.image.load("pic/quit.png")
        quitRect = quit.get_rect()
        quitRect.right = screen.get_rect().right
        quitRect.top = restartRect.top

        running = True
        while running:
            screen.fill((146, 168, 209))
            screen.blit(win,winRect)
            screen.blit(restart,restartRect)
            screen.blit(quit,quitRect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if restartRect.collidepoint(event.pos):
                        wnd2(screen)
                    elif quitRect.collidepoint(event.pos):
                        sys.exit()
            pygame.display.update()


class wnd4Tied:
    def __init__(self,screen):
        pygame.display.set_caption("麻将")
        tied = pygame.image.load("pic/Tied.png")
        tiedRect = tied.get_rect()
        tiedRect.centerx = screen.get_rect().centerx
        tiedRect.centery = screen.get_rect().centery
        restart = pygame.image.load("pic/restart.png")
        restartRect = restart.get_rect()
        restartRect.left = screen.get_rect().left
        restartRect.top = screen.get_rect().bottom - 115
        quit = pygame.image.load("pic/quit.png")
        quitRect = quit.get_rect()
        quitRect.right = screen.get_rect().right
        quitRect.top = restartRect.top

        running = True
        while running:
            screen.fill((146, 168, 209))
            screen.blit(tied,tiedRect)
            screen.blit(restart,restartRect)
            screen.blit(quit,quitRect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if restartRect.collidepoint(event.pos):
                        wnd2(screen)
                    elif quitRect.collidepoint(event.pos):
                        sys.exit()
            pygame.display.update()

class wnd5Lost:
    def __init__(self,screen,playerName):
        pygame.display.set_caption(playerName)
        win = pygame.image.load("pic/Lost.png")
        winRect = win.get_rect()
        winRect.centerx = screen.get_rect().centerx
        winRect.centery = screen.get_rect().centery
        restart = pygame.image.load("pic/restart.png")
        restartRect = restart.get_rect()
        restartRect.left = screen.get_rect().left
        restartRect.top = screen.get_rect().bottom - 115
        quit = pygame.image.load("pic/quit.png")
        quitRect = quit.get_rect()
        quitRect.right = screen.get_rect().right
        quitRect.top = restartRect.top

        running = True
        while running:
            screen.fill((146, 168, 209))
            screen.blit(win,winRect)
            screen.blit(restart,restartRect)
            screen.blit(quit,quitRect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if restartRect.collidepoint(event.pos):
                        wnd2(screen)
                    elif quitRect.collidepoint(event.pos):
                        sys.exit()
            pygame.display.update()


wnd1()