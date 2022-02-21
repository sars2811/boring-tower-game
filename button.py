import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self , name):
        super().__init__()
        self.name = name
        