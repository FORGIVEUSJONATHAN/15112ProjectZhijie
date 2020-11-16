import pygame


class tile:
    def __init__(self,screen,name,status):
        # tile.type
        self.screen = screen
        self.name = name
        self.image = pygame.image.load('pic/tile_type3_300ppi/3-b.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        if status: #the tile is selected
            tile.status = status
        else:
            tile.status = False
    def blitSelf(self):
        self.screen.blit(self.image, self.rect)




