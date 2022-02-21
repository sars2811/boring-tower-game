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
            if self.cooldown_tracker == 0:
                P1 = Projectile(self.X , self.Y , enemy_inrange[0] , self.hit_points , self.range)
                projectiles.add(P1)
        else:
            if self.cooldown_tracker < self.cooldown_number:
                self.cooldown_tracker += 1
            return

    def hit(self):
        self.lives -= 1
        if(self.lives <= 0):
            self.kill()
        