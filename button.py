import pygame.font
import pygame

class Button:
    def __init__(self, ai_game, msg, rect_left, rect_top):
        # setting screen
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        length = len(msg)
        #setting dimensions
        self.height, self.width = 30, 27*length
        self.button_color = (255,255,255)
        self.text_color = (250, 0, 0)
        self.font = pygame.font.SysFont('Ariel', 50, True, True)
        #setting rect object
        self.rect = pygame.Rect( rect_left, rect_top, self.width, self.height)
        # setting button message
        self._prep_msg(msg)
        
    def _prep_msg(self, msg):
        '''turn message into a render image'''
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.rect.center = self.rect.center
        
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.rect)