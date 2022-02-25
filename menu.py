from game_constants import *
from menu_button import MenuButton

buttons = [
    MenuButton(BUTTON_X , BUTTON_Y , 0),
    MenuButton(BUTTON_X , BUTTON_Y + 130 , 1),
    MenuButton(BUTTON_X , BUTTON_Y + 2 * 130 , 2),
]

class Menu:
    def __init__(self):
        self.menu_buttons = buttons
        
    def check_hovered(self, mos_pos):
        for button in self.menu_buttons:
            button.check_hovered(mos_pos)

    def check_clicked(self, mos_pos):
        for button in self.menu_buttons:
            entity = button.clicked(mos_pos)
            if entity != None:
                return entity
            
        return None

    def draw(self, display):
        for button in self.menu_buttons:
            button.draw(display)