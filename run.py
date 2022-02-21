import pygame
import game_constants

if __name__ == "__main__":
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((game_constants.WIN_WIDTH , game_constants.WIN_HEIGHT))
    from start_screen import StartMenu
    main_menu = StartMenu(DISPLAYSURF)
    main_menu.run()
    