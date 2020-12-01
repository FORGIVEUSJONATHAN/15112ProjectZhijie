## Course Number: 15112
## Andrew ID: zhijiex
import pygame

class square:
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load("pic/square.png")
        self.image = pygame.transform.smoothscale(self.image,(240,240))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen.get_rect().centerx
        self.rect.centery = self.screen.get_rect().centery
    def blitSelf(self):
        self.screen.blit(self.image,self.rect)

class gang: # gang button
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load("pic/gang.png")
        self.image = pygame.transform.smoothscale(self.image,(55,65))
        self.rect = self.image.get_rect()
        self.rect.topleft = (760,553)
    def blitSelf(self):
        self.screen.blit(self.image,self.rect)

class peng: # peng button
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load("pic/peng.png")
        self.image = pygame.transform.smoothscale(self.image,(55,65))
        self.rect = self.image.get_rect()
        self.rect.topleft = (820,553)
    def blitSelf(self):
        self.screen.blit(self.image,self.rect)

class chi: # chi button
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load("pic/chi.png")
        self.image = pygame.transform.smoothscale(self.image,(55,65))
        self.rect = self.image.get_rect()
        self.rect.topleft = (880,553)
    def blitSelf(self):
        self.screen.blit(self.image,self.rect)


class guo: # guo button
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load("pic/guo.png")
        self.image = pygame.transform.smoothscale(self.image,(55,65))
        self.rect = self.image.get_rect()
        self.rect.topleft = (940,553)
    def blitSelf(self):
        self.screen.blit(self.image,self.rect)

class hu: #hu button
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load("pic/hu.png")
        self.image = pygame.transform.smoothscale(self.image,(55,65))
        self.rect = self.image.get_rect()
        self.rect.topleft = (1000,553)
    def blitSelf(self):
        self.screen.blit(self.image,self.rect)