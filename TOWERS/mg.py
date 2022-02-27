import os
import pygame
from game_constants import *
from tower import Tower

Tower_images = [pygame.transform.scale(pygame.image.load(os.path.join("Assets/Pictures/TOWERS" , "MG.png")) , (35 , 35 * 229 / 110)).convert_alpha(),
                pygame.transform.scale(pygame.image.load(os.path.join("Assets/Pictures/TOWERS" , "MG2.png")) , (60 , 60 * 239 / 218)).convert_alpha(),
                pygame.transform.scale(pygame.image.load(os.path.join("Assets/Pictures/TOWERS" , "MG3.png")) , (50 , 50 * 259 / 166)).convert_alpha(),]

class Mg(Tower):
    def __init__(self, level, x, y):
        super().__init__(level, x, y)
        self.image = Tower_images[level]
        self.rect = self.image.get_rect()
        self.rect.center = (self.X , self.Y)
        self.base_rect.center = (self.X + BASE_IMAGE_DISP[level][0] , self.Y + 16)

    def level_up(self , money):
        cost = self.level_up_cost()
        if self.level <= 1 and money >= cost:
            self.level += 1
            self.image = Tower_images[self.level]
            self.rect = self.image.get_rect()
            self.rect.center = (self.X , self.Y)
            self.base_rect.center = (self.X + BASE_IMAGE_DISP[self.level][0] , self.Y + 16)
            return (True , cost)
        else:
            return (False , 0)