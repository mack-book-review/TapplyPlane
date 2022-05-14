import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):

    def __init__(self,pos):
        super().__init__()

        self.images = [
            pygame.image.load("images/planeBlue1.png"),
            pygame.image.load("images/planeBlue2.png"),
            pygame.image.load("images/planeBlue3.png"),
        ]

        self.frame = 0
        self.image = self.images[self.frame]

        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.speed = [0,0]
        self.health = 10
        self.points = 0
        self.is_damaged = False
        self.cooldown = 60

    def take_damage(self,damageAmount):
        if not self.is_damaged:
            self.is_damaged = True
            self.health -= damageAmount

            if self.health <= 0:
                self.kill()

    def update(self):
        self.frame = pygame.time.get_ticks() // 60 % len(self.images)
        self.image = self.images[self.frame]

        self.rect.move_ip(self.speed)
        self.speed = [0,0]

        if self.is_damaged:

            self.cooldown -= 0.5
            if self.cooldown <= 0:
                self.is_damaged = False
        else:
            # self.image.set_alpha(0)
            self.cooldown = 60



    def up(self):
        if self.rect.top > 0:
            self.speed[1] = -5

    def down(self):
        if self.rect.bottom < 400:
            self.speed[1] = 5


    def draw(self,screen):
        screen.blit(self.image,self.rect)