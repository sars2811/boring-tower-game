import math
import os
import pygame

from game_constants import *
from projectile import Projectile


class Tower(pygame.sprite.Sprite):
    def __init__(self , level ,x ,y):
        super().__init__()
        self.surf = pygame.Surface((TOWER_WIDTH , TOWER_HEIGHT))
        self.level = level
        self.range = TOWER_RANGE
        self.hit_points = TOWER_HITPOINT[level]
        self.targetable = []
        self.current_target = None
        self.X = x
        self.Y = y
        self.selected = False
        self.radius = TOWER_RANGE
        self.image = pygame.image.load(os.path.join("Assets/Pictures" , "tower.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (self.X , self.Y)
        self.cooldown_tracker = 20
        self.cooldown_number = 20
        self.lives = 10
        self.angle = 0

    def draw(self , display):
        display.blit(self.image , self.rect)

        
    def draw_range(self, display):
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range ), self.range, 0)

        display.blit(surface, (self.X - self.range, self.Y - self.range))
        
    def move(self , x , y):
        self.X = x
        self.Y = y

        self.rect.center = (self.X , self.Y)

    def cooldown(self):
        if self.cooldown_tracker >= self.cooldown_number:
            self.cooldown_tracker = 0
        elif self.cooldown_tracker != self.cooldown_number:
            self.cooldown_tracker += 1

    def shoot(self, enemies , projectiles):
        enemy_inrange = [s for s in pygame.sprite.spritecollide(self , enemies , False, pygame.sprite.collide_circle) if s != self]
        if enemy_inrange:
            self.cooldown()
            enemy = enemy_inrange[0]
            # dirn = (enemy.X - self.X , enemy.Y - self.Y)
            # length = math.hypot(*dirn)
            # if length == 0.0:
            #     pass
            # else:
            #      dirn = (dirn[0]/length, dirn[1]/length)

            # angle_new = math.degrees(math.atan2(-dirn[1] , dirn[0]))
            # angle_change = angle_new - self.angle
            # self.angle = angle_new

            # self.rotate(angle_change)

            if self.cooldown_tracker == 0:
                P1 = Projectile(enemy , self.hit_points , self.range , self)
                projectiles.add(P1)
        else:
            if self.cooldown_tracker < self.cooldown_number:
                self.cooldown_tracker += 1
            return

    def hit(self):
        self.lives -= 1
        if(self.lives <= 0):
            self.kill()

    # def rotate(self, angle):
    #     self.image = pygame.transform.rotate(self.image , angle)
    #     self.rect = self.image.get_rect()
    #     self.rect.center = (self.X , self.Y)

    # def blitRotate(self , surf, pos, originPos, angle):

    #     # offset from pivot to center
    #     image_rect = self.image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    #     offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
        
    #     # roatated offset from pivot to center
    #     rotated_offset = offset_center_to_pivot.rotate(-angle)

    #     # roatetd image center
    #     rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    #     # get a rotated image
    #     rotated_image = pygame.transform.rotate(image, angle)
    #     rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    #     # rotate and blit the image
    #     surf.blit(rotated_image, rotated_image_rect)
    
    #     # draw rectangle around the image
    #     pygame.draw.rect(surf, (255, 0, 0), (*rotated_image_rect.topleft, *rotated_image.get_size()),2)

        