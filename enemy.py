import math
import os
import pygame

from game_constants import *
class Enemy(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        self.level = level
        self.health = MONSTER_HEALTH[level]
        self.animation_count = 0
        self.speed = MONSTER_SPEED
        self.path = [(-50 , 190) , (885,190) , (885 , 380) , (70 , 380) , (70 , 570) , (800,570)]
        self.path_pos = 0
        self.X = self.path[0][0]
        self.Y = self.path[0][1]
        #self.image
        #self.images
        self.speed_increase = SPEED_INCREASE
        self.flipped = False
        self.money = 5
        self.image = pygame.image.load(os.path.join("Assets/Pictures" , "enemy.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (self.X , self.Y)
        self.radius = 5
        
    def draw(self , display):
        display.blit(self.image , self.rect)
        self.draw_health_bar(display)

    def draw_health_bar(self , display):
        
        length = 50
        shrink_by = length / MONSTER_HEALTH[self.level]
        health_length = self.health * shrink_by
        
        pygame.draw.rect(display , RED , (self.X - 27 , self.Y - 15 , length , 10))
        pygame.draw.rect(display , GREEN , (self.X - 27 , self.Y - 15 , health_length , 10))

    def move(self):
        self.animation_count += 1
        #TODO: Change when assets arrive

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
            #TODO: Implement the rest as u get the resources

        if(dirn[0] > 0 and self.flipped):
            self.flipped = False
            #TODO: Implement the rest as u get the resources

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
            self.kill()
            return True
            

        return False
