import math
import os
import pygame

from game_constants import *
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.level = 0 #
        self.health = MONSTER_HEALTH[self.level] 
        self.animation_count = 0
        self.die_animation = 0
        self.speed = MONSTER_SPEED
        self.path = [(-50 , 190) , (885,190) , (885 , 380) , (70 , 380) , (70 , 570) , (800,570)] #maybe according to the monster size
        self.path_pos = 0
        self.X = self.path[0][0]
        self.Y = self.path[0][1]
        self.flipped = False
        self.money = 5 #
        self.image = pygame.Surface((40 , 40))
        self.rect = self.image.get_rect()
        self.rect.center = (self.X , self.Y)
        self.radius = 5 #
        self.walk_imgs = []
        self.die_imgs = []
        
    def draw(self , display):
        display.blit(self.walk_imgs[int(self.animation_count/3)] , self.rect)
        self.draw_health_bar(display)

    def draw_health_bar(self , display):
        #TODO: Make it according to the images.
        
        length = 50
        shrink_by = length / MONSTER_HEALTH[self.level]
        health_length = self.health * shrink_by
        
        pygame.draw.rect(display , RED , (self.X - 40 , self.Y - 30 , length , 10))
        pygame.draw.rect(display , GREEN , (self.X - 40 , self.Y - 30 , health_length , 10))

    def move(self):
        self.animation_count += 1
        if (self.animation_count >= PICTURE_NUMBER * 3):
            self.animation_count = 0

        if(self.path_pos >= (len(self.path ) - 1)):
            x2 , y2 = self.path[len(self.path) - 1]
            x1 , y1 = self.path[len(self.path) - 2]
        else:
            x1 , y1 = self.path[self.path_pos]
            x2 , y2 =  self.path[self.path_pos + 1]

        dirn = ((x2-x1) , (y2-y1))

        length = math.sqrt((dirn[0])**2 + (dirn[1])**2)
        dirn = (dirn[0] / length , dirn[1] / length)

        #Flipping the images accordin to going left or right
        if(dirn[0] < 0 and not(self.flipped)):
            self.flipped = True
            for x, img in enumerate(self.walk_imgs):
                self.walk_imgs[x] = pygame.transform.flip(img, True, False)
            for x, img in enumerate(self.die_imgs):
                self.die_imgs[x] = pygame.transform.flip(img, True, False)

        if(dirn[0] > 0 and self.flipped):
            self.flipped = False
            for x, img in enumerate(self.walk_imgs):
                self.walk_imgs[x] = pygame.transform.flip(img, True, False)
            for x, img in enumerate(self.die_imgs):
                self.die_imgs[x] = pygame.transform.flip(img, True, False)

        #Changing the current path position according to the current position
        if dirn[0] > 0: #moving towards right
            if dirn[1] >= 0: #moving down
                if self.X >= x2 and self.Y >= y2:
                    self.path_pos += 1
            else:
                if self.X >= x2 and self.Y <= y2:
                    self.path_pos += 1
        elif dirn[0] < 0: #Moving towards left
            if dirn[1] >= 0: #moving down
                if self.X <= x2 and self.Y >= y2:
                    self.path_pos += 1
            else:
                if self.X <= x2 and self.Y <= y2:
                    self.path_pos += 1
        else:
            if dirn[1] >= 0:
                if self.Y >= y2:
                    self.path_pos += 1
            else:
                if self.Y <= y2:
                    self.path_pos += 1

        self.rect.move_ip(self.speed * dirn[0] , self.speed * dirn[1])
        self.X , self.Y = self.rect.center

    def hit(self , damage):

        self.health -= damage

        if self.health <= 0:
            return (True , self.level)
        else:
            return (False , 0)

    def speed_increase(self):
        self.speed += SPEED_INCREASE

    def draw_dead(self , display):
        if self.die_animation == PICTURE_NUMBER - 1:
            self.kill()
        display.blit(self.die_imgs[int(self.die_animation)] , self.rect)
        self.die_animation += 1

