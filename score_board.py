from email.headerregistry import Group
import pygame.font
import pygame
from pygame.sprite import Sprite
from rocket import Rocket

class Scoreboard:
    "a class to report scoring information"
    def __init__(self, ai_game):
        """initialize scorekeeping attributes"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # font settings for scores
        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        # prepare initial score
        self.prep_score()
        self.prep_level()
        self.prep_highscore()
        self.prep_rockets()
        
    def prep_score(self):
        """To turn the score into a rendered image"""
        rounded_score = round(self.stats.score, -1)
        str_score = "{:,}".format(rounded_score)
        self.score_image = self.font.render(str_score, True, self.text_color, self.settings.bg_color)
        
        # display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_level(self):
        """To turn the level into a rendered image"""
        str_level = str(self.stats.level)
        self.level_image = self.font.render(str_level, True, self.text_color, self.settings.bg_color)
        
        # display the score at the top right of the screen
        self.level_rect = self.score_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = 50

    def show_score(self):
        """draw score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highscore_image, self.highscore_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.rockets.draw(self.screen)
        
    def prep_highscore(self):
        self.highscore = "{:,}".format(self.stats.highscore)
        self.highscore_image = self.font.render(self.highscore, True, self.text_color, self.settings.bg_color)

        # displaying score at the midtop of the screen
        self.highscore_rect = self.highscore_image.get_rect()
        self.highscore_rect.midtop = self.screen_rect.midtop
        
    def check_highscore(self):
        if self.stats.score > self.stats.highscore:
            self.stats.highscore = self.stats.score
            self.prep_highscore()

    def prep_rockets(self):
        """shows how many rockets are left"""
        self.rockets = pygame.sprite.Group()
        for rocket_number in range(self.stats.rockets_left):
            rocket = Rocket(self.ai_game)
            rocket.rect.x = 10 + rocket_number*rocket.rect.width
            rocket.rect.y = 10
            self.rockets.add(rocket)