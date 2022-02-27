import os
import pygame
from enemy import Enemy
from game_constants import *

walk_imgs = []
die_imgs = []

height = int(314 * 75 / 333 )
width = 75


for x in range(20):
    num_str = str(x)
    if x < 10:
        num_str = "00" + num_str
    else:
        num_str = "0" + num_str
    walk_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Assets/Pictures/ENEMY/4", "4_enemies_1_walk_" + num_str + ".png")) , (width , height)))
    die_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Assets/Pictures/ENEMY/4", "4_enemies_1_die_" + num_str + ".png")) , (width , height)))

    # die_imgs.append(pygame.image.load(os.path.join("Assets/Pictures/ENEMY/7" , "7_enemies_1_die_" + num_str + ".png")))


class Sword(Enemy):
    def __init__(self):
        super().__init__()
        self.level = 2
        self.health = MONSTER_HEALTH[self.level] 
        self.walk_imgs = walk_imgs.copy()
        self.die_imgs  = die_imgs.copy()
        self.rect = self.walk_imgs[0].get_rect()
        self.rect.center = (self.X , self.Y)

