import pygame


class tile:
    def __init__(self,screen,name,status):
        # tile.type
        self.screen = screen
        self.name = name
        self.image = pygame.image.load('pic/tile_type3_300ppi/3-b.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.status = False
        if status: #the tile is selected
            tile.status = status
        else:
            tile.status = False
    def blitSelf(self):
        self.screen.blit(self.image, self.rect)


    def __str__(self):
        return f"Location: {self.rect.x}{self.rect.y}, tile status: {self.status}"

