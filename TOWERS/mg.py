import os
import pygame
from tower import Tower

imgs = []
base_img_disp = [(6,16) , (0 , 16) , (7,16)]
imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Assets/Pictures/TOWERS" , "MG.png")) , (35 , 35 * 229 / 110)).convert_alpha())
imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Assets/Pictures/TOWERS" , "MG2.png")) , (60 , 60 * 239 / 218)).convert_alpha())
imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Assets/Pictures/TOWERS" , "MG3.png")) , (50 , 50 * 259 / 166)).convert_alpha())

class Mg(Tower):
    def __init__(self, level, x, y):
        super().__init__(level, x, y)
        self.image = imgs[level]
        self.rect = self.image.get_rect()
        self.rect.center = (self.X , self.Y)
        self.base_rect.center = (self.X + base_img_disp[level][0] , self.Y + 16)

