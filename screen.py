
## Course Number: 15112
## Andrew ID: zhijiex

import sys
import pygame
import setting
import buttons

class wnd1:
    def __init__(self):
        #set up the screen display, the icon, and the caption
        pygame.init()
        pygame.display.set_caption("麻将")
        icon = pygame.image.load("pic/tile_type4_300ppi/4-33.png")
        pygame.display.set_icon(icon)
        screen = pygame.display.set_mode((1200, 800),pygame.RESIZABLE)
        start = pygame.image.load("pic/Start.png") # start button
        start = pygame.transform.scale(start, (200, 100))
        startRect = start.get_rect()
        startRect.centerx = screen.get_rect().centerx
        startRect.centery = screen.get_rect().centery
        startRect.y = startRect.y+300
        startImg = pygame.image.load("pic/StartImg.png")
        startImg = pygame.transform.smoothscale(startImg,(625,300))
        startImgRect = startImg.get_rect()
        startImgRect.centerx = screen.get_rect().centerx
        startImgRect.centery = screen.get_rect().centery
        running = True
        while running:
            screen.fill((146, 168, 209))
            screen.blit(start, startRect)
            screen.blit(startImg, startImgRect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if startRect.collidepoint(event.pos): # clicking the start button will enter the game
                        wnd2(screen)
            pygame.display.update()


class wnd2:
    def __init__(self,screen):

        global player4, player3, player2, player1
        self.screen = screen
        pygame.display.set_caption("麻将")
        screen = pygame.display.set_mode((1200,800))
        pygame.mixer.music.load('sound/BackGround.mp3') # load the background music
        pygame.mixer.music.play(-1) # play the background music
        pygame.mixer.music.set_volume(0.10) # set bgm volume
        pengSound = pygame.mixer.Sound('sound/PengSound.wav') # load peng sound effect
        gangSound = pygame.mixer.Sound('sound/GangSound.wav') # load gang sound effect
        listofPlayer = setting.drawTileAll() # create tile stack and 4 players
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


        running = True
        runindex = 1
        checkPeng = False # indicator of Peng
        checkGang = 3 # indicator of Gang, 1: True with type1, 2: True with type 2, 3: False
        checkHu = False # indicator of winning
        checkP1Draw = True # player 1 can draw or not 
        checkP2Draw = True # player 2 can draw or not 
        checkP3Draw = True # player 3 can draw or not 
        checkP4Draw = True # player 4 can draw or not 
        hu = buttons.hu(screen) # create the button of hu
        peng = buttons.peng(screen) # create the button of peng
        gang = buttons.gang(screen) # create the button of gang
        dTListAll = [] # all the discarded tiles list
        while running:
            screen.fill((244, 244, 255))


            setting.refreshTileImage(player1,player2,player3,player4) # refresh tile images
            
            square = buttons.square(screen) 
            square.blitSelf()
            
            dTListAll = setting.getdTAll(player1,player2,player3,player4) # all the discarded tiles list

            # check 自摸
            if runindex == 1 and setting.checkwin(player1.get_hTNameList()): # check player 1 winning by drawing a tile
                hu.blitSelf()
                checkHu = True
            elif runindex == 2 and setting.checkwin(player2.get_hTNameList()): # check player 2 winning by drawing a tile
                wnd5Lost(screen,"Player 2 won!!!")
            elif runindex == 3 and setting.checkwin(player3.get_hTNameList()): # check player 3 winning by drawing a tile
                wnd5Lost(screen,"Player 3 won!!!")
            elif runindex == 4 and setting.checkwin(player4.get_hTNameList()): # check player 4 winning by drawing a tile
                wnd5Lost(screen,"Player 4 won!!!")
            else: # no players win by drawing a tile
                checkHu = False

            # this session is for check peng action,
            # if check peng is True and the player is not 1,
            # Peng Action will take place
            if runindex == 1 and player4.dT != []: # check runindex and whether the player has dT
                if player1.checkPeng(player4): # check peng option
                    peng.blitSelf()
                    checkP1Draw = False

                elif player2.checkPeng(player4):# check peng option
                    print("2Peng4")
                    runindex = 2
                    setting.pengAction(screen, player2, player4)
                    pengSound.play()
                    checkP2Draw = False

                elif player3.checkPeng(player4):# check peng option
                    print("3Peng4")
                    runindex = 3
                    setting.pengAction(screen, player3, player4)
                    pengSound.play()
                    checkP3Draw = False

                checkPeng = True


            elif runindex == 2 and player1.dT != []: # check runindex and whether the player has dT
                if player2.checkPeng(player1):# check peng option
                    print("2Peng1")
                    runindex = 2
                    setting.pengAction(screen, player2, player1)
                    pengSound.play()
                    checkP2Draw = False

                elif player3.checkPeng(player1):# check peng option
                    print("3Peng1")
                    runindex = 3
                    setting.pengAction(screen, player3, player1)
                    pengSound.play()
                    checkP3Draw = False

                elif player4.checkPeng(player1):# check peng option
                    print("4Peng1")
                    runindex = 4
                    setting.pengAction(screen, player4, player1)
                    pengSound.play()
                    checkP4Draw = False

                checkPeng = True


            elif runindex == 3 and player2.dT != []: # check runindex and whether the player has dT
                if player1.checkPeng(player2): # check peng option
                    peng.blitSelf()
                    checkP1Draw = False

                elif player3.checkPeng(player2): # check peng option
                    print("3Peng2")
                    runindex = 3
                    setting.pengAction(screen, player3, player2)
                    pengSound.play()
                    checkP3Draw = False

                elif player4.checkPeng(player2): # check peng option
                    print("4Peng2")
                    runindex = 4
                    setting.pengAction(screen, player4, player2)
                    pengSound.play()
                    checkP4Draw = False

                checkPeng = True

            elif runindex == 4 and player3.dT != []: # check runindex and whether the player has dT
                if player1.checkPeng(player3): # check peng option
                    peng.blitSelf()
                    checkP1Draw = False

                elif player2.checkPeng(player3): # check peng option
                    print("2Peng3")
                    runindex = 2
                    setting.pengAction(screen, player2, player3)
                    pengSound.play()
                    checkP2Draw = False

                elif player4.checkPeng(player3): # check peng option
                    print("4Peng3")
                    runindex = 4
                    setting.pengAction(screen, player4, player3)
                    pengSound.play()
                    checkP4Draw = False
                checkPeng = True


            else:
                checkPeng = False

            # this session is for check gang action,
            # if check gang is True and the player is not 1,
            # gang Action will take place,
            # Gang Action will be divided into type 1 and type2
            # both action will allow player to draw an extra tile

            if runindex == 1 and player4.dT != []:  # check runindex and whether the player has dT
                if player1.checkGang(player4) in [1,2]:
                    print("能gang")
                    gang.blitSelf()
                    checkGang = player1.checkGang(player4)

                elif player2.checkGang(player4) in [1,2]:
                    print("2Gang4")
                    runindex = 2
                    setting.gangAction1(screen, player2, player4)
                    gangSound.play()
                    player2.drawATile(screen, tileRemain)
                    print("2 draw a tile")

                elif player3.checkGang(player4) in [1,2]:
                    print("3Gang4")
                    runindex = 3
                    setting.gangAction1(screen, player3, player4)
                    gangSound.play()
                    player3.drawATile(screen, tileRemain)
                    print("3 draw a tile")


            elif runindex == 2 and player1.dT !=[]:
                if player2.checkGang(player1) == 1:
                    print("Gang")
                    runindex = 2
                    setting.gangAction1(screen, player2, player1)
                    gangSound.play()
                    player2.drawATile(screen, tileRemain)
                    print("2 draw a tile")

                elif player3.checkGang(player1) == 1:
                    print("3Gang1")
                    runindex = 3
                    setting.gangAction1(screen, player3, player1)
                    gangSound.play()
                    player3.drawATile(screen, tileRemain)
                    print("3 draw a tile")

                elif player4.checkGang(player1) == 1:
                    print("4Gang1")
                    runindex = 4
                    setting.gangAction1(screen, player4, player1)
                    gangSound.play()
                    player4.drawATile(screen, tileRemain)
                    print("4 draw a tile")


            elif runindex == 3 and player2.dT != []:
                if player1.checkGang(player2) in [1,2] :
                    print("gang")
                    gang.blitSelf()
                    checkGang = player1.checkGang(player2)

                elif player3.checkGang(player2) == 1:
                    print("3Gang2")
                    runindex = 3
                    setting.gangAction1(screen, player3, player2)
                    gangSound.play()
                    player3.drawATile(screen, tileRemain)
                    print("3 draw a tile")

                elif player4.checkGang(player2) == 1:
                    print("4Gang2")
                    runindex = 4
                    setting.gangAction1(screen, player4, player2)
                    gangSound.play()
                    player4.drawATile(screen, tileRemain)
                    print("4 draw a tile")


            elif runindex == 4 and player3.dT != []:
                if player1.checkGang(player3) in [1,2]:
                    print("能gang")
                    gang.blitSelf()
                    checkGang = player1.checkGang(player3)

                elif player2.checkGang(player3) == 1:
                    print("2Gang3")
                    runindex = 2
                    setting.gangAction1(screen, player2, player3)
                    gangSound.play()
                    player2.drawATile(screen, tileRemain)
                    # checkP2Draw = False

                    print("2 draw a tile")

                elif player4.checkGang(player3) == 1:
                    print("4Gang3")
                    runindex = 4
                    setting.gangAction1(screen, player4, player3)
                    gangSound.play()
                    player4.drawATile(screen, tileRemain)
                    # checkP4Draw = False

                    print("4 draw a tile")

            else:
                checkGang = 3



            # check for the mouse click action
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN: # if the player clicked the button
                    if hu.rect.collidepoint(event.pos) and checkHu == True: # check whether player 1 clicked the win button
                        wnd3Win(screen)

                    if peng.rect.collidepoint(event.pos) and checkPeng == True: # check whether player 1 clicked the peng button
                        if runindex == 1: # the current running index 1
                            print("1Peng4")
                            setting.pengAction(screen,player1,player4)
                            pengSound.play()
                            runindex = 1
                            checkPeng = False
                        elif runindex == 3: # the current running index 3
                            print("1Peng2")
                            setting.pengAction(screen, player1, player2)
                            pengSound.play()
                            runindex = 1
                            checkPeng = False
                        elif runindex == 4:  # the current running index 4
                            print("1Peng3")
                            setting.pengAction(screen, player1, player3)
                            pengSound.play()
                            runindex = 1
                            checkPeng = False

                    elif gang.rect.collidepoint(event.pos) and checkGang in [1,2]: #check whether player 1 clicked the Gang Action
                        if checkGang == 1: # if check gang is 1
                            if runindex == 1:
                                setting.gangAction1(screen, player1, player4)
                                gangSound.play()
                                runindex = 1
                                checkGang = 3 # check gang is not available next time
                            elif runindex == 3:
                                setting.gangAction1(screen, player1, player2)
                                gangSound.play()
                                runindex = 1
                                checkGang = 3 # check gang is not available next time
                            elif runindex == 4:
                                setting.gangAction1(screen, player1, player3)
                                gangSound.play()
                                runindex = 1
                                checkGang = 3 # check gang is not available next time
                        elif checkGang == 2: # if check gang is 2, has 4 tiles on hand, player index must be one
                                setting.gangAction2(screen,player1)
                                gangSound.play()

                        player1.drawATile(screen, tileRemain) # after gang player 1 need to draw a card to maintain the balance
                        print("1 draw a tile")
                    if runindex == 1: # player 1 round
                        if  checkP1Draw == True:
                            if player1.drawATile(screen, tileRemain) == False: # check for a tied game or player 1 draw a tile
                                wnd4Tied(screen)
                            else:
                                print("1 draw a tile")
                        checkP1Draw = True

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
                                setting.creatDtile(screen,player1.hT[i],player1.dT,1) #add the tile into dT
                                player1.disTile(player1.hT[i],i) #remove the tile from hT
                                print("1 discarded a tile")
                                if player2.checkHuCong(player1): # if discarded Tile let player 2 win
                                    wnd5Lost(screen, "You let Player 2 win!!!")
                                elif player3.checkHuCong(player1): # if discarded Tile let player 3 win
                                    wnd5Lost(screen, "You let Player 3 win!!!")
                                elif player4.checkHuCong(player1): # if discarded Tile let player 4 win
                                    wnd5Lost(screen, "You let Player 4 win!!!")

                                runindex = 2 # move index to the next player

                                break

                    elif runindex == 2: # player 2 round
                        if  checkP2Draw == True:
                            if player2.drawATile(screen,tileRemain) == False:  # check for a tied game or player 2 draw a tile
                                wnd4Tied(screen)
                            else:
                                print("2 draw a tile")
                        dTname = player2.disTileName(dTListAll) # get the intended discard tile's name
                        player2.disTileAct(screen,dTname) # remove tile from dT, add tile to hT
                        print("2 discarded a tile")
                        checkP2Draw = True

                        # player2.disTileRandom(screen) # player 2 discard a random card
                        if player1.checkHuCong(player2): # check whether player 2 let player 1 win
                            hu.blitSelf()
                            checkHu = True
                        elif player3.checkHuCong(player2):  # check whether player 2 let player 3 win
                            wnd5Lost(screen, "Player 2 let Player 3 win!!!")
                        elif player4.checkHuCong(player2):  # check whether player 2 let player 4 win
                            wnd5Lost(screen, "Player 2 let Player 4 win!!!")

                        runindex = 3

                    elif runindex == 3: # player 3 round
                        if checkP3Draw == True:
                            if player3.drawATile(screen, tileRemain) == False and checkPeng:# check for a tied game or player 3 draw a tile
                                wnd4Tied(screen)
                            else:
                                print("3 draw a tile")
                        dTname = player3.disTileName(dTListAll) # get the intended discard tile's name
                        player3.disTileAct(screen, dTname) # remove tile from dT, add tile to hT
                        print("3 discarded a tile")
                        checkP3Draw = True

                        # player3.disTileRandom(screen) # player 3 discard a card
                        if player1.checkHuCong(player3): # check whether player 3 let player 1 win
                            hu.blitSelf()
                            checkHu = True
                        elif player2.checkHuCong(player3): # check whether player 3 let player 2 win
                            wnd5Lost(screen, "Player 3 let Player 2 win!!!")
                        elif player4.checkHuCong(player3):# check whether player 3 let player 4 win
                            wnd5Lost(screen, "Player 3 let Player 4 win!!!")

                        runindex = 4


                    elif runindex == 4: # player 4 round
                        if checkP4Draw == True:
                            if player4.drawATile(screen, tileRemain) == False:# check for a tied game or player 4 draw a tile
                                wnd4Tied(screen)
                            else:
                                print("4 draw a tile")
                        dTname = player4.disTileName(dTListAll)# get the intended discard tile's name
                        player4.disTileAct(screen, dTname) # remove tile from dT, add tile to hT
                        print("4 discarded a tile")
                        # player4.disTileRandom(screen) # player 4 discard a card
                        checkP4Draw = True
                        if player1.checkHuCong(player4): # check whether player 4 let player 1 win
                            hu.blitSelf()
                            checkHu = True
                        elif player2.checkHuCong(player4): # check whether player 4 let player 2 win
                            wnd5Lost(screen, "Player 4 let Player 2 win!!!")
                        elif player3.checkHuCong(player4): # check whether player 4 let player 3 win
                            wnd5Lost(screen, "Player 4 let Player 3 win!!!")

                        runindex = 1

            pygame.display.update()

class wnd3Win: # Wining page for player 1
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
        pygame.mixer.music.load('sound/Victory.wav') # Sound Effect
        pygame.mixer.music.play(-1)
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
                    if restartRect.collidepoint(event.pos): # click restart image to restart the game
                        wnd2(screen)
                    elif quitRect.collidepoint(event.pos): # click the quit image to quit the game
                        sys.exit()
            pygame.display.update()


class wnd4Tied: # Tied page if no one win
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
        pygame.mixer.music.load('sound/Tied.wav') # Sound Effect
        pygame.mixer.music.play(-1)
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
                    if restartRect.collidepoint(event.pos):# click restart image to restart the game
                        wnd2(screen)
                    elif quitRect.collidepoint(event.pos):# click the quit image to quit the game
                        sys.exit()
            pygame.display.update()

class wnd5Lost: # lost page
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
        pygame.mixer.music.load('sound/Lost.wav') # Sound Effect
        pygame.mixer.music.play(-1)
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
                    if restartRect.collidepoint(event.pos):# click restart image to restart the game
                        wnd2(screen)
                    elif quitRect.collidepoint(event.pos): # click the quit image to quit the game
                        sys.exit()
            pygame.display.update()

wnd1()