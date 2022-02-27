import os
import random
import sys
import pygame
from ENEMIES.alien import Alien
from ENEMIES.ogre import Ogre
from ENEMIES.sword import Sword
from game_constants import *
from menu import Menu
import shelve

FramePerSec = pygame.time.Clock()

file = shelve.open(FILE_NAME)

flag1 = HIGH_SCORE_NAME in file
flag2 = HIGH_NAME in file

high_score = 0
high_name = "Anonymous"

if flag1:
    high_score = file[HIGH_SCORE_NAME]
else:
    file[HIGH_SCORE_NAME] = 0

if flag2:
    high_name = file[HIGH_NAME]
else:
    file[HIGH_NAME] = "Anonymous"

file.close()

class Game:
    def __init__(self, display , name):
        self.display = display
        self.alive_enemy_list = pygame.sprite.Group()
        self.dead_enemy_list = pygame.sprite.Group()
        self.attack_tower_list = pygame.sprite.Group()
        self.projectile_list = pygame.sprite.Group()
        self.lives = LIVES
        self.money = MONEY
        self.font = pygame.font.SysFont("comicsans" , 40)
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
        
        self.wave_n = 0
        self.time_n_wave = 120
        self.current_wave = WAVES[self.wave_n]

        self.last_spawn = pygame.time.get_ticks()

        self.name = name

    def gen_enemies(self):
        #TODO: MAYBE ADD A TIMER FOR SOMEWHAT RANDOM SPAWNING
        if sum(self.current_wave) != 0:
            wave_enemies = [Alien() , Ogre() , Sword()]
            not_found = True
            while not_found:
                x = random.randint(0 , len(self.current_wave) - 1)
                if self.current_wave[x] != 0:
                    self.alive_enemy_list.add(wave_enemies[x])
                    self.current_wave[x] -= 1
                    not_found = False

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

    def display_HS(self):
        self.display_text(f"High Score: {high_score} by {high_name}" , 200 , 50 , BLACK)

    def draw(self):

        #This function takes care of drawing everything
        self.display.fill(GREY)
        self.display.blit(self.bg , (0,0))
        self.display_hud()
        self.display_HS()
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

        for t in pygame.sprite.groupcollide(self.projectile_list, self.alive_enemy_list, False ,False).items():
            enemy_hit = t[1][0]

            if enemy_hit:
                killed , enemy_level = enemy_hit.hit(t[0].damage)

                if killed:
                    self.score += MONSTER_SCORE[enemy_level]
                    self.money += MONSTER_MONEY[enemy_level]
                    self.alive_enemy_list.remove(enemy_hit)
                    self.dead_enemy_list.add(enemy_hit)

                t[0].kill()

            # Here if bullet hit multiple enemies, all registered the hit
            # for a in t[1]:
            #     killed , enemy_level = t[0].hit(a.damage)
            #     if killed:
            #         self.score += MONSTER_SCORE[enemy_level]
            #         self.money += MONSTER_MONEY[enemy_level]
            #         self.alive_enemy_list.remove(t[0])
            #         self.dead_enemy_list.add(t[0])
                
            #     a.kill()
                

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

        if sum(self.current_wave) == 0:
            if len(self.alive_enemy_list) == 0:
                if self.time_n_wave > 0:
                    self.time_n_wave -= 1
                elif self.wave_n <= (len(WAVES) - 2) and self.time_n_wave <= 0:
                    self.wave_n += 1
                    self.time_n_wave = 120
                    self.current_wave = WAVES[self.wave_n]
                else:
                    print("Game ended")
                    self.run_bool = False


    def check_HS(self):

        #TODO: change it to actually store the data
        if self.score > high_score:
            file = shelve.open(FILE_NAME)
            file[HIGH_SCORE_NAME] = self.score
            file[HIGH_NAME] = self.name

    def game_end(self):
        #TODO: MAKE AND DIRECT TO THE GAME END SCREEN.
        self.run_bool = False
                
    def run(self):
        
        while self.run_bool:
            self.update()
            self.draw()

            now = pygame.time.get_ticks()
            if now - self.last_spawn >= random.randint(300 , 500):
                self.last_spawn = now
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
                        self.time_n_wave = 0

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.selected_tower:
                        if self.selected_tower.upgrade_text_rect.collidepoint(mos_pos) and self.selected_tower.upgradable:
                            upgraded , cost = self.selected_tower.level_up(self.money)

                            if not upgraded:
                                self.vibrate_money = True
                            else:
                                self.money -= cost

                        else: self.selected_tower = None
                    
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
                        if tower.rect.collidepoint(mos_pos) or tower.base_rect.collidepoint(mos_pos):
                            self.selected_tower = tower

                    # Checking if the menu got clicked.
                    tower_clicked = self.menu.check_clicked(mos_pos)
                    if tower_clicked != None:
                        self.placing_tower = tower_clicked
            

            #SEE IF MOVING SOMETHING
        
            FramePerSec.tick(FPS)


        self.check_HS()
        
        pygame.quit()
        sys.exit()
