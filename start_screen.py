import sys
import pygame
import pygame_textinput
from game import Game

from game_constants import *

start_font = pygame.font.Font(None, 30)

welcome_text = start_font.render("Welcome!" , True , RED)
welcome_text_rect = welcome_text.get_rect()

to_text = start_font.render("to" , True , RED)
to_text_rect = to_text.get_rect()

start_text = start_font.render("Start!" , True , RED)
start_text_rect = start_text.get_rect()

game_text = start_font.render("The Boring Game" , True , RED)
game_text_rect = game_text.get_rect()

text_input = pygame_textinput.TextInputVisualizer()
text_input_rect = text_input.surface.get_rect()

welcome_text_rect.center = ((WIN_WIDTH / 2) , (WIN_HEIGHT / 2 - 80))
text_input_rect.center = ((WIN_WIDTH / 2 - 65) , (WIN_HEIGHT / 2 - 55))
to_text_rect.center = ((WIN_WIDTH / 2) , (WIN_HEIGHT / 2 - 30))
game_text_rect.center = ((WIN_WIDTH / 2) , (WIN_HEIGHT / 2))
start_text_rect.center = ((WIN_WIDTH / 2) , (WIN_HEIGHT / 2 + 30))

frames = pygame.time.Clock()

pygame.mixer.music.load('Assets\Music\8bitDungeonLevel.mp3')


class StartMenu:
    def __init__(self , display):
        self.display = display
        text_input.value = "Anonymous"

    def run(self):
        run = True
        pygame.mixer.music.play(-1)


        while run:     

            self.draw()

            events = pygame.event.get()

            text_input.update(events)

            for event in events:
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False

                    if event.key == pygame.K_RETURN:
                        game = Game(self.display , text_input.value)
                        game.run()
                        del game

                if event.type == pygame.MOUSEBUTTONDOWN:
                    #Checking if Start button clicked

                    mos_pos = pygame.mouse.get_pos()

                    if start_text_rect.collidepoint(mos_pos):
                        game = Game(self.display , text_input.value)
                        game.run()
                        del game


        pygame.quit()
        sys.exit()

    def draw(self):
        self.display.fill(L_BROWN)
        self.display.blit(welcome_text , welcome_text_rect)
        self.display.blit(to_text , to_text_rect)
        self.display.blit(game_text , game_text_rect)
        self.display.blit(start_text , start_text_rect)

        self.display.blit(text_input.surface, text_input_rect)
        frames.tick(FPS)
        pygame.display.update()
