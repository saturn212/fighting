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
WIDTH = 1200
HEIGHT = 600
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

class FON:
    def __init__(self):
        self.timer = 0
        self.frame = 0
        self.image = fon_image

    def update(self):
        self.timer += 2
        sc.blit(self.image[self.frame], (0, 0))
        if self.timer / FPS > 0.1:
            if self.frame == len(self.image) - 1:
                self.frame = 0
            else:
                self.frame += 1
            self.timer = 0

class Player_1(pygame.sprite.Sprite):
    def __init__(self, image_lists):
        pygame.sprite.Sprite.__init__(self)
        self.image_lists = image_lists
        self.image = self.image_lists['idle'][0]
        self.current_list_image = self.image_lists['idle']
        self.rect = self.image.get_rect()
        self.anime_idle = True
        self.anime_run = False
        self.anime_attack = False
        self.frame = 0
        self.timer_anime = 0
        self.dir = "right"
        self.hp = 100
        self.jump_step = -20
        self.jump = False
        self.flag_damage = False
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_outline = self.mask.outline()
        self.mask_list = []
        self.rect.center = (200, 370)
        self.hp_bar = "blue"
        self.key = pygame.key.get_pressed()
    def move(self):
        if self.key[pygame.K_d]:
            self.rect.x += 2
            self.anime_idle = False
            if not self.anime_attack:
                self.anime_run = True
        elif self.key[pygame.K_a]:
            self.rect.x -= 2
            self.anime_idle = False
            if not self.anime_attack:
                self.anime_run = True

        else:
            if not self.anime_attack:
                self.anime_idle = True
            self.anime_run = False
    def jumps(self):
        if self.key[pygame.K_SPACE]:
            self.jump = True
        if self.jump:
            if self.jump_step <= 20:
                self.rect.y += self.jump_step
                self.jump_step += 1
            else:
                self.jump = False
                self.jump_step = -20
    def attack(self):
        if self.key[pygame.K_e] and not self.anime_attack:
            self.frame = 0
            self.anime_attack = True
            self.anime_idle = False
            self.anime_run = False
            self.flag_damage = True
            self.current_list_image = self.image_lists['attack']
    def attack2(self):
        if self.key[pygame.K_f] and not self.anime_attack:
            self.frame = 0
            self.anime_attack = True
            self.anime_idle = False
            self.anime_run = False
            self.flag_damage = True
            self.current_list_image = self.image_lists['attack 2']
    def animation(self):
        self.timer_anime += 2
        if self.timer_anime / FPS > 0.1:
            if self.frame == len(self.current_list_image) - 1:
                self.frame = 8
                if self.anime_attack:
                    self.current_list_image = pl1_idle_image
                    self.anime_attack = False
                    self.anime_idle = True
            else:
                self.frame += 1
            self.timer_anime = 0
        if self.anime_idle:
            self.current_list_image = self.image_lists['idle']
        elif self.anime_run:
            self.current_list_image = self.image_lists['run']
        #elif self.anime_attack:
        #    self.current_list_image = self.image_lists['attack']
        #elif self.anime_attack:
        #    self.current_list_image = self.image_lists['attack 2']
        try:
            if self.dir == "right":
                self.image = self.current_list_image[self.frame]
            else:
                self.image = pygame.transform.flip(self.current_list_image[self.frame], True, False)
        except:
            self.frame = 0
    def draw_hp_bar(self):
        pygame.draw.rect(sc, self.hp_bar, (0, 0, 600 * self.hp / 100, 50))

    def update(self):
        if self.rect.center[0] - player_2.rect.center[0] < 0:
            self.dir = "right"
        else:
            self.dir = "left"
        self.key = pygame.key.get_pressed()
        self.move()
        self.animation()
        self.attack()
        self.jumps()
        self.draw_hp_bar()
        self.attack2()

class Player_2(pygame.sprite.Sprite):
    def __init__(self, image_lists):
        pygame.sprite.Sprite.__init__(self)
        self.image_lists = image_lists
        self.image = self.image_lists['idle'][0]
        self.current_list_image = self.image_lists['idle']
        self.rect = self.image.get_rect()
        self.anime_idle = True
        self.anime_run = False
        self.anime_attack = False
        self.frame = 0
        self.timer_anime = 0
        self.dir = "left"
        self.hp = 100
        self.jump_step = -20
        self.jump = False
        self.flag_damage = False
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_outline = self.mask.outline()
        self.mask_list = []
        self.rect.center = (1000, 370)
        self.hp_bar = "red"
        self.key = pygame.key.get_pressed()

    def move(self):
        if self.key[pygame.K_RIGHT]:
            self.rect.x += 2
            self.anime_idle = False
            if not self.anime_attack:
                self.anime_run = True
        elif self.key[pygame.K_LEFT]:
            self.rect.x -= 2
            self.anime_idle = False
            if not self.anime_attack:
                self.anime_run = True

        else:
            if not self.anime_attack:
                self.anime_idle = True
            self.anime_run = False

    def jumps(self):
        if self.key[pygame.K_UP]:
            self.jump = True
        if self.jump:
            if self.jump_step <= 20:
                self.rect.y += self.jump_step
                self.jump_step += 1
            else:
                self.jump = False
                self.jump_step = -20

    def attack(self):
        if self.key[pygame.K_e] and not self.anime_attack:
            self.frame = 0
            self.anime_attack = True
            self.anime_idle = False
            self.anime_run = False
            self.flag_damage = True



    def animation(self):
        self.timer_anime += 2
        if self.timer_anime / FPS > 0.1:
            if self.frame == len(self.current_list_image) - 1:
                self.frame = 8
                if self.anime_attack:
                    self.current_list_image = pl1_idle_image
                    self.anime_attack = False
                    self.anime_idle = True
                else:
                    self.frame += 1
                self.timer_anime = 0
            if self.anime_idle:
                self.current_list_image = self.image_lists['idle']
            elif self.anime_run:
                self.current_list_image = self.image_lists['run']
            elif self.anime_attack:
                self.current_list_image = self.image_lists['attack']
            try:
                if self.dir == "rigth":
                    self.image = self.current_list_image[self.frame]
                else:
                    self.image = pygame.transform.flip(self.current_list_image[self.frame], True, False)
            except:
                self.frame = 0

    def draw_hp_bar(self):
        pygame.draw.rect(sc, self.hp_bar, (0, 0, 600 * self.hp / 100, 50))

    def update(self):
        if self.rect.center[0] - player_1.rect.center[0] < 0:
            self.dir = "right"
        else:
            self.dir = "left"
        self.key = pygame.key.get_pressed()
        self.move()
        self.animation()
        self.attack()
        self.jumps()
        self.draw_hp_bar()




def restart():
    global fon, player1_group, player2_group,player_2,player_1

    player1_group = pygame.sprite.Group()
    player2_group = pygame.sprite.Group()
    fon = FON()

    player_1 = Player_1({'run': pl1_run_image, 'idle': pl1_idle_image, 'attack': pl1_attack_image, 'attack 2': pl1_attack2_image})
    player_2 = Player_2({'run': pl2_run_image, 'idle': pl2_idle_image, 'attack': pl2_attack_image})
    player1_group.add(player_1)
    player2_group.add(player_2)
def game_lvl():
    fon.update()
    player1_group.draw(sc)
    player1_group.update()

    player2_group.draw(sc)
    player2_group.update()
    # sc.fill(BLACK)
    pygame.display.update()


restart()
# drawMaps('1.txt')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game_lvl()
    clock.tick(FPS)

update()