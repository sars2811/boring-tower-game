import sys
import pygame
from game import Game

from game_constants import *

start_font = pygame.font.Font(None, 30)
start_text = start_font.render("Start!" , True , RED)
game_text = start_font.render("The Boring Game" , True , RED)
start_text_rect = start_text.get_rect()
start_text_rect.center = ((WIN_WIDTH / 2) , (WIN_HEIGHT / 2))
game_text_rect = game_text.get_rect()
game_text_rect.midbottom = start_text_rect.midtop


class StartMenu:
    def __init__(self , display):
        self.display = display

    def run(self):
        run = True

        while run: 

            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False

                    if event.key == pygame.K_RETURN:
                        game = Game(self.display)
                        game.run()
                        del game

                if event.type == pygame.MOUSEBUTTONDOWN:
                    #Checking if Start button clicked

                    mos_pos = pygame.mouse.get_pos()

                    if start_text_rect.collidepoint(mos_pos):
                        game = Game(self.display)
                        game.run()
                        del game


        pygame.quit()
        sys.exit()

    def draw(self):
        self.display.fill(L_BROWN)
        self.display.blit(game_text , game_text_rect)
        self.display.blit(start_text , start_text_rect)
        pygame.display.update()
