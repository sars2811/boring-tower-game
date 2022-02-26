import os
import sys
import time
import pygame
from ENEMIES.alien import Alien
from ENEMIES.ogre import Ogre
from ENEMIES.sword import Sword
from TOWERS.mg import Mg
from game_constants import *
from menu import Menu

FramePerSec = pygame.time.Clock()

class Game:
    def __init__(self, display):
        self.display = display
        self.alive_enemy_list = pygame.sprite.Group()
        self.dead_enemy_list = pygame.sprite.Group()
        self.attack_tower_list = pygame.sprite.Group()
        self.projectile_list = pygame.sprite.Group()
        # game_constants.BASE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Pictures/TOWERS" , "tower.png")) , (70 , 70)).convert_alpha()
        # game_constants.TOWER_IMAGES = [pygame.transform.scale(pygame.image.load(os.path.join("Assets/Pictures/TOWERS" , "MG.png")) , (35 , 35 * 229 / 110)).convert_alpha(),
        #         pygame.transform.scale(pygame.image.load(os.path.join("Assets/Pictures/TOWERS" , "MG2.png")) , (60 , 60 * 239 / 218)).convert_alpha(),
        #         pygame.transform.scale(pygame.image.load(os.path.join("Assets/Pictures/TOWERS" , "MG3.png")) , (50 , 50 * 259 / 166)).convert_alpha(),]
        self.lives = LIVES
        self.money = MONEY
        self.timer = time.time()
        self.font = pygame.font.SysFont("comicsans" , 40)
        self.wave = 0
        self.selected_tower = None
        self.placing_tower = None
        self.bg = pygame.image.load(os.path.join("Assets/Pictures" , "bg-hd.png")).convert_alpha()
        self.run_bool = True
        self.score = 0
        self.display.fill(GREY)
        self.menu = Menu()
        self.vibrate_money = False
        self.vibrate_count = 0
        self.vibrate_disp = 0

        # self.pause = True

    def gen_enemies(self):
        #TODO: DO BETTER ENEMY GENERATION.
        if len(self.alive_enemy_list) == 0:
            E1 = Alien()
            self.alive_enemy_list.add(E1)

    def display_text(self, text , pos_x , pos_y , color):
        text_surface = self.font.render(text , True , color)
        self.display.blit(text_surface , (pos_x , pos_y))

    def display_hud(self):

        #Displaying the score
        self.display_text(str(self.score) , 980 , 30 , BLACK)

        #Displaying Money Info
        pygame.draw.rect(self.display , YELLOW , (980 , 90 , 30 , 30))
        if self.vibrate_money:
            self.display_text(str(self.money) , 1020 , MONEY_Y + self.vibrate_disp , RED)
        else:
            self.display_text(str(self.money) , 1020 , MONEY_Y , BLACK)

        #Displaying Lives
        pygame.draw.rect(self.display , RED , (980 , 140 , 30 , 30))
        self.display_text(str(self.lives) , 1020 , 125 , BLACK)

    def draw(self):

        #This function takes care of drawing everything
        self.display.fill(GREY)
        self.display.blit(self.bg , (0,0))
        self.display_hud()
        self.menu.draw(self.display)

        for enemy in self.dead_enemy_list:
            enemy.draw_dead(self.display)

        for enemy in self.alive_enemy_list:
            enemy.draw(self.display)
            enemy.draw_health_bar(self.display)

        for tower in self.attack_tower_list:
            tower.draw(self.display)

        if self.selected_tower:
            self.selected_tower.draw_range(self.display)

        for projectile in self.projectile_list:
            projectile.draw(self.display)

        if self.placing_tower:
            self.placing_tower.draw(self.display)
            self.placing_tower.draw_range(self.display)

        pygame.display.update()

    def update(self):

        for enemy in self.alive_enemy_list:
            enemy.move()
            
            #Implementing if the enemy has crossed into the castle.
            if(enemy.X >= enemy.path[len(enemy.path) - 1][0] and enemy.Y >= enemy.path[len(enemy.path) - 1][1]):
                if self.lives <= 0:
                    self.game_end()
                self.lives -= 1
                enemy.kill()

        for tower in self.attack_tower_list:
            tower.shoot(self.alive_enemy_list , self.projectile_list)
            
        for projectile in self.projectile_list:
            projectile.update()

        for t in pygame.sprite.groupcollide(self.alive_enemy_list , self.projectile_list , False ,False).items():
            for a in t[1]:
                killed , enemy_level = t[0].hit(a.damage)
                if killed:
                    self.score += MONSTER_SCORE[enemy_level]
                    self.money += MONSTER_MONEY[enemy_level]
                    self.alive_enemy_list.remove(t[0])
                    self.dead_enemy_list.add(t[0])
                
                a.kill()
                

        for collide in  pygame.sprite.groupcollide(self.attack_tower_list , self.alive_enemy_list , False ,False).items():
            for x in collide[1]:
                collide[0].hit()

        if self.vibrate_money:
            if self.vibrate_count >= MAX_VIBRATE_COUNT:
                self.vibrate_money = False
                self.vibrate_count = 0
                self.vibrate_disp = 0
            else:
                multiplier = (self.vibrate_count % 3) - 1
                self.vibrate_disp = VIBRATE_DISP * multiplier
                self.vibrate_count += 1


    def game_end(self):
        #TODO: MAKE AND DIRECT TO THE GAME END SCREEN.
        self.run_bool = False
                
    def run(self):
        
        while self.run_bool:
            self.update()
            self.draw()

            self.gen_enemies()

            mos_pos = pygame.mouse.get_pos()

            #For tower that is selected and yet not placed.
            if self.placing_tower:
                self.placing_tower.move(mos_pos[0] , mos_pos[1])
            else:
                self.menu.check_hovered(mos_pos)

                #TODO: CHECK IF INTERSECTING WITH ANOTHER TOWER AND REACT ACCORDINGLY

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run_bool = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.run_bool = False

                    if event.key == pygame.K_n:
                        self.waves += 1

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.selected_tower:
                        #TODO: Check for upgrade option.
                        self.selected_tower = None
                    
                    # TODO: Complete this and enable placing tower
                    if self.placing_tower != None:
                        not_allowed = False

                        for tower in self.attack_tower_list:
                            if self.placing_tower.base_rect.colliderect(tower.base_rect):
                                #TODO: Chnage the color of something to show tat there was intersection.
                                not_allowed = True
                                pass

                        if not not_allowed:
                            if self.money >= TOWER_COST[self.placing_tower.level]:
                                self.attack_tower_list.add(self.placing_tower)
                                self.money -= TOWER_COST[self.placing_tower.level]
                                self.placing_tower = None
                            else:
                                self.vibrate_money = True
                                self.placing_tower = None

                    # Checking if a tower was clicked.
                    for tower in self.attack_tower_list:
                        if tower.rect.collidepoint(mos_pos):
                            self.selected_tower = tower

                    # Checking if the menu got clicked.
                    tower_clicked = self.menu.check_clicked(mos_pos)
                    if tower_clicked != None:
                        self.placing_tower = tower_clicked
            

            #SEE IF MOVING SOMETHING
        
            FramePerSec.tick(FPS)

        pygame.quit()
        sys.exit()
