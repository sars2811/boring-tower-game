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
BASE_IMAGE_DISP = [(6,16) , (0 , 16) , (7,16)]

#MONSTER INFO
MONSTER_HEALTH = (100 , 120 , 200) #TODO: Change according to the graphics and monster type
MONSTER_SPEED = 4
MONSTER_HEIGHT = 64
MONSTER_WIDTH = 30
SPEED_INCREASE = 1
PICTURE_NUMBER = 20
MONSTER_SCORE = (10 , 15 , 20)
MONSTER_MONEY = (10 , 15 , 20)
#(Alien , Ogre , Sword )
WAVES = [
    [20, 0, 0],
    [40, 0, 0],
    [80, 0, 0],
    [20, 20, 0],
    [50, 30, 0, ],
    [70, 50, 0],
    [20, 100, 0],
    [50, 100, 0],
    [80, 100, 0],
    [20, 20, 50],
    [40, 40, 100],
    [20, 20, 150],
    [200, 100, 200],
]

#BUTTON INFO
BUTTON_WIDTH = 125
BUTTON_HEIGHT = 125
BUTTON_X = 1050
BUTTON_Y = 250
BUTTONS = []

#MENU INFO
MENU_X = 1000
MENU_Y = 300

#OTHER STUFF
MAX_VIBRATE_COUNT = 15
MONEY_Y = 75
VIBRATE_DISP = 5
FILE_NAME = "high_score.txt"
HIGH_SCORE_NAME = "high_score"
HIGH_NAME = "name"
