#Window Constants
WIN_WIDTH = 1160
WIN_HEIGHT = 640

#Other Game related Constants
FPS = 30

#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
GREY = (120, 120, 120)
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)
L_BROWN = (196, 164, 132)

#Initial Condition
LIVES = 10
MONEY = 2000

#TOWER INFO
TOWER_HITPOINT = (40 , 50 , 60) #TODO: Change accorfing to the tower and stuff.
TOWER_COOLDOWN = (20 , 17 , 15)
TOWER_RANGE = 200
ARROW_SPEED = 15
TOWER_HEIGHT = 64
TOWER_WIDTH = 30
TOWER_COST = (500 , 1000 , 1500)
# BASE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Pictures/TOWERS" , "tower.png")) , (70 , 70))
TOWER_IMAGES = []
BASE_IMAGE_DISP = [(6,16) , (0 , 16) , (7,16)]

#MONSTER INFO
MONSTER_HEALTH = (100 , 120 , 200) #TODO: Change according to the graphics and monster type
MONSTER_SPEED = 4
MONSTER_HEIGHT = 64
MONSTER_WIDTH = 30
SPEED_INCREASE = 1
PICTURE_NUMBER = 20

#BUTTON INFO
BUTTON_WIDTH = 125
BUTTON_HEIGHT = 125
BUTTON_X = 1050
BUTTON_Y = 250
BUTTONS = []

#MENU INFO
MENU_X = 1000
MENU_Y = 300

#TODO: MAKE MULTIPLE HIGHSCORES THINGY.


# def init():
#     BUTTONS.append(MenuButton(BUTTON_X , 200 , 0))
#     BUTTONS.append(MenuButton(BUTTON_X , 350 , 1))
#     BUTTONS.append(MenuButton(BUTTON_X , 500 , 2))

#     TOWER_IMAGES.append(pygame.transform.scale(pygame.image.load(os.path.join("Assets/Pictures/TOWERS" , "MG.png")) , (35 , 35 * 229 / 110)).convert_alpha())
#     TOWER_IMAGES.append(pygame.transform.scale(pygame.image.load(os.path.join("Assets/Pictures/TOWERS" , "MG2.png")) , (60 , 60 * 239 / 218)).convert_alpha())
#     TOWER_IMAGES.append(pygame.transform.scale(pygame.image.load(os.path.join("Assets/Pictures/TOWERS" , "MG3.png")) , (50 , 50 * 259 / 166)).convert_alpha())

#     # BASE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Pictures/TOWERS" , "tower.png")) , (70 , 70)).convert_alpha()
