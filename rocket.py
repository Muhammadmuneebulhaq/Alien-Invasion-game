import pygame
from pygame.sprite import Sprite

class Rocket(Sprite):
    '''class to manage the rocket'''
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #loading rocket image
        self.image = pygame.image.load('Gallery\\rocket.png')
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()

        #setting the location of the rocket to midbottom
        self.rect.midleft = self.screen_rect.midleft
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #movement detection
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        elif self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
        self.rect.x = self.x
        self.rect.y = self.y
    
    def midleft(self):
        self.rect.midleft = self.screen_rect.midleft
        self.x = float(self.rect.x)

    def reset_pos(self):
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False