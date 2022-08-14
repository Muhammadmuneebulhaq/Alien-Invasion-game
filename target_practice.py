import time
import pygame
import alien_invasion
from settings import Settings
from rocket import Rocket

class targetPractice:
    def __init__(self, ai_game):

        super().__init__()
        self.settings = Settings()
        self.rocket = Rocket(ai_game)
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('Gallery\\target.png')
        self.rect = self.image.get_rect()
        self.rect.topright = self.screen_rect.topright
        self.do_practice = False
        self.rect.y = self.rect.top
        self.y = float(self.rect.y)

    def start(self):
            self._update()
            #self.screen.fill(self.settings.bg_color)
            self._blit_target()
            #pygame.display.update()
    def _blit_target(self):
        self.screen.blit(self.image, self.rect)

    def _update(self):
        if self.rect.bottom >= self.settings.screen_height :
            self.settings.direction *= -1
        elif self.rect.top < 0:
            self.settings.direction *= -1
        self.y += self.settings.alien_speed*self.settings.direction
        self.rect.y = self.y
