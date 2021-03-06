import math
import pygame

from game_constants import *


class Projectile(pygame.sprite.Sprite):
    def __init__(self ,target, damage , range , tower):
        super().__init__()
        self.X = tower.X
        self.Y = tower.Y
        self.target = target
        self.damage = damage
        self.range = range
        self.image = pygame.Surface((9,9))
        self.rect = self.image.get_rect()
        self.rect.center = (self.X , self.Y)
        self.radius = 4
        pygame.draw.circle(self.image , RED , (4, 4) , self.radius)
        self.moves_max = self.range / ARROW_SPEED
        self.moves = 0
        self.tower = tower

    def draw(self , display):
        display.blit(self.image , self.rect)

    def update(self):

        if self.moves <= (self.moves_max):
            x2 = self.target.X
            y2 = self.target.Y
            dirn = (x2 - self.X , y2 - self.Y)
            length = math.sqrt(dirn[0]**2 + dirn[1]**2)
            if length == 0.0:
                pass
            else:
                 dirn = (dirn[0]/length, dirn[1]/length)
            self.rect.move_ip(ARROW_SPEED * dirn[0] , ARROW_SPEED * dirn[1])

            self.X , self.Y = self.rect.center

            self.moves += 1     
        else:
            self.kill()
