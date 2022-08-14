'''Author: Muhammad Muneeb Ul Haq
Date started: 19 May 2022
Summary: Alien invasion game

Details: This program is the source code for a game that uses pygame module to develop it. Separate classes are created for every different work in the game such as the settings, Rocket, Alien, Bullets and buttons etc. The bullets are created using the pygame.rect module and the rocket and aliens are shown on the screen using the blit method.The screen rect is used to detect if the sprites are inside the screen.

Working: First of all the run game function in class alienInvasion is run in which the welcome screen is run this detects the pressing of mouse buttons and keyboard keys. After a button is pressed the execution returns to the run game function and enters the while loop in this while loop two conditions are checked if the practice button is pressed or the play game button is pressed.This inturn brings the execution to the respective while loop in the while loop the screen is continuously updated and if any condition that ends the game is met the execution is bringed back to the initial stage i.e the welcome screen.
'''

import pygame 
import sys
import audio
import random
from time import sleep
from pygame.rect import Rect

from settings import Settings
from rocket import Rocket
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from target_practice import *
from score_board import Scoreboard

class alienInvasion:

    '''Main class to manage game'''

    def __init__(self):
        '''Initializing game and creating game resources'''
        pygame.init()
        self.settings = Settings()
        # game window dimensions
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # caption at top of the screen
        pygame.display.set_caption("alien Invasion by Muhammad Muneeb")
        self.rocket = Rocket(self)
        self.stats = GameStats(self)
        self.practice = targetPractice(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.level_button = False
        self.play_button = Button(self, "PLAY", 554, 386)
        self.practice_button = Button(self, "PRACTICE", 500, 455)
        self.easy_button = Button(self, "EASY", 379, 548)
        self.medium_button = Button(self, "MEDIUM", 520, 548)
        self.hard_button = Button(self, "HARD", 711, 548)
        self.sb = Scoreboard(self)
        self.game_over = False
        self.target_ok = 0

    def run_game(self):
        
        '''Start main game loop'''
        
        self._welcome_screen()
        while True:
            self._check_event()
            if self.stats.game_active:
                self._create_fleet()
                while True:
                    self._check_event()
                    self.rocket.update()
                    self._update_bullets()
                    self._update_aliens()
                    self._update_screen_game()
                    if self.game_over:
                        break
            elif self.practice.do_practice:
                while True:
                    self._check_event()
                    self.practice._update()
                    self.rocket.update()
                    self._update_bullets()
                    self._update_screen_practice()
                    if self.game_over:
                        break
                           
    def _check_event(self):
        # watch keyboard input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                self._check_key_down_events(event)
            
            elif event.type == pygame.KEYUP:
                self._check_key_up_events(event)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #get mouse pos 
                mouse_pos = pygame.mouse.get_pos()
                # check collision
                print(mouse_pos)
                self._check_button(mouse_pos)
                return

    def _fire_bullet(self):
        '''create new bullet and add it to bullet group'''
        if self.stats.game_active:
            if len(self.bullets) < self.settings.bullets_allowed:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)
        elif self.practice.do_practice:
            if len(self.bullets) == self.settings.bullets_allowed:
                for bullet in self.bullets:
                    if bullet.rect.right >= 1200:
                        self.practice.do_practice = False
                        self.game_over = True
        
            else:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)

    def _update_screen_game(self):
        # fill background color into the screen
        self.screen.fill(self.settings.bg_color)
        #blitting the rocket image on the screen
        self.rocket.blitme()
        # Drawing score onto the screen
        self.sb.show_score()
        #updating aliens
        self.aliens.draw(self.screen)
        #updating bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        if not self.stats.game_active :
            self._welcome_screen()

        # makes the most recent screen displayed
        pygame.display.flip()
    
    def _update_screen_practice(self):
        # fill background color into the screen
        self.screen.fill(self.settings.bg_color)
        #blitting the rocket image on the screen
        self.rocket.blitme()
        #for drawing target on screen
        self.practice._blit_target()
        #updating bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        if not self.practice.do_practice:
            self._welcome_screen()

        # makes the most recent screen displayed
        pygame.display.flip()

    def _update_bullets(self):
        self.bullets.update()
        # getting rid of buletts outside the screen
        if self.stats.game_active:
            for bullet in self.bullets.copy():
                if bullet.rect.right >= 1200:
                    self.bullets.remove(bullet)
        elif self.practice.do_practice:
            pass
        self._check_bullet_collisions()
        
    def _welcome_screen(self):
        '''shows the welcome screen until space bar is pressed'''
        welcome_screen = pygame.image.load('Gallery\\welcome.png')
        while True:
            self.screen.blit(welcome_screen, (0,0))
            self.play_button.draw_button()
            self.practice_button.draw_button()
            self.easy_button.draw_button()
            self.medium_button.draw_button()
            self.hard_button.draw_button()
            pygame.display.flip()
            self._check_event()
            return       
                    
    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien.x + alien_width * alien_number *2
        alien.y = alien.y + alien_height * row_number *2
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _check_bullet_collisions(self):
        
        if self.stats.game_active:
            # checking for bullets that hit aliens in game
            collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)        # checking if screen is clear
            if not self.aliens and not self.practice.do_practice:
                self.bullets.empty()
                self._create_fleet()
                self.stats.level += 1
                self.sb.prep_level()
                self.settings.increase_speed()
            if collisions:
                for aliens in collisions.values():
                    self.stats.score += self.settings.alien_point * len(aliens)
                self.sb.prep_score()
                self.sb.check_highscore()
        elif self.practice.do_practice:
            # checking for bullets that hit the target in practice
            target_hit = pygame.sprite.spritecollide(self.practice,self.bullets,True,())
            if target_hit:
                self.target_ok += 1
            if self.target_ok == 3:
                self.game_over = True
                self.practice.do_practice = False

    def _create_fleet(self):
        '''create the fleet of aliens'''
        # Create an alien and find the number of aliens in a row.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # finding available spaces at x and y and capacity
        available_space_x = self.settings.screen_width - self.rocket.rect.width - 3*alien_width
        number_of_aliens = (available_space_x) // (alien_width*1.7)
        available_space_y = self.settings.screen_height - self.rocket.rect.width - 3*alien_height
        number_of_rows = (available_space_y) // (alien_height*1.5)
        # to generate aliens in a pattern
        for row_number in range(int(number_of_rows)):
            for alien_number in range(int(number_of_aliens)):
                self._create_alien(alien_number, row_number)
        
        self.settings.direction = 1
                 
    def _check_key_down_events(self,event):
        '''check for key presses'''
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._start_game()
            return
        elif event.key == pygame.K_t:
            self._start_practice()
            return
            
    def _check_key_up_events(self,event):
        '''check for key releases'''
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
           self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
        
    def _update_aliens(self):
        # changing the position
    
        self.aliens.update()
        for alien in self.aliens:
            if alien.check_edges():
                self._change_fleet_direction()
                break               
        self._check_alien_rocket_collision()
        self._check_borderline()

    def _change_fleet_direction(self):
        for alien in self.aliens:
            alien.rect.x -= self.settings.falling_speed
        self.settings.direction *= -1
        
    def _check_alien_rocket_collision(self):
        if pygame.sprite.spritecollideany(self.rocket, self.aliens):
            self._rocket_hit()
            
    def _rocket_hit(self):
            if self.stats.rockets_left > 0:
                #decrease rockets left
                self.stats.rockets_left -= 1
                self.sb.prep_rockets()
                #check if remaining rockets are less than zero
                if self.stats.rockets_left == 0:
                    pygame.mouse.set_visible(True)
                    self.stats.game_active = False
                    self.game_over = True
                    self.level_button = False
                else:
                    #remove remaining aliens and bullets
                    self.aliens.empty()
                    self.bullets.empty()
                    #create new ones
                    if self.stats.game_active:
                        self._create_fleet()
                    self.rocket.midleft()
                    #pause the game for 1 second
                    sleep(1)
                    print(self.stats.rockets_left)

    def _check_borderline(self):
            for alien in self.aliens:
                if alien.rect.left <= 0:
                    self._rocket_hit()
    
    def _check_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            self._start_game()
            if not self.level_button:
                self.settings.speedup_scale = 1
        elif self.practice_button.rect.collidepoint(mouse_pos):
            self._start_practice()
        elif self.easy_button.rect.collidepoint(mouse_pos):
            self.settings.speedup_scale = 1.1
            self.level_button = True
        elif self.medium_button.rect.collidepoint(mouse_pos):
            self.settings.speedup_scale = 1.5
            self.level_button = True
        elif self.hard_button.rect.collidepoint(mouse_pos):
            self.settings.speedup_scale = 2
            self.level_button = True

    def _start_game(self):
        self.stats.reset_stats()
        self.aliens.empty()
        self.bullets.empty()
        self._create_fleet()
        self.rocket.midleft()
        self.rocket.reset_pos()
        self.sb.prep_rockets()
        self.settings.initialize_dynamic_settings()
        self.practice.do_practice = False
        self.stats.game_active = True
        self.game_over = False
        pygame.mouse.set_visible(False)
    
    def _start_practice(self):
        self.stats.reset_stats()
        self.aliens.empty()
        self.bullets.empty()
        self.rocket.midleft()
        self.rocket.reset_pos()
        self.stats.game_active = False
        self.practice.do_practice = True
        self.game_over = False
        self.target_ok = 0

if __name__ == "__main__":
    # make a game instance to run the game
    game = alienInvasion()
    game.run_game()