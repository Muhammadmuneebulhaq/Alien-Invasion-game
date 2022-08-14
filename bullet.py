import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''class to manage the bullet'''
    def __init__(self, ai_game):
        '''create a bullet at current rocket position'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        # create bullet rect at (0, 0) and then assign current position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = ai_game.rocket.rect.midright
        # store bullet position as decimal value
        self.x = float(self.rect.x)

    def update(self):
        '''fires the bullet from the rocket'''
        #update decimal position of the bullet
        self.x += self.settings.bullet_speed
        # update the rect position
        self.rect.x = self.x

    def draw_bullet(self):
        '''this draws the bullet with current position '''
        pygame.draw.rect(self.screen, self.color, self.rect)

