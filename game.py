import os
import sys
import time
import pygame
from ENEMIES.alien import Alien
from ENEMIES.ogre import Ogre
from ENEMIES.sword import Sword
from game_constants import *
from tower import Tower

FramePerSec = pygame.time.Clock()

class Game:
    def __init__(self, display):
        self.display = display
        self.alive_enemy_list = pygame.sprite.Group()
        self.dead_enemy_list = pygame.sprite.Group()
        self.attack_tower_list = pygame.sprite.Group()
        self.projectile_list = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
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
        self.display.fill(BLACK)
        T1 = Tower(0 , (WIN_WIDTH / 2) , (WIN_HEIGHT / 2))
        self.attack_tower_list.add(T1)

        # self.pause = True

    def gen_enemies(self):
        #TODO: DO BETTER ENEMY GENERATION.
        if len(self.alive_enemy_list) == 0:
            E1 = Alien()
            self.alive_enemy_list.add(E1)


    def display_text(self, text , pos_x , pos_y):
        text_surface = self.font.render(text , True , BLACK)
        self.display.blit(text_surface , (pos_x , pos_y))

    #TODO: Change the position of HUD and also decrease that in size.
    def display_hud(self):
        #Drawing the Outer Rectangles   
        pygame.draw.rect(self.display , GREY , (30 , 30 , 400 , 100))
        pygame.draw.rect(self.display , WHITE , (30 , 30 , 400 , 100) , 3)

        #Displaying Money Info
        pygame.draw.rect(self.display , YELLOW , (50 , 50 , 60 , 60))
        self.display_text(str(self.money) , 115 , 60)

        #Displaying Lives
        pygame.draw.rect(self.display , RED , (250 , 50 , 60 , 60))
        self.display_text(str(self.lives) , 315 , 60)

    def draw(self):

        #This function takes care of drawing everything
        self.display.blit(self.bg , (0,0))
        self.display_hud()

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
                killed = t[0].hit(a.damage)
                if killed:
                    self.score += 10
                    self.alive_enemy_list.remove(t[0])
                    self.dead_enemy_list.add(t[0])
                
                a.kill()
                

        for collide in  pygame.sprite.groupcollide(self.attack_tower_list , self.alive_enemy_list , False ,False).items():
            for x in collide[1]:
                collide[0].hit()


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
                        self.selected_tower = None
                    
                    mos_pos = pygame.mouse.get_pos()
                    # TODO: Complete this and enable placing tower
                    if self.placing_tower:
                        not_allowed = False

                    # Checking if a tower was clicked.
                    for tower in self.attack_tower_list:
                        if tower.rect.collidepoint(mos_pos):
                            self.selected_tower = tower

            

            #SEE IF MOVING SOMETHING
        
            FramePerSec.tick(FPS)

        pygame.quit()
        sys.exit()
