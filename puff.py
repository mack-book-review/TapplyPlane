import pygame
from pygame.locals import *
import random

class Puff(pygame.sprite.Sprite):

    def __init__(self,pos):
        super().__init__()

        smoke_number = random.randint(0,24)
        smoke_number_str = ""
        if smoke_number < 10:
            smoke_number_str = "0" + str(smoke_number)
        else:
            smoke_number_str = str(smoke_number)

        self.image = pygame.image.load("images/blackSmoke{}.png".format(smoke_number_str))
        self.image = pygame.transform.scale(self.image,(30,30))

        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = [random.randint(-5,-1),random.randint(-5,5)]

    def update(self):
        self.rect.move_ip(self.speed)
        if self.rect.left < 0 or self.rect.top < 0:
            self.kill()

    def draw(self,screen):
        screen.blit(self.image,self.rect)