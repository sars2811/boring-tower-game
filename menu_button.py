import os
import pygame
from TOWERS.mg import Mg

# from game_constants import BASE_IMAGE, BASE_IMAGE_DISP, BLACK, BUTTON_HEIGHT, BUTTON_WIDTH, TOWER_IMAGES, WHITE  
from game_constants import * 

Tower_images = [pygame.transform.scale(pygame.image.load(os.path.join("Assets/Pictures/TOWERS" , "MG.png")) , (35 , 35 * 229 / 110)).convert_alpha(),
                pygame.transform.scale(pygame.image.load(os.path.join("Assets/Pictures/TOWERS" , "MG2.png")) , (60 , 60 * 239 / 218)).convert_alpha(),
                pygame.transform.scale(pygame.image.load(os.path.join("Assets/Pictures/TOWERS" , "MG3.png")) , (50 , 50 * 259 / 166)).convert_alpha(),]

class MenuButton:
    def __init__(self , x , y ,level ):
        self.image = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT))
        self.rect = self.image.get_rect()
        self.level = level
        self.rect.center = (x , y)
        self.entity = Mg(level , x , y)
        self.hover = False
        self.base_image = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Pictures/TOWERS" , "tower.png")) , (70 , 70)).convert_alpha()
        self.image_rect = Tower_images[self.level].get_rect()
        self.image_rect.center = (x , y)
        self.base_rect = self.base_image.get_rect()
        self.base_rect.center = (x + BASE_IMAGE_DISP[level][0] , y + 16)

    def clicked(self , mos_pos):
        if self.rect.collidepoint(mos_pos):
            return self.entity
        else:
            return None

    def check_hovered(self , mos_pos):
        if self.rect.collidepoint(mos_pos):
            self.hover = True
        else:
            self.hover = False

    def draw(self , display):
        self.image.fill(WHITE)

        if self.hover:
            pygame.draw.rect(self.image , BLACK , (0,0,BUTTON_WIDTH,BUTTON_HEIGHT) , 6)
        else:
            pass

        display.blit(self.image , self.rect)
        display.blit(self.base_image, self.base_rect)
        display.blit(Tower_images[self.level] , self.image_rect)
        
        


