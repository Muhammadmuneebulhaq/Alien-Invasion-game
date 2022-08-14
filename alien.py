import pygame
from pygame.sprite import Sprite
from rocket import Rocket

class Alien(Sprite):
    '''class to manage the alien object'''
    def __init__(self, ai_game):
        '''initializing the position of the alien'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.rocket = Rocket(self)
        '''alien image'''
        self.image = pygame.image.load('Gallery\\alien.jpg')
        self.rect = self.image.get_rect()

        # coordinates
        self.x = self.rect.width
        self.y = self.rect.height

        self.x = float(self.rect.x + self.rocket.rect.width + 100)
        self.y = float(self.rect.y)

    def update(self):
        # changing the horizontal position
        self.y += self.settings.alien_speed*self.settings.direction
        self.rect.y = self.y
 
    def check_edges(self):
        if self.rect.top <= 0:
            return True
        elif self.rect.bottom >= self.settings.screen_height:
            return True
            