import pygame
import script
import os
import sys
import random
pygame.font.init()


pygame.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
lvl_game = 1
WIDTH = 1280
HEIGHT = 720
FPS = 60
sc = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (28, 170, 200)
MP_BLUE = (0, 0, 255)
from load import *
f1 = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
score = 0
camera_group = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/player_1.png")
        self.rect = self.image.get_rect()

        self.dir = "right"
        self.hp = 100
        self.rect.center = (640, 360)
        self.hp_bar = "blue"
        self.key = pygame.key.get_pressed()
    def move(self):
        if self.key[pygame.K_d]:
            self.rect.centerx += 7
            self.dir = "right"
        if self.key[pygame.K_a]:
            self.rect.centerx -= 7
            self.dir = "left"
        if self.key[pygame.K_w]:
            self.rect.centery -= 7
            self.dir = "top"
        if self.key[pygame.K_s]:
            self.rect.centery += 7
            self.dir = "bottom"


    def update(self):

        self.key = pygame.key.get_pressed()
        self.move()



class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (300, 300)
        self.speed = 6
        self.dir = "right"
        self.timer_moove = 0
        self.timer_shot = 0
        self.triger = True
        self.atack_dir = ''
        self.timer_trigger = 0
        self.start_pos = pygame.math.Vector2(self.rect.center)
        self.end_pos = pygame.math.Vector2(player.rect.center)
        self.velocity = (self.end_pos - self.start_pos).normalize() * self.speed


    def update(self):

        d = ((self.rect.center[0] - player.rect.center[0])**2
            + (self.rect.center[1] - player.rect.center[1])**2) ** (1/2)

        #if d < 300 and self.timer_trigger / FPS > 1:
        #    self.triger = True
        #    print(self.triger)
        #else:
        #    self.triger = False
        #if self.triger == False:
        #    self.timer_trigger += 1

        if self.triger:
            self.start_pos = pygame.math.Vector2(self.rect.center)
            self.end_pos = pygame.math.Vector2(player.rect.center)
            self.velocity = (self.end_pos - self.start_pos).normalize() * self.speed
            self.rect.center += self.velocity








def restart():
    global fon, player1_group ,player_1, enemy_group,player

    player1_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()



    player = Player()
    enemy = Enemy()
    player1_group.add(player)
    enemy_group.add(enemy)
def game_lvl():
    sc.fill(BLACK)
    player1_group.draw(sc)
    player1_group.update()
    enemy_group.draw(sc)
    enemy_group.update()

    pygame.display.update()


restart()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game_lvl()
    clock.tick(FPS)

