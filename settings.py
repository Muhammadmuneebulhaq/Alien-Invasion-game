import pygame

class Settings:
    '''A class to store all settinge for alien invasion'''
    def __init__(self):
        '''Initialize game static settings'''
        self.screen_height = 800
        self.screen_width = 1200
        self.bg_color = (255, 255, 255)
        
        # rocket settings
        self.rocket_limit = 3
        self.rocket_speed = 5
        # bullet settings
        self.bullet_speed = 1
        self.bullet_height = 3
        self.bullet_width = 15
        self.bullet_color = (255,0,0)
        self.bullets_allowed = 3 
        # alien settings
        self.alien_speed = 1
        self.falling_speed = 10
        self.direction = 1
        # how quickly the game speeds up
        self.speedup_scale = 1
        # how quickly hit points increase
        self.pointup_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        "initialize settings that change throughout the game"
        self.rocket_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 1
        self.fleet_direction = 1
        self.alien_point = 10

    def increase_speed(self):
        "increase speed settings"
        self.rocket_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        "increase points settings"
        self.alien_point = int(self.alien_point * self.pointup_scale)
