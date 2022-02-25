import pygame

from game_constants import *

if __name__ == "__main__":
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((1160 , 640))
    from start_screen import StartMenu
    main_menu = StartMenu(DISPLAYSURF)
    main_menu.run()
    