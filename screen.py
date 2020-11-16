import sys
import pygame
import setting

class wnd1:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("麻将")
        icon = pygame.image.load("pic/tile_type4_300ppi/4-33.png")
        pygame.display.set_icon(icon)
        screen = pygame.display.set_mode((1200, 800),pygame.RESIZABLE)
        start = pygame.image.load("pic/开始.png")
        start = pygame.transform.scale(start, (200, 100))
        startRect = start.get_rect()
        startRect.centerx = screen.get_rect().centerx
        startRect.centery = screen.get_rect().centery
        running = True
        while running:
            screen.fill((255, 123, 255))
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



        running = True
        while running:
            screen.fill((2, 1, 255))
            tileStack111 = setting.tileStack(3)
            pTile1 = setting.drawTile(tileStack111,1)
            setting.showtile(screen,pTile1,1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(tileRect)
                    if tileRect.collidepoint(event.pos):
                        tileRect.y -= 30

            screen.blit(tile, tileRect)
            pygame.display.update()

wnd1()