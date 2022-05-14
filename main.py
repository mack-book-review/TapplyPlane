import pygame, sys, random
from pygame.locals import *
from player import Player
from rock import Rock
from star import Star
from puff import Puff

pygame.init()
size = (width,height) = (700,400)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Helvetica",20)

background = None
player = None
rocks = pygame.sprite.Group()
stars = pygame.sprite.Group()
smoke_particles = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
star_timer = 1

WHITE = (255,255,255)
BLACK = (0,0,0)

def spawn_star():
    global star_timer
    star_timer += pygame.time.get_ticks()//1000
    if star_timer % 60 == 0:
        star_timer += 1
        star = Star((width,random.randint(0,height)),random.randint(1,3))
        stars.add(star)
        all_sprites.add(star)

def main():
    background = pygame.image.load("images/background.png")
    background = pygame.transform.smoothscale(background,size)

    player = Player((50,height/2))
    all_sprites.add(player)

    for i in range(20):
        rock = Rock(random.randint(0,1))
        rock.rect.left = width + random.randint(0,700)
        rocks.add(rock)
        all_sprites.add(rock)


    health_text = font.render("Health: {}".format(player.health),True,BLACK)
    health_rect = health_text.get_rect()
    health_rect.left = 20
    health_rect.top = 10

    point_text = font.render("Points: {}".format(player.points),True,BLACK)
    point_rect = point_text.get_rect()
    point_rect.right = width - 10
    point_rect.top = 10

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            player.up()
        if keys[K_DOWN]:
            player.down()

        spawn_star()

        if player and  player.is_damaged and player.health > 0:
            puff = Puff((player.rect.centerx-10,player.rect.centery))
            smoke_particles.add(puff)
            all_sprites.add(puff)


        if pygame.sprite.spritecollide(player,rocks,False):
            player.take_damage(1)
            health_text = font.render("Health: {}".format(player.health), True, BLACK)

        hit_list = pygame.sprite.spritecollide(player,stars,True)
        for star in hit_list:
            player.points += star.points
            point_text = font.render("Points: {}".format(player.points), True, BLACK)

        screen.blit(background,background.get_rect())


        all_sprites.update()
        all_sprites.draw(screen)

        screen.blit(health_text,health_rect)
        screen.blit(point_text,point_rect)

        pygame.display.flip()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
